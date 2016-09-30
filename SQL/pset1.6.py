##  Now that we know that our customers love rock music, we can decide which musicians to 
##  invite to play at the concert. 

##  Let's invite the artists who have written the most rock music in our dataset.
##  Write a query that returns the Artist name and total track count of the top 10 rock bands. 


QUERY ='''
SELECT a.Name,COUNT(g.Name) FROM  Genre g,Track t, Album aa,Artist a
WHERE a.ArtistId = aa.ArtistId and aa.AlbumId = t.AlbumId and t.GenreId = g.GenreId and g.name = 'Rock'
group by a.Name
order by COUNT(g.Name) desc limit 10;
'''

'''
---Visual Guide---

Before Query...

#############      #############      #############      ############
#    Genre  #      #   Track   #      #   Album   #      #  Artist  #
#############      #############      #############      ############
|  GenreId  | ---> |  GenreId  |      |  ArtistId  | --->| ArtistId |
+-----------+      +-----------+      +-----------+      +----------+
|  Name     |      |  AlbumId   |---> |  AlbumId  |      |  Name    |
+-----------+      +-----------+      +-----------+      +----------+

After Query...

#######################################
#             GenreArtist             #
#######################################
|  Artist.Name  |  COUNT(Genre.Name)  |
+---------------+---------------------+

'''