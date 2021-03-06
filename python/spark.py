import logging
import sys
import ConfigParser
from threading import Thread
import time
import os



logging.basicConfig(stream=sys.stdout, level=logging.INFO)

LOG = logging.getLogger(__name__)

def suiterun (tname,ctx,version,sdir,suits,run,r):
    logging.info ("Running %s", tname)

    try:
        # Run dictates how many times to run all the suits
        # runs are executed serially
        while run > 0:
            run = run  -1

            # For each run we iterate through configured Suits and execute them
            for i in suits:
                # suiteparams:  database:suite_name
                suitparams = i.split (":")
                topdir = sdir+"/" + suitparams[1] + "/spark"+ version

                with open(topdir + "/query_order.txt", 'r') as orderfile:
                    for name in orderfile:
                        name = name.rstrip()

                        with open(topdir + "/" + name, 'r') as queryfile:

                            query = queryfile.read()
                            now = time.time()
                            # execute query
                            ctx.sql ("use " + suitparams[0])
                            results = ctx.sql (query).collect ()
                            ############ close cursor
                            duration  = time.time() - now
                            # Append the result to file
                            f = open (r,'a')
                            resultline = "spark"+version+","+tname+","+suitparams[1]+","+name + "," +  run.__str__() + "," + duration.__str__()+"\n"
                            f.write(resultline)
                            f.close()
    except Exception, e:
        logging.error ("Could not execute: " + name + " with exception " + e.__str__())


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.fatal("Usage: <%s> <config file>" , sys.argv[0])
        sys.exit(-1)

    Config = ConfigParser.ConfigParser()
    Config.read(sys.argv[1])
    spark_location =  Config.get("connectioninfo","spark_location")
    spark_version =  Config.get("connectioninfo","spark_version")
    spark_executor_num =  Config.get("connectioninfo","spark_executor_num")
    spark_executor_mem =  Config.get("connectioninfo","spark_executor_mem")
    spark_executor_cores =  Config.get("connectioninfo","spark_executor_cores")
    spark_driver_mem =  Config.get("connectioninfo","spark_driver_mem")
    spark_auto_broadcast =  Config.get("connectioninfo","spark_auto_broadcast")

    suitList = Config.get("testinfo","suits").split(",")
    iterations = Config.getint("testinfo","iterations")
    results = Config.get("testinfo", "resultsfile")
    concurrency = Config.getint("testinfo","concurrency")
    suit_dir = Config.get("testinfo","suit_dir")

    # Depending on Spark version chose a different version of Spark on the system
    # Location is coming from the config file
    os.environ['SPARK_HOME'] = spark_location
    os.environ['PYTHONPATH'] = spark_location + "/python:"+ spark_location + "/python/lib/usr/lib/spark:$PYTHONPATH"
    os.environ['HADOOP_CONF_DIR'] = "/etc/hadoop/conf"
    os.environ['YARN_CONF_DIR'] = "/etc/hadoop/conf"
    sys.path.append(spark_location + "/python")


    from pyspark.sql import HiveContext
    from pyspark import SparkContext, SparkConf

    try:
      if spark_version == "2.0":
            from pyspark.sql import SparkSession
            sqlContext = SparkSession.builder.master("yarn").appName("Spark2 SQL Driver")\
                .config("spark.executor.instances", spark_executor_num)\
                .config("spark.executor.memory", spark_executor_mem)\
                .config("spark.driver.memory", spark_driver_mem)\
                .config("spark.executor.cores", spark_executor_cores)\
                .config("spark.sql.autoBroadcastJoinThreshold", spark_auto_broadcast)\
                .enableHiveSupport().getOrCreate ()
      else:
        conf = SparkConf()
        conf.setAppName("Spark1 SQL Driver")
        conf.set("spark.executor.instances", spark_executor_num )
        conf.set("spark.executor.memory", spark_executor_mem)
        conf.set("spark.executor.cores", spark_executor_cores)
        conf.set("spark.driver.memory", spark_driver_mem)
        conf.set("spark.sql.autoBroadcastJoinThreshold", spark_auto_broadcast)
        sc = SparkContext (conf=conf)
        sqlContext = HiveContext(sc)

      # Concurrency dictates # of concurrent connections to Spark
      # We will spin up a different thread per connection
      # We pass SqlContext or SparkSession depending on version to threads
      #    Assume SqlContext / SparkSession are thread safe, which should be the case
      threads = []
      while concurrency > 0:
        name = "Thread #" + concurrency.__str__()
        try:
            thread = Thread (target=suiterun,args = (name,sqlContext,spark_version,suit_dir,suitList,iterations,results))
            threads.append(thread)
        except:
            logging.fatal("Unable to start thread %s", name)
        concurrency = concurrency-1
      for t in threads:
        t.start()
      for t in threads:
        t.join()
    except Exception, e:
        logging.error ("Exception encountered: " +  str(e))
        sys.exit (1)

    logging.info ("Spark " + spark_version + ".  All Done.")
