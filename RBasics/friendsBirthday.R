birthdayData <- read.csv('friendBirthday.csv')
birthdayData$Start.date <- as.character(birthdayData$Start.date)
birthdayData$Start.date
birthdayData$Start.date <- as.Date(birthdayData$Start.date, format ="%m/%d")
birthdayData$Day <- as.numeric(format(birthdayData$Start.date, "%d"))
birthdayData$Month <- format(birthdayData$Start.date, "%B")
birthdayData$Month <- factor(birthdayData$Month, levels = c("January","February","March","April","May","June","July","August","September","October","November","December"))
library(ggplot2)
qplot(data = birthdayData, x = Day, xlab = "Days of Month ", ylab = "Number of friends") +
  scale_x_continuous(breaks = seq(1,31,1))+
  facet_wrap(~Month,ncol =2)
ggsave("5.png", width = 12, height = 6)
by(birthdayData$Day,birthdayData$Month,  length)
subset(birthdayData,birthdayData$Day == 9 & birthdayData$Month == "March")
max(by(birthdayData$Day,birthdayData$Month,  length))
min(by(birthdayData$Month,birthdayData$Day,  length))
