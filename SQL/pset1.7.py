##  The show was a huge hit! Congratulations on all your hard work :)  
##  After the popularity of your first show you've decided to jump on the
##  railway for an Alternative & Punk tour through France!  

##  What does the alternative punk scene look like throughout French 
##  cities in your dataset?

##  Return the BillingCities in France, followed by the total number of 
##  tracks purchased for Alternative & Punk music.
##  Order your output so that the city with the most invoices is on top.


QUERY = '''
SELECT i.BillingCity,COUNT(*) as NumTracks FROM Invoice i,InvoiceLine il,Track t,Genre g
WHERE i.InvoiceId = il.InvoiceId and il.TrackId = t.TrackId and t.GenreId = g.GenreId
and i.BillingCountry = 'France' and g.name = 'Alternative & Punk'
group by BillingCity
order by NumTracks desc;
'''


'''
---Visual Guide---

Before Query...

#################       #################       #############      #############
#    Invoice    #       #  InvoiceLine  #       #   Track   #      #   Genre   #
#################       #################       #############      #############
|  InvoiceId    | --->  |  InvoiceId    |       |  GenreId  | ---> |  GenreId  |
+---------------+       +---------------+       +-----------+      +-----------+
|  BillingCity| |       |  TrackId      |  ---> |  TrackId  |      |  Name     |  
+---------------+       +---------------+       +-----------+      +-----------+
| BillingCountry|
+---------------+

After Query..

###############################
#        InvoiceGenre         #
###############################
|  BillingCity  |  NumTracks  |
+---------------+-------------+

'''