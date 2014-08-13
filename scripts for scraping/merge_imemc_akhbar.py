infile1=open('./data_parsed_Aug12/parsed_akhbar.txt','r')
infile2=open('./data_parsed_Aug12/parsed_imemc.txt','r')

outfile1=open('stage2_common.txt','w')
outfile2=open('stage2_rem.txt','w')


dic1={}
dic2={}

outfile1.write('Date\tOrdinal_day\tFull_name\tFirst_name\tLast_name\tAge\t'+
                      'Ethnic_group\tSex\tName_summary\tAge_group\tName_unknown\tAge_unknown\tPlace\tCircumstances\tIMEMC_name\tIMEMC_age\tIMEMC_place\tIMEMC_circumstances\n')

for line in infile1:
    list=line.strip().split('\t')
    dic1[list[2]]=list

for line in infile2:
    list=line.strip().split('\t')
    dic2[list[2]]=list

for x in dic1.keys():
    name1=dic1[x][4]
    if 'al-' in dic1[x][4]:
        name1=name1.split('-')[1]
    dic1[x].append(name1)
        
for y in dic2.keys():
    name2=dic2[y][4]
    if 'al-' in dic2[y][4]:
        name2=name2.split('-')[1]
    dic2[y].append(name2)

finaldic={}
i=0
print len(dic1)

####zero pass
for x in dic1.keys():
    if 'unknown' in x:
        finaldic[x]=dic1[x][0:13]
        finaldic[x].append("")
        finaldic[x].append("")
        finaldic[x].append("")
        finaldic[x].append("")
        del(dic1[x])
        i+=1
print i


####first pass
flagx={}
for x in dic1.keys():
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
            if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7] and dic2[y][5]==dic1[x][5] and dic1[x][12]==dic2[y][12] and dic1[x][2]==dic2[y][2]:
                finaldic[x]=dic1[x][0:14]
                finaldic[x].append(dic2[y][2])
                finaldic[x].append(dic2[y][5])
                finaldic[x].append(dic2[y][12])
                finaldic[x].append(dic2[y][13])
                #print x, y
                flagx[x]=y

for x in dic1.keys():
    if flagx[x]!=0:
        #print x, flagx[x]
        del(dic1[x])
        del(dic2[flagx[x]])
        i+=1
print i


####second pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
            if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7] and dic1[x][5]==dic2[y][5] and dic1[x][5]!="NA" and dic1[x][12]==dic2[y][12] \
                                                             and dic1[x][3][0:2]==dic2[y][3][0:2] and dic1[x][14][0:3]==dic2[y][14][0:3]:
                finaldic[x]=dic1[x][0:14]
                finaldic[x].append(dic2[y][2])
                finaldic[x].append(dic2[y][5])
                finaldic[x].append(dic2[y][12])
                finaldic[x].append(dic2[y][13])
                #print x, y
                flagx[x]=y        

for x in dic1.keys():
    if flagx[x]!=0:
        #print x, flagx[x]
        del(dic1[x])
        del(dic2[flagx[x]])        
        i+=1
print i


####third pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
            if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7] and dic1[x][5]==dic2[y][5] and dic1[x][5]!="NA" \
            and dic1[x][12]==dic2[y][12] and dic1[x][3][0:2]==dic2[y][3][0:2] and dic1[x][14][0:2]==dic2[y][14][0:2]:
                finaldic[x]=dic1[x][0:14]
                finaldic[x].append(dic2[y][2])
                finaldic[x].append(dic2[y][5])
                finaldic[x].append(dic2[y][12])
                finaldic[x].append(dic2[y][13])
                #print x, y
                flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        #print x, flagx[x]
        del(dic1[x])
        del(dic2[flagx[x]])        
        i+=1
print i


####fourth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7] and dic1[x][5]==dic2[y][5] \
                and dic1[x][12]==dic2[y][12] and dic1[x][3][0:2]==dic2[y][3][0:2] and dic1[x][14][0:2]==dic2[y][14][0:2]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
#print i


####fifth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7] and dic1[x][5]==dic2[y][5] \
                and dic1[x][12]==dic2[y][12] and dic1[x][3][0:1]==dic2[y][3][0:1] and dic1[x][14][0:1]==dic2[y][14][0:1]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
