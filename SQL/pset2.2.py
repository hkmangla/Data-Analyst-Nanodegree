import sqlite3

c = sqlite3.connect("chinook.db")
cur = c.cursor()
query = """select count(g.name),i.CustomerId,g.Name from Invoice i,InvoiceLine l,Track t,Customer c,Genre g where c.CustomerId = i.CustomerId and i.InvoiceId = l.InvoiceId 
and l.TrackId = t.TrackId and t.GenreId = g.GenreId and g.Name = 'Jazz' group by i.CustomerId;"""
query = """select g.Name,t.Milliseconds,COUNT(*) from Genre g,Track t, (select avg(Milliseconds) as av from Track)
where g.GenreId = t.GenreId and t.Milliseconds < av group by t.GenreId order by count(*);"""
cur.execute(query)
data = cur.fetchall()

import pandas as pd
dataf = pd.DataFrame(data)
print dataf