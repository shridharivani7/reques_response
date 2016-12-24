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
    