#print i



####sixth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7]  \
                and dic1[x][12]==dic2[y][12] and dic1[x][3][0:4]==dic2[y][3][0:4] and dic1[x][14]==dic2[y][14]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i



####seventh pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7]  \
                and dic1[x][12]==dic2[y][12] and dic1[x][3][0:2]==dic2[y][3][0:2] and dic1[x][14][0:2]==dic2[y][14][0:2]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i


####eighth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7]  \
                and dic1[x][3][0:4]==dic2[y][3][0:4] and dic1[x][14][0:4]==dic2[y][14][0:4]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr', 'Mohammad Ahmad Abu Amer']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i


####ninth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7]  \
                and dic1[x][3][0:3]==dic2[y][3][0:3] and dic1[x][14][0:3]==dic2[y][14][0:3]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr', 'Mohammad Ahmad Abu Amer']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i


####tenth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7]  \
                and dic1[x][3][0:2]==dic2[y][3][0:2] and dic1[x][14][0:2]==dic2[y][14][0:2]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr', 'Mohammad Ahmad Abu Amer', 'Mohammad Ziad Zabout']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i


####eleventh pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][0]==dic2[y][0] and dic1[x][7]==dic2[y][7]  \
                and dic1[x][3][0:1]==dic2[y][3][0:1] and dic1[x][14][0:2]==dic2[y][14][0:2]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr', 'Mohammad Ahmad Abu Amer', 'Mohammad Ziad Zabout', 'Mona Hajjaj Abu Amer', 'Qusai Issam al-Batsh', \
                            "Ahmed Abu Jm'ean Hji'er 19"]:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i


####twelfth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][3][0:4]==dic2[y][3][0:4] and dic1[x][14][0:4]==dic2[y][14][0:4]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr', 'Mohammad Ahmad Abu Amer', 'Mohammad Ziad Zabout', 'Mona Hajjaj Abu Amer', 'Qusai Issam al-Batsh', \
                            "Ahmed Abu Jm'ean Hji'er 19", 'Mohammed Ahmad Abu Amer']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i



####thirteenth pass
flagx={}
for x in dic1.keys():
    #print x
    flagx[x]=0
    for y in dic2.keys():
        if flagx[x]==0:
                if dic1[x][3][0:3]==dic2[y][3][0:3] and dic1[x][14][0:3]==dic2[y][14][0:3]:
                    finaldic[x]=dic1[x][0:14]
                    finaldic[x].append(dic2[y][2])
                    finaldic[x].append(dic2[y][5])
                    finaldic[x].append(dic2[y][12])
                    finaldic[x].append(dic2[y][13])
                    #print x, y
                    flagx[x]=y        


for x in dic1.keys():
    if flagx[x]!=0:
        if flagx[x] not in ['Mohammad Ahmad Najjar', 'Mahmoud Mohammad Abu Haddaf', 'Mohammad Ismael al-Ghoul', 'Ismael Mohammad al-Ghoul', \
                            'Aya Yassr al-Qisas', 'Abdul-Karim Najm', "Mohammad Mosa'ed Qishta'", 'Salah Hejazi', 'Mustafa Wael al-Ghoul', 'Mohammad Edrees Abu Sneina',\
                            'Anas Yousef Moammar', 'Mohammed Farhan Abu Jazr', 'Mohammad Ahmad Abu Amer', 'Mohammad Ziad Zabout', 'Mona Hajjaj Abu Amer', 'Qusai Issam al-Batsh', \
                            "Ahmed Abu Jm'ean Hji'er 19", 'Mohammed Ahmad Abu Amer', "Mohammad Fayez Sha'ban al-Sharif", 'Abdullah Soheil Abu Shawish']:
            #print x, flagx[x]
            del(dic1[x])
            del(dic2[flagx[x]])        
            i+=1
print i






for x in finaldic.keys():          
    string=('\t').join(finaldic[x])+'\n'
    outfile1.write(string)


for x in dic1.keys():          
    string=('\t').join(dic1[x])+'\n'
    outfile2.write(string)

for y in dic2.keys():
    string=('\t').join(dic2[y])+'\n'
    #outfile2.write(string)


outfile1.close()
outfile2.close()
