#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import impala._thrift_gen.Status.ttypes
import impala._thrift_gen.Types.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TExecState(object):
  REGISTERED = 0
  PLANNING = 1
  QUEUED = 2
  RUNNING = 3
  FINISHED = 4
  CANCELLED = 5
  FAILED = 6

  _VALUES_TO_NAMES = {
    0: "REGISTERED",
    1: "PLANNING",
    2: "QUEUED",
    3: "RUNNING",
    4: "FINISHED",
    5: "CANCELLED",
    6: "FAILED",
  }

  _NAMES_TO_VALUES = {
    "REGISTERED": 0,
    "PLANNING": 1,
    "QUEUED": 2,
    "RUNNING": 3,
    "FINISHED": 4,
    "CANCELLED": 5,
    "FAILED": 6,
  }


class TExecStats(object):
  """
  Attributes:
   - latency_ns
   - cpu_time_ns
   - cardinality
   - memory_used
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'latency_ns', None, None, ), # 1
    (2, TType.I64, 'cpu_time_ns', None, None, ), # 2
    (3, TType.I64, 'cardinality', None, None, ), # 3
    (4, TType.I64, 'memory_used', None, None, ), # 4
  )

  def __init__(self, latency_ns=None, cpu_time_ns=None, cardinality=None, memory_used=None,):
    self.latency_ns = latency_ns
    self.cpu_time_ns = cpu_time_ns
    self.cardinality = cardinality
    self.memory_used = memory_used

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.latency_ns = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.cpu_time_ns = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.cardinality = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.memory_used = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TExecStats')
    if self.latency_ns is not None:
      oprot.writeFieldBegin('latency_ns', TType.I64, 1)
      oprot.writeI64(self.latency_ns)
      oprot.writeFieldEnd()
    if self.cpu_time_ns is not None:
      oprot.writeFieldBegin('cpu_time_ns', TType.I64, 2)
      oprot.writeI64(self.cpu_time_ns)
      oprot.writeFieldEnd()
    if self.cardinality is not None:
      oprot.writeFieldBegin('cardinality', TType.I64, 3)
      oprot.writeI64(self.cardinality)
      oprot.writeFieldEnd()
    if self.memory_used is not None:
      oprot.writeFieldBegin('memory_used', TType.I64, 4)
      oprot.writeI64(self.memory_used)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TPlanNodeExecSummary(object):
  """
  Attributes:
   - node_id
   - fragment_id
   - label
   - label_detail
   - num_children
   - estimated_stats
   - exec_stats
   - is_active
   - is_broadcast
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'node_id', None, None, ), # 1
    (2, TType.I32, 'fragment_id', None, None, ), # 2
    (3, TType.STRING, 'label', None, None, ), # 3
    (4, TType.STRING, 'label_detail', None, None, ), # 4
    (5, TType.I32, 'num_children', None, None, ), # 5
    (6, TType.STRUCT, 'estimated_stats', (TExecStats, TExecStats.thrift_spec), None, ), # 6
    (7, TType.LIST, 'exec_stats', (TType.STRUCT,(TExecStats, TExecStats.thrift_spec)), None, ), # 7
    (8, TType.LIST, 'is_active', (TType.BOOL,None), None, ), # 8
    (9, TType.BOOL, 'is_broadcast', None, None, ), # 9
  )

  def __init__(self, node_id=None, fragment_id=None, label=None, label_detail=None, num_children=None, estimated_stats=None, exec_stats=None, is_active=None, is_broadcast=None,):
    self.node_id = node_id
    self.fragment_id = fragment_id
    self.label = label
    self.label_detail = label_detail
    self.num_children = num_children
    self.estimated_stats = estimated_stats
    self.exec_stats = exec_stats
    self.is_active = is_active
    self.is_broadcast = is_broadcast

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.node_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.fragment_id = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.label = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.label_detail = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.num_children = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRUCT:
          self.estimated_stats = TExecStats()
          self.estimated_stats.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.exec_stats = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TExecStats()
            _elem5.read(iprot)
            self.exec_stats.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.is_active = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readBool();
            self.is_active.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.BOOL:
          self.is_broadcast = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TPlanNodeExecSummary')
    if self.node_id is not None:
      oprot.writeFieldBegin('node_id', TType.I32, 1)
      oprot.writeI32(self.node_id)
      oprot.writeFieldEnd()
    if self.fragment_id is not None:
      oprot.writeFieldBegin('fragment_id', TType.I32, 2)
      oprot.writeI32(self.fragment_id)
      oprot.writeFieldEnd()
    if self.label is not None:
      oprot.writeFieldBegin('label', TType.STRING, 3)
      oprot.writeString(self.label)
      oprot.writeFieldEnd()
    if self.label_detail is not None:
      oprot.writeFieldBegin('label_detail', TType.STRING, 4)
      oprot.writeString(self.label_detail)
      oprot.writeFieldEnd()
    if self.num_children is not None:
      oprot.writeFieldBegin('num_children', TType.I32, 5)
      oprot.writeI32(self.num_children)
      oprot.writeFieldEnd()
    if self.estimated_stats is not None:
      oprot.writeFieldBegin('estimated_stats', TType.STRUCT, 6)
      self.estimated_stats.write(oprot)
      oprot.writeFieldEnd()
    if self.exec_stats is not None:
      oprot.writeFieldBegin('exec_stats', TType.LIST, 7)
      oprot.writeListBegin(TType.STRUCT, len(self.exec_stats))
      for iter12 in self.exec_stats:
        iter12.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.is_active is not None:
      oprot.writeFieldBegin('is_active', TType.LIST, 8)
      oprot.writeListBegin(TType.BOOL, len(self.is_active))
      for iter13 in self.is_active:
        oprot.writeBool(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.is_broadcast is not None:
      oprot.writeFieldBegin('is_broadcast', TType.BOOL, 9)
      oprot.writeBool(self.is_broadcast)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.node_id is None:
      raise TProtocol.TProtocolException(message='Required field node_id is unset!')
    if self.fragment_id is None:
      raise TProtocol.TProtocolException(message='Required field fragment_id is unset!')
    if self.label is None:
      raise TProtocol.TProtocolException(message='Required field label is unset!')
    if self.num_children is None:
      raise TProtocol.TProtocolException(message='Required field num_children is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TExecSummary(object):
  """
  Attributes:
   - state
   - status
   - nodes
   - exch_to_sender_map
   - error_logs
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'state', None, None, ), # 1
    (2, TType.STRUCT, 'status', (impala._thrift_gen.Status.ttypes.TStatus, impala._thrift_gen.Status.ttypes.TStatus.thrift_spec), None, ), # 2
    (3, TType.LIST, 'nodes', (TType.STRUCT,(TPlanNodeExecSummary, TPlanNodeExecSummary.thrift_spec)), None, ), # 3
    (4, TType.MAP, 'exch_to_sender_map', (TType.I32,None,TType.I32,None), None, ), # 4
    (5, TType.LIST, 'error_logs', (TType.STRING,None), None, ), # 5
  )

  def __init__(self, state=None, status=None, nodes=None, exch_to_sender_map=None, error_logs=None,):
    self.state = state
    self.status = status
    self.nodes = nodes
    self.exch_to_sender_map = exch_to_sender_map
    self.error_logs = error_logs

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.state = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.status = impala._thrift_gen.Status.ttypes.TStatus()
          self.status.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.nodes = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = TPlanNodeExecSummary()
            _elem19.read(iprot)
            self.nodes.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.exch_to_sender_map = {}
          (_ktype21, _vtype22, _size20 ) = iprot.readMapBegin()
          for _i24 in xrange(_size20):
            _key25 = iprot.readI32();
            _val26 = iprot.readI32();
            self.exch_to_sender_map[_key25] = _val26
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.error_logs = []
          (_etype30, _size27) = iprot.readListBegin()
          for _i31 in xrange(_size27):
            _elem32 = iprot.readString();
            self.error_logs.append(_elem32)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TExecSummary')
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 1)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.STRUCT, 2)
      self.status.write(oprot)
      oprot.writeFieldEnd()
    if self.nodes is not None:
      oprot.writeFieldBegin('nodes', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.nodes))
      for iter33 in self.nodes:
        iter33.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.exch_to_sender_map is not None:
      oprot.writeFieldBegin('exch_to_sender_map', TType.MAP, 4)
      oprot.writeMapBegin(TType.I32, TType.I32, len(self.exch_to_sender_map))
      for kiter34,viter35 in self.exch_to_sender_map.items():
        oprot.writeI32(kiter34)
        oprot.writeI32(viter35)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.error_logs is not None:
      oprot.writeFieldBegin('error_logs', TType.LIST, 5)
      oprot.writeListBegin(TType.STRING, len(self.error_logs))
      for iter36 in self.error_logs:
        oprot.writeString(iter36)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.state is None:
      raise TProtocol.TProtocolException(message='Required field state is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
