from itertools import *
def PasswordDic(username):
    dic=[]
    dictlist=[]
    f=open('dict.txt','r')
    for pwd in f:
        dic.append(pwd.strip())
    f.close()
    for (Pwd,UsernameStr) in product(username,dic):
        dictlist.append(Pwd+UsernameStr)
    f=open('pw.txt','a')
    for line in dictlist:
        f.write(line+'\n')
    f.close()
    return dictlist    


PasswordDic(['ppzcadmin'])

