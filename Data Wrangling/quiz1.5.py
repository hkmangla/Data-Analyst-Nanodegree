from bs4 import BeautifulSoup
import requests
http_proxy  = "http://192.168.100.12:3128"
https_proxy = "https://192.168.100.12:3128"
ftp_proxy   = "ftp://192.168.100.12:3128"
s = requests.Session()
proxy = { 
           "http"  : http_proxy, 
            "https" : https_proxy, 
            "ftp"   : ftp_proxy
        }
def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    },proxies=proxy)

    return r.text
s= requests.Session()
r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",proxies=proxy)    
soup = BeautifulSoup(r.text,"lxml")
data = {}
v = soup.find(id = "__EVENTVALIDATION")
data['eventvalidation'] = v['value']
ve = soup.find(id="__VIEWSTATE")
data['viewstate'] = ve['value']

f = open("virgin_logan_airport.html","w")
f.write(make_request(data))