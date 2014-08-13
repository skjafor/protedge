import re
import urllib


if __name__=='__main__':
    #url=('http://www.timesofisrael.com/fallen-idf-soldiers-in-operation-protective-edge/')
    #f = urllib.urlopen(url)
    
    
    infile=open('../data_raw_Aug12/raw_toi.txt','r')
    outfile=open('parsed_israel.txt','w')
    outfile.write('Date\tOrdinal_day\tFull_name\tFirst_name\tLast_name\tAge\tEthnic_group\tSex\tName_summary\tAge_group\tName_unknown\tAge_unknown\tPlace\tCircumstances\n')

    string=""

    for line in infile:
        string+=line
    list=string.split('\n*')[1:]

    ethnic_group="Israeli"
    sex="M"
    name_unknown_flag="0"
    age_unknown_flag="0"
    circumstances=""
    first_name=""
    place=""

    for x in list:
        print x
        m1=re.search('(.+)\*, (\d+)(,| years)', x)
        m2=re.search('(July|August) (\d+)', x)


        #date
        date=m2.group(1)+' '+m2.group(2)

        #ordinal_day
        ordinal_day=int(m2.group(2))-7
        if m2.group(1)=="August":
            ordinal_day=ordinal_day+31
        ordinal_day=str(ordinal_day)

        #full name
        full_name=m1.group(1)
        last_name=m1.group(1).split(' ')[-1]
        if '(' in last_name:
            last_name=m1.group(1).split(' ')[-2]
     
        age=m1.group(2)

        #name summary
        last_name_low=last_name.lower()
        namecode=str((ord(last_name_low[0])-96)*10+(ord(last_name_low[1])-96))        

        #age group
        if int(age)<=14:
            agecode="1"
        elif int(age)>14 and int(age)<=24:
            agecode="2"
        elif int(age)>24 and int(age)<=54:
            agecode="3"
        elif int(age)>54:
            agecode="4"
        
        outfile.write(date+'\t'+ordinal_day+'\t'+full_name+'\t'+first_name+'\t'+last_name+'\t'+age+'\t'+ethnic_group+'\t'+sex
                      +'\t'+namecode+'\t'+agecode+'\t'+name_unknown_flag+'\t'+age_unknown_flag+'\t'+place+'\t'+circumstances+'\n')
       
            
    outfile.close()    
