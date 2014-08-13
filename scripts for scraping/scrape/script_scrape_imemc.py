import re
import urllib


if __name__=="__main__":

    #url=('http://www.imemc.org/article/68429')
    #string=urllib.urlopen(url).read()


    namedic={}
    dicfile=open('name_gender_correspondence.txt','r')
    for dicline in dicfile:
        temp=dicline.strip().split('\t')
        #print temp[0]
        if len(temp)>1:
            namedic[temp[0]]=temp[1]
        else:
            namedic[temp[0]]=""
    namedic['Maida']="F"

    placedic={}
    placedicfile=open('places_imemc.txt','r')
    for placedicline in placedicfile:
        temp=placedicline.strip().split('\t')
        #print temp[0]
        if len(temp)>1:
            placedic[temp[0]]=temp[1]   


    infile=open('../data_raw_Aug12/raw_imemc.txt','r')
    outfile=open('parsed_imemc.txt','w')
    #outfile2=open('places_imemc.txt','w')    

    outfile.write('Date\tOrdinal_day\tFull_name\tFirst_name\tLast_name\tAge\t'+
                      'Ethnic_group\tSex\tName_summary\tAge_group\tName_unknown\tAge_unknown\tPlace\tCircumstances\n')

    ordinal_day=36              
    unknown_count=0
    ethnic_group="Palestinian"
    firstnamelist=[]
    placelist=[]




    for line in infile:
        #date parsing
        if 'July' in line or 'August' in line:
            day=re.search('(\d+)', line).group(1)
            if float(day)<10:
                day="0"+str(day)
            if ', July' in line:
                date="July "+day
            elif ', August' in line:
                date="August "+day
            ordinal_day-=1   

            
        #description parsing
        elif line.strip()!="":       
            full_name="NA"
            age="NA"
            sex="NA"
            namecode=0
            agecode="0"
            name_unknown_flag="0"
            age_unknown_flag="0"
            circumstances=""
            first_name=""
            last_name=""
            middle_name=""
            place=""


        #full circumstances
            circumstances=line.strip()


        #age        
            if re.search('(\d+)', line)!=None:
                age=re.search('(\d+)', line).group(1)
                if "month" in line:
                    age=(float(re.search('(\d+)', line).group(1))/12)
                   
        #age unknown
            else:
               age_unknown_flag="1"
               agecode="0"


        #age summary            
            if age!="NA":
                if float(age)<=14:
                    agecode="1"
                elif float(age)>14 and float(age)<=24:
                    agecode="2"
                elif float(age)>24 and float(age)<=54:
                    agecode="3"
                elif float(age)>54:
                    agecode="4"
                       

        #name                
            if "unknown" in line or 'Unknown' in line or 'unidentified' in line or "Unidentified" in line:
                full_name="unknown"+str(unknown_count)
                unknown_count+=1
                name_unknown_flag="1"     
            elif (',') in line:
                full_name=line.split(',')[0].strip()
            else:
                full_name=line.strip()
                

        #name summary
            if name_unknown_flag=="0":
                first_name=full_name.split(' ')[0]   
                last_name=full_name.split(' ')[-1]
                if len(full_name.split(' '))>2:
                    middle_name=full_name.split(' ')[1]
                
                if first_name=="Dr.":
                    first_name=middle_name
                if re.search('(\d+)', last_name)!=None:
                    last_name=middle_name
                    #print last_name
                elif re.search ('\((\w+)', last_name)!=None:
                    last_name=middle_name
    
                if first_name.split('-')[0] not in firstnamelist:
                    firstnamelist.append(first_name.split('-')[0])
                if middle_name!="" and middle_name.split('-')[0] not in firstnamelist:
                    firstnamelist.append(middle_name.split('-')[0])
    
                
                last_name_low=last_name.lower()
                if ('-') in last_name_low:
                    last_name_low=last_name_low.split('-')[1]
                if ('\'') in last_name_low:                    
                    last_name_low=('').join(last_name_low.split('\''))
                    
                #print last_name_low                
                namecode=((ord(last_name_low[0])-96)*10+(ord(last_name_low[1])-96))
                namecode=str(namecode)


            #gender
                if '\'' in first_name.split('-')[0]:
                    temp_first_name=('').join((first_name.split('-')[0]).split('\''))
                else:
                    temp_first_name=first_name.split('-')[0]
                #print temp_first_name
                if namedic[temp_first_name]=="M":
                    sex="M"
                elif namedic[temp_first_name]=="F":
                    sex="F"
                elif middle_name!="":
                    temp_middle_name=middle_name.split('-')[0]
                    if '\'' in temp_middle_name:
                        temp_middle_name=('').join(temp_middle_name.split('\''))
                    if namedic[temp_middle_name]=="M":
                        sex="M"
                    elif namedic[temp_middle_name]=="F":
                        sex="F"
                else:
                    sex="NA"

            #place                    
            #if re.search(', ([A-Z]\w+) ([A-Z]\w+)', line)!=None:
                #print(re.search(', ([A-Z]\w+) ([A-Z]\w+)', line).group(1))
                #place=re.search(', ([A-Z]\w+) ([A-Z]\w+)', line).group(1)+" " + re.search(', ([A-Z]\w+) ([A-Z]\w+)', line).group(2)
            #elif re.search(', ([A-Z]\w+)', line)!=None:
                #place=re.search(', ([A-Z]\w+)', line).group(1)
            #if place not in placelist:
                #placelist.append(place)
            for x in placedic.keys():
                if x in line:
                    place=placedic[x]
                    print x
            if place=="" and "Gaza" in line:
                place="Gaza"
                
                
        #print parsed result
            outfile.write(date+'\t'+str(ordinal_day)+'\t'+full_name+'\t'+first_name+'\t'+last_name+'\t'+str(age)+'\t'+ethnic_group+'\t'+sex
                      +'\t'+namecode+'\t'+agecode+'\t'+name_unknown_flag+'\t'+age_unknown_flag+'\t'+place+'\t'+circumstances+'\n')
                
    outfile.close()

    #for x in placelist:
    #    outfile2.write(x+'\n')
    #outfile2.close()
