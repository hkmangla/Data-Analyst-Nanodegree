import xml.etree.ElementTree as ET

data = {}
for _,element in ET.iterparse("sample1.osm"):
	if element.tag not in data.keys():
		data[element.tag] = 1
	else:
		data[element.tag] +=1
print data