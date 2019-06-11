#!/usr/bin/python

import requests
import os


pathpayload=" " #folder path of payload directory. example /opt/payload/
filepayload= " " #file name of payload. example xss-payload
attack = os.path.join(pathpayload, filepayload)


apiUrl = " " #api url. exam http://www.example.com/
pathUrl = " " #path api url. example json/login?
targetUrl = os.path.join(apiUrl, pathUrl)

def main():
    payload = bacapayload()
    pathresult = " " #folder path of result. example /opt/result
    successpayload = " " #file contain detected payload
    failpayload = " " #file contain undetected payload

    successpath = os.path.join(pathresult, successpayload)
    failpath = os.path.join(pathresult, failpayload)


    open(successpath, "w").close()
    open(failpath, "w").close()

    os.system("wc -l "+attack)

    for x in payload:
        payload = {"username" : x.strip(), "password":"assemble"}
        respon = requests.get(targetUrl, params=payload)
        if respon.status_code == 200:
            f = open(failpath, "a")
            f.write(x)
            f.close()
        elif respon.status_code == 401:
            f = open(failpath, "a")
            f.write(x)
            f.close()
        elif respon.status_code == 403:
            f = open(successpath, "a")
            f.write(x)
            f.close()
        else:
            print ("payload apa nih??", x)

        respon.close()
    

    os.system("wc -l "+successpath)
    os.system("wc -l "+failpath)




def bacapayload():
     f = open(attack, "r")
     f1 = f.readlines()

     return f1


if __name__=="__main__":
    main()

