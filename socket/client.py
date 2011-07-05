#!/usr/bin/python

import sys
from socket import *
serverHost = 'localhost'            # servername is localhost
serverPort = 6666               # use arbitrary port > 1024

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket


s.connect((serverHost, serverPort)) # connect to server on the port
s.send('waveman2disk')               # send the data
data = s.recv(1024)                 # receive up to 1K bytes
print data
