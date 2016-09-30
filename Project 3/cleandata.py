import csv
import pandas as pd
#with open("nodes_tags.csv",'r') as ff:
#	f = csv.reader(ff)
#	data = pd.DataFrame(f)
#	print data
data = pd.read_csv(r'nodes_tags.csv')
print data
