import urllib
import re


infile=open('firstnames_temp.txt','r')
outfile=open('fname_gender_correlation2.txt','w')

for line in infile:
    if 'Masculine'  in line or 'Feminine'  in line:
        outfile.write(line)
    else:
        list=line.strip().split('\t')
        url=('http://www.gpeters.com/names/baby-names.php?name=')+list[0]
        result=urllib.urlopen(url).read()
        if 'It\'s a boy' in result:
             temp='Masculine'
        elif 'It\'s a girl' in result:
             temp='Feminine'
        else:
             temp=""
        print list[0], temp                
        outfile.write(list[0]+'\t'+temp+'\n')
        



#for line in infile:
#    url='http://www.indiachildnames.com/genderof.aspx?name='+line.strip()
#    result=urllib.urlopen(url).read()
#    m=re.search('"font-size: 9pt">Name <b>(.+)</b> is a <font color=(.+)>(\w+) ', result)
#    if re.search('"font-size: 9pt">Name <b>(.+)</b> is a <font color=(.+)>(\w+) ', result)!=None:
#        outfile.write(line.strip()+'\t'+m.group(3)+'\n')
#        #print line.strip(), m.group(3) 
#    else:
#        outfile.write(line.strip()+'\t'+''+'\n')
#        #print line.strip()'''
    
infile.close()
outfile.close()
