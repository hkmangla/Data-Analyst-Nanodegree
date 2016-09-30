

#CSV File function
with open(file,mode) as variable_name #open file
string_var.split(',') #change string into list
string_var.strip() # avoid '\n' from file
.readline() #read line from file
os.path.join(file_location,file_name) #save file in variable
csv.reader(asfile) # return csv reader object of file asfile
csv.DictReader(asfile) #return csv DictReader file  
.next() #return next line of csv reader file
list_name.index(value) #return index of value in list list_name
write_file = csv.writer(csv_file, delimiter = any_symbol) # return a file object of file csv_file for write in it
write_file.writerow(row_line) #write row_line in write_file 




#XLS file function
openfile = xlrd.open_workbook(filename) #open file
readfile = openfile.sheet_by_index(0) # read file
readfile.cell_value(row,col) #cell value of index [row,col]
readfile.nrows #number of rows
readfile.ncols #number of columns
readfile.col_values(col_number , start_rowx = start_index, end_rowx= end_index) # slice column from start_index to end_index
readfile.cell_type(row,col) # type of cell having index [row, col]
realtime = xlrd.xldate_as_tuple(xltime,0) # change date into tuple format

#JSON file function
param["fmt"] = "json"
requests.get(url , params = param, proxies = proxy) # request data from url in json format

