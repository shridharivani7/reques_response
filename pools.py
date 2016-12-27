from multiprocessing import Pool, TimeoutError
import time
import requests
import json
def fetch_url(i):
    
    url="http://surya-interview.appspot.com/message"
    
    headers={'X-Surya-Email-Id':'shridharsjce@gmail.com'}
    #request.get function
    r=requests.get(url,headers=headers)
    x=r.json()
    #print "Request :", r.status_code,x
    #request.post function
    data=x
    r=requests.post(url,data=json.dumps(x))
    #print "Response :", r.status_code,r.content
    print i,"Percentile"
    return 
    
if __name__ == "__main__":
    jobs = []
    pool = Pool(processes=10)
    pool.map(fetch_url, range(100))
    
    pool.close()
    pool.join()
    
    
    
#Revised Way to do
from multiprocessing import Pool, TimeoutError
import time
import requests
import json
def fetch_url(i):
    url="http://surya-interview.appspot.com/message"
    
    headers={'X-Surya-Email-Id':'shridharsjce@gmail.com'}
    #request.get function
    r=requests.get(url,headers=headers)
    x=r.json()
    #print "Request :", r.status_code,x
    #request.post function
    data=x
    r=requests.post(url,data=json.dumps(x))
    if i in [10,50,90,95,99,100,101]:
        if i == 100:
            print "Mean"
        elif i == 101:
            print "Standard Deviation"
        else:
            print i,"th Percentile"
        return 
    
if __name__ == "__main__":
    jobs = []
    pool = Pool(processes=10)
    pool.map(fetch_url, range(102))
    
    pool.close()
    pool.join()

    

