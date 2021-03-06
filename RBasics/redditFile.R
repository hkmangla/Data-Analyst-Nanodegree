reddit <- read.csv('reddit.csv')
str(reddit)
summary(reddit)
table(reddit$employment.status)
table(reddit$age.range)
levels(reddit$age.range)
library(ggplot2)
levels(reddit$income.range)
reddit$age.range <- ordered(reddit$age.range, levels = c("Under 18", "18-24", "25-34", "35-44","45-54", "55-64", "65 or Above"))
reddit$income.range <- ordered(reddit$income.range, levels = c("Under $20,000", "$20,000 - $29,999" , "$30,000 - $39,999",  "$40,000 - $49,999", "$50,000 - $69,999","$70,000 - $99,999", "$100,000 - $149,999" ,"$150,000 or more"))
qplot(data = reddit, x = income.range )
