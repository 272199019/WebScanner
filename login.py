import re
import urllib2
import urllib
import httplib
import time
import socket

  
def login():

    HOSTSTR="http://business.eve.yeahtool.com/user/login"
    postdata={'token':'','param':'{"username":"111@qq.com","password":"123456"}','timezone':'8'}

    socket.setdefaulttimeout(30)    
    headers_values = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",  
             "Accept": "text/plain",'Referer':'http://111.111.111.111./2.1.5/login.html'}
    if postdata=='':           
            req = urllib2.Request(HOSTSTR,headers=headers_values)            
    else:
        req=urllib2.Request(HOSTSTR,urllib.urlencode(postdata),headers=headers_values)
    try:     
        page = urllib2.urlopen(req,timeout=30).read()   
        print page
      
    except urllib2.HTTPError,e:  
        print e.code    
        return None
    except urllib2.URLError,e:
        print e.reason  
        return None         
    except httplib.BadStatusLine,e:
        print 'BadStatusLine'     
        return None           
    except socket.error,e:
        print (str(e)) 
        return None 
    else:
        return None      
if __name__ == "__main__":
   
    login()
        
       
            
