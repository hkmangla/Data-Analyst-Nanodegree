from bs4 import BeautifulSoup
soup = BeautifulSoup(open("carrier_and_airport.html"),"lxml")
carrier_list =  soup.find(id="CarrierList")
c = []
for i in carrier_list.find_all('option'):
	c.append(i['value'])
print c