


getwd()

setwd('/Users/stephanehess/Documents/CAS_AML/docker_neuro_rehab_project/Jupyter/Data')
list.files()

data_wb_analysis <- read.csv("data_wb_analysis.csv")
head(data_wb_analysis)

wilcox.test(data_wb_analysis$T2_1, data_wb_analysis$T2_0, paired=TRUE, alternative = 'greater')
wilcox.test(data_wb_analysis$T3_1, data_wb_analysis$T3_0, paired=TRUE, alternative = 'greater')
wilcox.test(data_wb_analysis$morning_tot, data_wb_analysis$afternoon_tot, paired=TRUE, alternative = 'greater')

x <- c(4, 9, 5, 11, 4, 4, 3, 2, 4, 5, 3)
x <- c(4, 9, 5, 11, 40, 4, 3, 200000000000, 4, 5, 30000)
y <- c(1, 3, 5, 7, 3, 1, 3, 1, 5, 4, 1)
wilcox.test(x, y, paired = TRUE, alternative = "greater")
wilcox.test(y - x, alternative = "less")    # The same.

y - x
