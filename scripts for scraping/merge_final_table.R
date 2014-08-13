
#########creating the combined table

library(plyr)

combined2 <- read.delim("./Aug12/combined/combined_imemc_akhbar_corrected.txt")
parsed_imemc2 <- read.delim("./Aug12/parsed/parsed_imemc_corrected.txt")
parsed_toi <- read.delim("./Aug12/parsed/parsed_toisrael_corrected.txt")

comb <- merge(combined2[,c(1:9, 13:18)], parsed_imemc2[, c(3, 8, 9)], by.x="IMEMC_name", by.y="Full_name", all.x=TRUE)
comb <- comb[-which(!(parsed_imemc2$Full_name %in% combined2$IMEMC_name)), ]
row.names(comb) <- NULL
comb <- comb[, c(2: 11, 1, 13:14, 16:17, 12, 15)]

colnames(comb) <- c("Date", "Ordinal_day", "Full_name", "First_name", "Last_name", "Age", "Ethnic_group", "Sex", "Name_summary", "Place", "IMEMC_name", "IMEMC_age", "IMEMC_place", "IMEMC_sex", "IMEMC_name_summary", "Circumstances", "IMEMC_circumstances")
comb <- arrange(comb, Ordinal_day, Last_name, First_name)

comb <- rbind(comb, parsed_toi)

########creating some additional flags, groups etc.
comb$IMEMC_name[comb$IMEMC_name==""] <- NA
comb$IMEMC_age[comb$IMEMC_age==""] <- NA
comb$IMEMC_sex[comb$IMEMC_sex==""] <- NA
comb$IMEMC_place[comb$IMEMC_place==""] <- NA
comb$IMEMC_name_summary[comb$IMEMC_name_summary==""] <- NA

comb$Comb_age <- ifelse(!is.na(comb$IMEMC_age), comb$IMEMC_age, comb$Age)
comb$Comb_sex <- ifelse(!is.na(as.character(comb$IMEMC_sex)), as.character(comb$IMEMC_sex), as.character(comb$Sex))
comb$Comb_place <- ifelse(!is.na(as.character(comb$IMEMC_place)), as.character(comb$IMEMC_place), as.character(comb$Place))
comb$Comb_name_summary <- ifelse(!is.na(comb$IMEMC_name_summary) & comb$IMEMC_name_summary<1000, comb$IMEMC_name_summary, comb$Name_summary)


comb$Age_group <- ifelse(is.na(comb$IMEMC_age)&(is.na(comb$Age)), "Unknown", "NA")
for (x in 1:length(comb$Age_group)){
  if (!is.na(comb$Comb_age[x])& comb$Comb_age[x] <= 14) {comb$Age_group[x]="Child"}
  else if (!is.na(comb$Comb_age[x]) & comb$Comb_age[x] <= 24) {comb$Age_group[x]="Young adult"}
  else if (!is.na(comb$Comb_age[x]) & comb$Comb_age[x] <= 54) {comb$Age_group[x]="Adult"}
  else if (!is.na(comb$Comb_age[x])) {comb$Age_group[x]="Elderly"}
}

comb$Comb_sex <- as.factor(comb$Comb_sex)
comb$Comb_place <- as.factor(comb$Comb_place)
comb$Age_group <- as.factor(comb$Age_group)
comb$Age_group <- factor(comb$Age_group, levels=c("Unknown", "Child", "Young adult", "Adult", "Elderly"))

########simulating names and ages
median_name<-median(log(comb$Comb_name_summary[!is.na(comb$Comb_name_summary)]), na.rm=TRUE)
sd_name<-quantile(log(comb$Comb_name_summary[!is.na(comb$Comb_name_summary)]), 0.75, na.rm=TRUE)-quantile(log(comb$Comb_name_summary[!is.na(comb$Comb_name_summary)]), 0.25, na.rm=TRUE)
vec<-(rnorm(length(comb$Comb_name_summary), mean=median_name, sd=0.75*sd_name))
comb$Sim_name_summary<-ifelse(is.na(comb$Comb_name_summary), vec, log(comb$Comb_name_summary))+rnorm(length(comb$Comb_name_summary), 0, 0.33)

median_Comb_age=median(comb$Comb_age, na.rm=TRUE)
sd_Comb_age=median(comb$Comb_age, na.rm=TRUE)-quantile(comb$Comb_age, 0.25, na.rm=TRUE)
vec<-round(abs(rnorm(length(comb$Comb_age), mean=median_Comb_age, sd=2*sd_Comb_age)))
comb$Sim_age<-abs(ifelse(is.na(comb$Comb_age), vec, comb$Comb_age)+rnorm(length(comb$Comb_age), 0, 0.33))


#######writing out the final table
write.csv(comb, "./final.txt", row.names=FALSE)