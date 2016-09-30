##  A customer with the FirstName Helena has been declard your best customer.
##  She definitely deserves an email thanking her for their patronage :)  

##  Build a query that returns Helena's email, first name, last name, 
##  and the sum of all invoices she has received.


QUERY ='''
SELECT c.Email,c.FirstName,c.LastName,sum(Invoice.Total) FROM Customer c,Invoice WHERE
c.CustomerId = Invoice.CustomerId group by c.CustomerId order by Invoice.Total desc limit 1;
'''

'''
---VISUAL GUIDE---

Before Query...

###############         ####################   
#  Customer   #         #     Invoice      #   <-----  FROM/JOIN
###############         ####################   
|  CustomerId | = ON  = | CustomerId       |   
+=============+         +==================+  
|  FirstName  |         | Total            |  <-----  WHERE Total > 10.00
+=============+         +==================+  
|  LastName   |     
+=============+                 
|  Email      |               
+=============+

After Query...

###################################################   
#             CustomerInvoice                     #   <-----  RESULT!
###################################################   
|  Email  |  FirstName | LastName    |    Total   |
+=========+============+=============+============+

'''









    