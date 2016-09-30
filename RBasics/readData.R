getwd() #Give current working directory
setwd('~/MyDrive/Programming/Nanodegree/Data_analysis/RBasics')
#getwd()
stateInfo <- read.csv('stateData.csv')

stateSubset <- subset(stateInfo, state.region == 1)
head(stateSubset, 2)
dim(stateSubset)
stateSubsetBracket <- stateInfo[stateInfo$state.region == 1, ]

head(stateSubsetBracket, 2)
dim(stateSubsetBracket)
stateIlliteracy <- stateInfo[stateInfo$illiteracy <= 0.5, ]
stateIlliteracy
