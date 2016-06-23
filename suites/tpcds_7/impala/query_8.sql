
select  s_store_name
      ,sum(ss_net_profit)
 from store_sales
     ,date_dim
     ,store,
     (select ca_zip
     from (
      SELECT substr(ca_zip,1,5) ca_zip
      FROM customer_address
      WHERE substr(ca_zip,1,5) IN (
                          '37650','11903','52277','57021','44720','27796',
                          '72809','25950','18371','22720','54422',
                          '56215','63210','17096','33400','26581',
                          '11702','26142','54888','48285','20407',
                          '57596','99376','98218','68686','32796',
                          '19694','17359','43309','41128','90053',
                          '15799','70938','34715','58436','79756',
                          '17289','80691','94172','62308','20123',
                          '38032','44333','77118','24530','93471',
                          '12009','96756','29683','58270','36773',
                          '98354','68919','37705','92383','26784',
                          '61375','83491','40262','86322','52173',
                          '91722','68903','91880','14314','46125',
                          '34178','21767','37664','87322','61146',
                          '15574','86950','47546','25997','70707',
                          '11560','93751','56473','32457','25890',
                          '77661','39404','38559','67766','74778',
                          '42501','44594','13740','58205','98842',
                          '10568','27497','57234','92677','15922',
                          '14233','94125','48406','51473','29673',
                          '32577','29804','38471','41415','80919',
                          '30072','86780','77569','64388','39003',
                          '97540','47275','29488','43689','59822',
                          '47020','14697','23595','88123','97968',
                          '22747','11159','83338','48932','12774',
                          '21910','48387','10672','69441','43713',
                          '12737','35172','24377','48076','68611',
                          '28925','35276','14707','28393','15543',
                          '94981','48491','38668','30436','11237',
                          '69481','33813','87699','29072','13281',
                          '36655','76303','17335','36885','33292',
                          '68778','68639','67748','39417','19473',
                          '22452','37182','33744','46667','38935',
                          '56247','84775','84681','56829','22147',
                          '14928','77556','11090','43164','34927',
                          '28540','24090','12386','30179','26972',
                          '68353','36776','76892','50142','29191',
                          '29885','52314','10531','20864','97162',
                          '11585','95558','81171','59030','46199',
                          '64445','14514','54011','70830','42121',
                          '52732','47680','11582','37358','65412',
                          '59997','67929','12664','14461','32284',
                          '28268','62017','60236','61123','63243',
                          '31045','49052','61093','94376','60034',
                          '46205','45025','19433','84999','90572',
                          '44531','60730','10246','77645','23209',
                          '22039','46239','32889','57864','29773',
                          '17838','95165','84058','25198','97879',
                          '87064','47045','68476','29448','59045',
                          '25971','16688','13627','21730','44939',
                          '11914','66637','27850','52276','16650',
                          '35572','33329','33094','67864','49225',
                          '59191','24064','11378','47269','32902',
                          '14732','87190','37160','93522','39338',
                          '16472','12107','28663','64305','20904',
                          '58302','37724','28238','62404','67179',
                          '16205','39882','53508','63882','38488',
                          '41523','14261','14484','80247','22470',
                          '21484','82954','46711','39483','22250',
                          '51765','34150','95548','97998','35784',
                          '42334','97823','19542','17801','68083',
                          '78723','21245','26525','13793','88851',
                          '76991','17959','11445','30598','23275',
                          '76947','68721','13476','13444','20110',
                          '59219','39583','76844','16041','36028',
                          '32612','60699','91277','32155','14661',
                          '70263','85755','43638','98766','31107',
                          '83554','12721','43558','37256','23487',
                          '79523','28745','86378','71515','34164',
                          '89060','62601','27952','44088','53347',
                          '26211','89858','39946','56597','22214',
                          '36635','29978','81719','89134','27707',
                          '22715','78923','18499','54993','26741',
                          '44160','65002','14119','64887','13538',
                          '82781','88434','60696','69148','69626',
                          '57710','17665','57205','42427','36050',
                          '22634','94633','48871','54760','21661',
                          '78420','31422','93654','45899','85785',
                          '60572','16866','69786','32063','86598',
                          '51921','12859','65531','11900')
     intersect
      select ca_zip
      from (SELECT substr(ca_zip,1,5) ca_zip,count(*) cnt
            FROM customer_address, customer
            WHERE ca_address_sk = c_current_addr_sk and
                  c_preferred_cust_flag='Y'
            group by ca_zip
            having count(*) > 10)A1)A2) V1
 where ss_store_sk = s_store_sk
  and ss_sold_date_sk = d_date_sk
  and d_qoy = 1 and d_year = 2001
  and (substr(s_zip,1,2) = substr(V1.ca_zip,1,2))
 group by s_store_name
 order by s_store_name
 limit 100;

