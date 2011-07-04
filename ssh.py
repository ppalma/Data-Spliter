#!/usr/bin/python

#
#  secure shell pipe module
#

import os
import sys
from socket import *


localPortNo=8000
maxTries=10
blockSize=65536*16

def createTCPSocketSSH (remoteHostname, remotePort=22, localPort=-1):
    global localPortNo
    if localPort == -1:
        localPort = localPortNo
        localPortNo = localPortNo+1
    tryNo = 1
    while 1:
      #  command = "ssh -f -g -A -X -N -T -L%d:localhost:%d %s\n" \
      #            % (localPort, remotePort, remoteHostname)
        command = "ssh ppalma@%s"%remoteHostname
	result = os.system(command)
        if result == 0:
            break
        localPort = localPort+1
        tryNo = tryNo + 1
        if tryNo == maxTries:
            os.exit(1)


    # create a TCP socket which connects to our ssh pipe
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", localPort))
    return s

createTCPSocketSSH('ssh.ppalma.cl')
