import re
import urllib2, cookielib

if __name__=="__main__":
    ####get the file
    #url=('http://english.al-akhbar.com/node/20528')
    #hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #   'Accept-Encoding': 'none',
    #   'Accept-Language': 'en-US,en;q=0.8',
    #   'Connection': 'keep-alive'}
    
    #string=urllib2.urlopen(urllib2.Request(url, headers=hdr)).read() 
    #string=string.split('will update the list as new information is released.</p>')[1].split('<p><i>(Al-Akhbar)</i></p>')[0]
    #list=string.split('>')

    ####create the name-gender dictionary
    namedic={}
    dicfile=open('name_gender_correspondence.txt','r')
    for dicline in dicfile:
        temp=dicline.strip().split('\t')
        #print temp[0]
        if len(temp)>1:
            namedic[temp[0]]=temp[1]
        else:
            namedic[temp[0]]=""

    placedic={}
    placedicfile=open('places_akhbar.txt','r')
    for placedicline in placedicfile:
        temp=placedicline.strip().split('\t')
        #print temp[0]
        if len(temp)>1:
            placedic[temp[0]]=temp[1]
    
    infile=open('../data_raw_Aug12/raw_alakhbar.txt','r')

    ####set up the structure of the outfile
    outfile=open('parsed_akhbar.txt','w')
    #outfile2=open('places_akhbar.txt','w')
    
    outfile.write('Date\tOrdinal_day\tFull_name\tFirst_name\tLast_name\tAge\t'+
                      'Ethnic_group\tSex\tName_summary\tAge_group\tName_unknown\tAge_unknown\tPlace\tCircumstances\n')
    prevline=""
    ordinal_day=0              
    unknown_count=0
    ethnic_group="Palestinian"
    firstnamelist=[]
    placelist=[]
    prevplace=""


    ####parse the lines containing dates
    for line in infile:
        #date parsing
        if ', July' in line or ', August' in line:
            day=re.search('(\d+)', line).group(1)
            if float(day)<10:
                day="0"+str(day)
            if ', July' in line:
                date="July "+day
            elif ', August' in line:
                date="August "+day
            ordinal_day+=1   


    ####parse the lines containing names        
        #description parsing
        elif re.search('(\d+)', line)!=None:
            line=line.split('<')[0]
            line=line.decode("utf-8").replace(u"\u2019", "\'").encode("utf-8")
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

            line=re.search('(\d+)\. ?(.+)', line).group(2) #stripping the ordinal


        #full circumstances
            if "same" not in line:
                prevline=line.strip()
                circumstances=prevline
            else:
                circumstances=prevline+" "+line.strip()
                place=prevplace


        #age        
            if re.search('(\d+)', line)!=None:
                age=re.search('(\d+)', line).group(1)
                if "month" in line:
                    age=(float(re.search('(\d+)', line).group(1))/12)

                    
        #age unknown
            else:
               age_unknown_flag="1"
               agecode="0"


        #old age summary            
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
            elif re.search('(.+), (\d+)', line)!=None:
                full_name=(re.search('(.+), (\d+)', line).group(1))
            elif re.search('(.+) was killed', line)!=None:
                full_name=re.search('(.+) was killed', line).group(1).split(',')[0]
            elif re.search('(.+) succumbed', line)!=None:
                full_name=re.search('(.+) succumbed', line).group(1).split(',')[0]
            elif re.search('(.+) was found', line)!=None:
                full_name=re.search('(.+) was found', line).group(1).split(',')[0]
            else:
                full_name=line.split(',')[0].strip()
                print(line)


        #name summary
            if name_unknown_flag=="0":
                #print name
                first_name=full_name.split(' ')[0]   
                last_name=full_name.split(' ')[-1]
                if len(full_name.split(' '))>2:
                    middle_name=full_name.split(' ')[1]

                if first_name not in firstnamelist:
                    firstnamelist.append(first_name)
                if middle_name!="" and middle_name not in firstnamelist:
                    firstnamelist.append(middle_name)
                
                last_name_low=last_name.lower()
                if ('-') in last_name_low:
                    last_name_low=last_name_low.split('-')[1]
                if ('\'') in last_name_low:
                    print last_name_low
                    last_name_low=('').join(last_name_low.split('\''))
                
                namecode=((ord(last_name_low[0])-96)*10+(ord(last_name_low[1])-96))
                namecode=str(namecode)


            #finally, gender!
                #print first_name
                if '\'' in first_name.split('-')[0]:
                    temp_first_name=('').join((first_name.split('-')[0]).split('\''))
                else:
                    temp_first_name=first_name.split('-')[0]
                #print temp_first_name
                if len(temp_first_name)>1:
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
                #if re.search(' in (.+)', line)!=None:
                #    if re.search(' in (.+)', line).group(1) not in placelist:
                #        placelist.append(re.search('in (.+)', line).group(1))
                for x in placedic.keys():
                    if x in line:
                        place=placedic[x]
                if place=="" and "Gaza City" in line:
                    place="Gaza City"
                if place=="" and "Gaza" in line:
                    place="Gaza"                    
                prevplace=place
                
                
        ####print parsed result
            outfile.write(str(date)+'\t'+str(ordinal_day)+'\t'+full_name+'\t'+first_name+'\t'+last_name+'\t'+str(age)+'\t'+ethnic_group+'\t'+sex
                      +'\t'+str(namecode)+'\t'+str(agecode)+'\t'+name_unknown_flag+'\t'+age_unknown_flag+'\t'+place+'\t'+circumstances+'\n')             
    outfile.close()

    #for x in placelist:
    #    outfile2.write(x+'\n')
    #outfile2.close()
