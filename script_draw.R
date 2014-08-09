ds <- read.csv("combined_akhbar_israel.txt", sep="\t")

library(lubridate)
class(ds$date<-as.Date(ds$date, format="%b %d"))

##############simulating day, name, age, for programs where jitter is not available
ds$sim_day<-ds$ordinal_day+8+rnorm(length(ds$ordinal_day), 0, 0.33)

median_name<-median(log(ds$name_summary[ds$name_unknown==0]), na.rm=TRUE)
sd_name<-quantile(log(ds$name_summary[ds$name_unknown==0]), 0.75, na.rm=TRUE)-quantile(log(ds$name_summary[ds$name_unknown==0]), 0.25, na.rm=TRUE)
vec<-(rnorm(length(ds$name_summary), mean=median_name, sd=0.75*sd_name))
ds$sim_name<-ifelse(ds$name_unknown==1, vec, log(ds$name_summary))+rnorm(length(ds$age), 0, 0.33)

median_age=median(ds$age, na.rm=TRUE)
sd_age=median(ds$age, na.rm=TRUE)-quantile(ds$age, 0.25, na.rm=TRUE)
vec<-round(abs(rnorm(length(ds$age), mean=median_age, sd=2*sd_age)))
ds$sim_age<-abs(ifelse(is.na(ds$age), vec, ds$age)+rnorm(length(ds$age), 0, 0.33))


##############create combined factor variables for plotting, for the colour and size
ds$plot_colour<-ifelse(ds$name_unknown|is.na(ds$sex), "Name unknown", NA)
sexmap<-c("Female","Male")
ds$sex<-sexmap[as.factor(ds$sex)]
ds$plot_colour<-ifelse(is.na(ds$plot_colour), ds$sex, ds$plot_colour)
ds$plot_colour<-ifelse(ds$ethnic_group=="Israeli", "Israeli soldier", ds$plot_colour)
ds$plot_colour<-as.factor(ds$plot_colour)
ds$plot_colour<-factor(ds$plot_colour, levels=c("Name unknown", "Female", "Male", "Israeli soldier"))

agemap<-c("Age unknown", "Child <=14yo", "Adult", "Adult", "Adult")
ds$age_summary2<-factor(as.factor(agemap[as.factor(ds$age_group)]), levels=c("Age unknown", "Child <=14yo", "Adult"))



##############finally, the plot
library(ggplot2)
palette<-c("grey", "black", "dark red", "light blue")

sizemap<-c(2, 3, 2)
ds$size<-sizemap[ds$age_summary2]

#ggplot(ds,aes(x=date, y=sim_age, color=plot_colour, size=size, label=full_name))+geom_text(position=position_jitter(w=0.45, h=0.05), size=2.5)+scale_size_area()+theme_bw()+theme(axis.title.y=element_blank(), legend.position="none")+xlab("Timeline")+scale_colour_manual(values=palette, name="age group")
#ggplot(ds,aes(x=date, y=sim_name, color=plot_colour, size=size, label=full_name))+geom_point(position=position_jitter(w=0.45, h=0.05), alpha=7/10)+scale_size_area()+theme_bw()+theme(axis.title.y=element_blank(), axis.text.y=element_blank(), legend.position="none")+xlab("Timeline")+scale_colour_manual(values=palette, name="age group")
ggplot(ds,aes(x=date, y=sim_age, color=plot_colour, size=size, label=full_name))+geom_point(position=position_jitter(w=0.45, h=0.05), alpha=7/10)+geom_text(position=position_jitter(w=0.45, h=0.05), size=1)+scale_size_area()+theme_bw()+theme(legend.position="none")+xlab("Timeline")+ylab("Age of victim")+scale_colour_manual(values=palette, name="Age group")

ggplot(ds[ds$ethnic_group!="Israeli",],aes(x=date, y=sim_age, color=plot_colour, size=size, label=full_name))+geom_point(position=position_jitter(w=0.45, h=0.05), alpha=7/10)+geom_text(position=position_jitter(w=0.45, h=0.05), size=1)+scale_size_area()+theme_bw()+theme(legend.position="none")+xlab("Timeline")+ylab("Age of victim")+scale_colour_manual(values=palette, name="Age group")





##############some other plots
library(ggplot2)
ds$date2<-as.factor(format(ds$date, "%m/%d"))
p1<-ggplot(ds[ds$ethnic_group!="Israeli",],aes(x=date2, y=age))
p1<-p1+geom_boxplot(notch=FALSE, fill="grey")
p1<-p1 + theme(legend.position="none")+theme_bw()+xlab("Timeline")+ylab("Age of victim")
p1


library(hexbin)
p2<-ggplot(ds[ds$ethnic_group!="Israeli",],aes(x=date2, y=age, group=1))
p2<-p2+geom_hex(binwidth=c(1, 5))
p2<-p2+geom_smooth(color="white", se=F)
p2<-p2+theme_bw()+scale_fill_continuous(low = "#CCCCCC", high = "#FF0000")
p2<-p2+xlab("Timeline")+ylab("Age of victim")
p2


#####one more combined factor
library(plyr)
library(dplyr)
agemap<-c("Age unknown", "Child <=14yo", "Adult")
ds$plot_colour2<-ifelse(ds$ethnic_group=="Israeli", "Israeli soldier", agemap[as.factor(ds$age_summary2)])
ds$plot_colour2<-factor(as.factor(ds$plot_colour2), levels=c("Age unknown", "Child <=14yo", "Adult", "Israeli soldier"))

dss<-ds%>%filter(plot_colour2 %in% levels(ds$plot_colour2)) %>%
  group_by(plot_colour2) %>%
  mutate(cumDeaths=order_by(date, cumsum(!is.na(full_name))))


palette=c("dark grey", "green", "red", "blue")
p3 <- ggplot(dss, aes(x=date, y=cumDeaths, colour=plot_colour2))
p3 <- p3 + geom_smooth()
p3 <- p3 + xlab("Timeline")+ylab("Deaths (cumulative)")+ scale_y_continuous()+ ggtitle("Deaths in Operation Protective Edge")
p3 <- p3 + scale_colour_manual(values=palette, name="Group")
p3 <- p3 + theme_bw()+theme(legend.key = element_rect(fill = "white"))
p3



