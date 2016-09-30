?diamonds
names(diamonds)
library(ggplot2)
#problem 1
ggplot(aes(x = x, y = price), data = diamonds) + geom_point()
#problem 2
cor(diamonds$price, diamonds$x)
cor(diamonds$price, diamonds$y)
cor(diamonds$price, diamonds$z)
#problem 3
ggplot(aes(x = depth, y = price), data = diamonds) + geom_point(alpha = 1/100)+
  scale_x_continuous(breaks= seq(50,70,2))
cor(diamonds$depth, diamonds$price)
#problem 8
ggplot(aes(x = carat, y = price), data = diamonds) + geom_point()
#problem 9
diamonds$volume = diamonds$x*diamonds$y*diamonds$z
names(diamonds)
ggplot(aes(x = volume, y = price), data = diamonds) + geom_point(alpha = 1/20) +
  scale_x_continuous(breaks = seq(0,1000,100), limits = c(0,1000))
library(plyr)
count(diamonds$volume == 0)
#problem 11
with(subset(diamonds, diamonds$volume != 0 & diamonds$volume < 800), cor.test(price, volume))

#problem 12
ggplot(aes(x = volume, y = price), data = subset(diamonds, diamonds$volume != 0 & diamonds$volume < 800)) +
   geom_point(alpha = 1/20 ) +
  geom_smooth(method = 'lm' , color = 'red')

#problem 13
diamondsByClarity <- diamonds %>%
  group_by(clarity) %>%
  summarise(mean_price = mean(price),
            median_price = median(price),
            min_price = min(price),
            max_price = max(price),
            n = n()
            ) %>%
  arrange(clarity)
diamondsByClarity

#problem 14

diamonds_by_clarity <- group_by(diamonds, clarity)
diamonds_mp_by_clarity <- summarise(diamonds_by_clarity, mean_price = mean(price))

diamonds_by_color <- group_by(diamonds, color)
diamonds_mp_by_color <- summarise(diamonds_by_color, mean_price = mean(price))
p1 <- ggplot(aes(x = clarity, y = mean_price), data = diamonds_mp_by_clarity) + geom_bar(stat = 'identity')
p2 <- ggplot(aes(x = color, y = mean_price), data = diamonds_mp_by_color) + geom_bar(stat = 'identity')
grid.arrange(p1,p2,ncol = 1)

unemployement <- read.csv('gapminder2.csv', header = T, row.names = 1, check.names = F)
unemployement <- t(unemployement)
unemployement <- as.data.frame(unemployement)
names(unemployement)

p1 <- ggplot(aes(x = row.names(subset(unemployement, !is.na(unemployement$Australia))), y =Australia),
       data = subset(unemployement, !is.na(unemployement$Australia))) + geom_bar(stat = 'identity') +
  xlab("Unemployement Rate in b/w 15-24 age")
p2 <- ggplot(aes(x = row.names(subset(unemployement, !is.na(unemployement$Poland))), y =Poland),
       data = subset(unemployement, !is.na(unemployement$Poland))) + geom_bar(stat = 'identity') +
  xlab("Unemployement Rate in b/w 15-24 age")
grid.arrange(p1,p2,ncol = 1)