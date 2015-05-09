# -*- coding: utf-8 -*-
import scan
import difflib
import colprint
import re
import datetime
from Queue import Queue
from bs4 import BeautifulSoup
from sqlinjectclass import SqlInject

class PathScan():
    
    Scanner=scan.scanclass()
    def __init__(self):
        print ''
    def serverbanner(self,target):                     
        result=self.Scanner.GetData(target,'OPTIONS')#OPTIONS is Enable
        if result[1]==200 and (result[2].get('allow',1))!=1:
            colprint.strprint(2,'\nOPTIONS is Enable:  '+result[2]['allow'])
            PutEnable=re.search('PUT',result[2]['allow'])
            if PutEnable:
                colprint.strprint(4,'PUT Method is Enable!')
                
        result=self.Scanner.GetData(target)# Server Banner
        print result
        if result[1]==200 and (result[2].get('server',1))!=1:
            colprint.strprint(2,'Server:'+result[2]['server'])
        if result[1]==200 and (result[2].get('x-powered-by',1))!=1:
            colprint.strprint(2,'x-powered-by:'+result[2]['x-powered-by'])
        
        result=self.Scanner.GetData(target+'robots.txt',regstr='*')#Server robots.txt
        if result[1]==200:
            colprint.strprint(2,'robots.txt')
            colprint.strprint(2,result[2])

    def path(self,target):

        result=self.Scanner.GetData(target+'../../../../../../../../../../../../windows/win.ini')
        print result[2]
        result=self.Scanner.GetData(target+'../../../../../../../../../../../etc/passwd%00')
        print result[2]
        with open(r'urlpath.txt') as f:   
            for line in f:
                print line
                url=target+line
                result=self.Scanner.GetData(url) 
                print result[0]    
                if result[0]==url.strip(): 
                    print result[1]
                else:
                    print '302'
                    
        urltoscan=target
        urltoscan=urltoscan.replace('http://','',1).replace('.cn','',1).replace('.com','',1).replace('.edu','',1).replace('www.','',1).replace('.net','',1)

        WEBBAK=['web.rar','web.bak','web.tar.gz',urltoscan+'.rar']
        for x in WEBBAK:
            url=target+x
            result=self.Scanner.GetData(url)
            print result[:2]
        for x in xrange(0,61):
            datestr=datetime.date.today()-datetime.timedelta(x)
            datestr=datestr.strftime('%Y-%m-%d').replace('-','',2)
            url=target+datestr+'.rar'
            result=self.Scanner.GetData(url)
            print result[:2]
        
       
    
    # zhengli lujin
    def urlget(self,target):#url list
        result=self.Scanner.GetData(target,regstr='*')
        urldict={}
        if result[1]==200: #<a href=>
            soup=BeautifulSoup(result[2])
            for link in  soup.find_all('a'):
                if link.get('href'):
                    if  link.get('href').startswith(target):
                        urldict[link.get('href')]=link.get('href')
                     
                    #White List or Black List?
                    STARTLIST=['/','../','./','?']
                    for i in STARTLIST:
                        if  link.get('href').startswith(i):
                            fullurl=target+link.get('href') 
                            urldict[fullurl]=fullurl
        return urldict

    def urllist(self,target):
        urldictresult={}
        urldict1=self.urlget(target)
        for x in urldict1:
            urldict2=self.urlget(x)
            urldictresult = urldict1.copy()
            urldictresult.update(urldict2)        
        return urldictresult
            
    def sqlinjectscan(self,target):  
       
        toscanurl=self.urllist(target)
        for x in toscanurl:
            SqlInject().ScanSql(x)
        















        
