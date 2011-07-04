#!/usr/bin/python

from socket import *
import os
myHost = '127.0.0.1'
myPort = 2000

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket
s.bind((myHost, myPort))            # bind it to the server port
s.listen(5)                         # allow 5 simultaneous
                                    # pending connections


while 1:
    # wait for next client to connect
    connection, address = s.accept() # connection is a new socket
    while 1:
        data = connection.recv(1024) # receive up to 1K bytes
        if data:
            connection.send('echo -> '+data)
	    print data
	    os.system('export EW_HOME=/home/ppalma/Desktop/earthworm_7.4/')
	    os.system('export EW_VERSION=v7.4')

	    os.system('export EW_RUN_DIR=${EW_HOME}/Run_OVC')
	    os.system('export SYS_NAME=`hostname`')
	    os.system('export EW_INSTALLATION=INST_OVDAS')
	    os.system('export EW_PARAMS=${EW_RUN_DIR}/Params/')
	    os.system('export EW_LOG=${EW_RUN_DIR}/Logs/')
	    os.system('export PATH=$PATH:${EW_HOME}/bin')
	    os.system('/home/ppalma/Desktop/earthworm_7.4/bin/reconfigure')
	    os.system(data)

        else:
            break
    connection.close()              # close socket
