data("diamonds")
?diamonds
names(diamonds)
dim(diamonds)
is.ordered(diamonds$x)
library(ggplot2)
qplot(data = diamonds, x = price)+
  facet_wrap(~cut,scales = "free_y")
ggsave('firstPlot.jpg')
summary(diamonds$price)
sum(diamonds$price >= 15000)
by(diamonds$price, diamonds$cut, min)
# Price Per carat
qplot(data = diamonds, x = price/carat) +
  scale_x_log10()+
  facet_wrap(~cut)

#Box Plot of price by
#cut
qplot(data = diamonds, x = cut, y = price, geom = "boxplot") +
  coord_cartesian(ylim = c(0,7000))
  ggsave("1.png")
by(diamonds$price, diamonds$cut, summary)
#color
qplot(data = diamonds, x = color, y = price, geom = "boxplot")+
  coord_cartesian(ylim = c(0,8000))
ggsave("2.png")
by(diamonds$price, diamonds$color, summary)
#clarity
qplot(data = diamonds, x = clarity, y = price, geom = "boxplot")+
  coord_cartesian(ylim = c(0,8000))
ggsave("3.png")
by(diamonds$price, diamonds$clarity, summary)

qplot(data = diamonds, x = color, y = price/carat, geom = "boxplot")+
  coord_cartesian(ylim = c(0,6000))
 ggsave("4.png")
 
 qplot(data = diamonds, x = carat, geom = "freqpoly", binwidth = 0.01) +
   scale_x_continuous(lim = c(0,2.5), breaks = seq(0,2.5,0.1))
 
 gapminderData <- read.csv('gapminder.csv', header = T, row.names = 1, check.names = F)
tgapmiderData <- t(gapminderData)
gapminderData <- data.frame(tgapmiderData)
p1 <- qplot(data = gapminderData, x = row.names(gapminderData), y = Norway)
p2 <- qplot(data = gapminderData, x = row.names(gapminderData), y = United.States)
library(gridExtra)
grid.arrange(p1,p2)
qplot(data = gapminderData, x = row.names(gapminderData), color = colnames(gapminderData))