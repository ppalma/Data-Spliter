#!/usr/bin/python
#----------------------------------------------------------------------------
# Name:         Picker.py
# Author:       Patricio Palma Solis
# Created:      2011/06/14 
#----------------------------------------------------------------------------

from ftplib import FTP
import datetime
from ftptool import FTPHost

class Picker:
	def __init__(self):
		self.ftp = None
		self.folder = None
		self.fromDate = datetime.datetime.now()
		self.toDate = datetime.datetime.now()
		self.stations = None
		self.connected = False
		self.format = "%a %b %d %H:%M:%S %Y"
		print "init Picker"

	def Connect(self,addr='',user='',passwd='',folder=''):
		if self.ftp == None:
			self.ftp = FTP(addr,user,passwd)
			self.addr= addr
			self.user = user
			self.passwd = passwd	
			connected = True
			self.folder=folder
			self.ftp.cwd(folder)

			print "Connected"
	def Disconnect(self):
		if self.ftp <> None:
			self.ftp.quit()
			connected = False	
			print "Disconnected"

	def SetFromDate(self,yy=0,mm=0,dd=0,h=0,m=0,s=0):
		self.fromDate = datetime.datetime(yy,mm,dd,h,m,s);

	def SetToDate(self,yy=0,mm=0,dd=0,h=0,m=0,s=0):
		self.toDate = datetime.datetime(yy,mm,dd,h,m,s);

	def GetFiles(self, directory):
		
		a_host = FTPHost.connect(self.addr,user=self.user,password=self.passwd)
		alld = {'': {}}
		print self.folder
		x=[]
		self.ftp.dir('-d','*/',lambda L:x.append(L.split()[-1]))
		print x
#		for (dirname, subdirs, files) in a_host.walk(self.folder):
#			d = alld
#			dirname = dirname[len(self.folder):]
#			print dirname
#			for subd in dirname.split('/'):
#				based = d
#				d = d[subd]
#			if subdirs:
#				for dn in subdirs:
#					d[dn] = {}
#			else:
#				based[subd] = files
		alld['':x]
		return alld['']
			
