#!/usr/bin/python

import sys
from socket import *
serverHost = 'localhost'            # servername is localhost
serverPort = 2000                   # use arbitrary port > 1024

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket


s.connect((serverHost, serverPort)) # connect to server on the port
s.send('/home/ppalma/Desktop/earthworm_7.4/bin/reconfigure')               # send the data
data = s.recv(1024)                 # receive up to 1K bytes
print data
