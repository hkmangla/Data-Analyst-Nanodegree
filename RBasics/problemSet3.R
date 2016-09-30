library(ggplot2)
#problem 1
ggplot(aes(x = log(price)), data = diamonds) +
  geom_histogram(aes(fill = cut)) +
  facet_wrap(~color) + scale_fill_brewer(type = 'qual')

#problem 2
ggplot(aes(x = table, y = price), data = subset(diamonds, table <75 & table >45)) +
  geom_point(aes(color = cut)) + scale_fill_brewer(type = 'qual') +
  scale_x_continuous(breaks = seq(50,75,2))

#problem 4
diamonds$volume <- with(diamonds, x*y*z)
ggplot(aes(y = log10(price),x = volume), data = subset(diamonds, volume <= 800)) +
  geom_point(aes(color = clarity)) + scale_color_brewer(type = 'div')

#problem 5
pf$prop_initiated = pf$friendships_initiated/pf$friend_count
table(pf$prop_initiated)

#problem 6

ggplot(aes(x = 50*round(tenure/50), y = prop_initiated), data = pf) +
  geom_line(aes(color = year_joined.bucket), stat = 'summary', fun.y = median)

#problem 9
with(subset(pf, !is.nan(prop_initiated)), by(prop_initiated, year_joined.bucket, summary) )


#problem 10

ggplot(aes(y = price/carat, x= cut), data = diamonds) +
  geom_jitter(aes(color = color)) +
  facet_wrap(~clarity) +
  scale_color_brewer(type = 'div')
