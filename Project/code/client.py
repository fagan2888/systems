#!/usr/bin/env python
#
# Autogenerated by Thrift Compiler (0.9.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

import sys
import pprint
from urlparse import urlparse
from thrift.transport import TTransport
from thrift.transport import TSocket
from thrift.transport import THttpClient
from thrift.protocol import TBinaryProtocol

from ml import MLEngine
from ml.ttypes import *

if len(sys.argv) <= 1 or sys.argv[1] == '--help':
  print ''
  print 'Usage: ' + sys.argv[0] + ' [-h host[:port]] [-u url] [-f[ramed]] function [arg1 [arg2...]]'
  print ''
  print 'Functions:'
  print '  double Predict(i32 id, string x)'
  print '  void Learn(string x, double y)'
  print '  void LearnFromID(i32 id, double y)'
  print '  double AvgPredictionTime()'
  print '  void Test()'
  print ''
  sys.exit(0)

pp = pprint.PrettyPrinter(indent = 2)
host = 'localhost'
port = 9090
uri = ''
framed = False
http = False
argi = 1

if sys.argv[argi] == '-h':
  parts = sys.argv[argi+1].split(':')
  host = parts[0]
  if len(parts) > 1:
    port = int(parts[1])
  argi += 2

if sys.argv[argi] == '-u':
  url = urlparse(sys.argv[argi+1])
  parts = url[1].split(':')
  host = parts[0]
  if len(parts) > 1:
    port = int(parts[1])
  else:
    port = 80
  uri = url[2]
  if url[4]:
    uri += '?%s' % url[4]
  http = True
  argi += 2

if sys.argv[argi] == '-f' or sys.argv[argi] == '-framed':
  framed = True
  argi += 1

cmd = sys.argv[argi]
args = sys.argv[argi+1:]

if http:
  transport = THttpClient.THttpClient(host, port, uri)
else:
  socket = TSocket.TSocket(host, port)
  if framed:
    transport = TTransport.TFramedTransport(socket)
  else:
    transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = MLEngine.Client(protocol)
transport.open()

if cmd == 'Predict':
  if len(args) != 2:
    print 'Predict requires 2 args'
    sys.exit(1)
  pp.pprint(client.Predict(eval(args[0]),args[1],))

elif cmd == 'Learn':
  if len(args) != 2:
    print 'Learn requires 2 args'
    sys.exit(1)
  pp.pprint(client.Learn(args[0],eval(args[1]),))

elif cmd == 'LearnFromID':
  if len(args) != 2:
    print 'LearnFromID requires 2 args'
    sys.exit(1)
  pp.pprint(client.LearnFromID(eval(args[0]),eval(args[1]),))

elif cmd == 'AvgPredictionTime':
  if len(args) != 0:
    print 'AvgPredictionTime requires 0 args'
    sys.exit(1)
  pp.pprint(client.AvgPredictionTime())

elif cmd == 'Test':
  if len(args) != 0:
    print 'Test requires 0 args'
    sys.exit(1)
  pp.pprint(client.Test())

else:
  print 'Unrecognized method %s' % cmd
  sys.exit(1)

transport.close()