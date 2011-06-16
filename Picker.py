#!/usr/bin/python
#----------------------------------------------------------------------------
# Name:         Picker.py
# Author:       Patricio Palma Solis
# Created:      2011/06/14 
#----------------------------------------------------------------------------

from ftplib import FTP
import datetime

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
			ftp = FTP(addr,user,passwd)
			connected = True
			ftp.cwd(folder)
			files = []
			files = ftp.retrlines('LIST')


			print "Connected"
	def Disconnect(self):
		if self.ftp <> None:
			ftp.quit()
			connected = False	
			print "Disconnected"

	def SetFromDate(self,yy=0,mm=0,dd=0,h=0,m=0,s=0):
		self.fromDate = datetime.datetime(yy,mm,dd,h,m,s);

	def SetToDate(self,yy=0,mm=0,dd=0,h=0,m=0,s=0):
		self.toDate = datetime.datetime(yy,mm,dd,h,m,s);

	def GetFiles(self):
		Huds = ['20110407_1200huds0e.gcf','20110407_1200huds0n.gcf','20110407_1200huds0z.gcf']
		Malva = ['20110331_1500malvae.gcf','20110331_1500malvan.gcf','20110331_1500malvaz.gcf']
		Meli = ['20110517_0800e.gcf','20110517_0800n.gcf','20110517_0800z.gcf']
			
		Hudson = {}
		Hudson['Malva'] = Malva
		Hudson['Huds'] = Huds
		
		Melimoyu = {}
		Melimoyu['Meli'] = Meli

		volcan = {}
		volcan['Hudson'] = Hudson
		volcan['Melimoyu'] = Melimoyu
	#	print volcan['Hudson']['Malva']
	#	print volcan['Melimoyu']
		self.printr(volcan)

	def printr(self,d):
		if type(d) == type({}):
			print 'ii %s'%(d[d.keys()[0]])
			self.printr(d[d.keys()[0]])		
		if type(d) == type([]):
			print 'list'
		
