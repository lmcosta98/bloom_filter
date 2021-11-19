#!/usr/bin/env python
# coding: utf-8

# In[60]:


import random
import csv

#Generate random number with n digits
def numb_(n):
    str_=''
    for i in range(n):
        str_+=str(random.randint(0,9))
    return str_
    
#First digit
init_dig=['1','2','3','5','6','8','45','70','71','72','74','75','77','78','79','90','91','98','99']

#Generate n invalid NIFs
def generate_nifs(n):
    f=open("data_nifs.csv","a",newline='')
    writer=csv.writer(f,delimiter=' ')
    
    for i in range(n):
        #pick a random first digit
        p=random.choice(init_dig)
        #Randomize the rest of the number
        nif= p + numb_(9-len(p))

        #Calculate the true validaion number
        val=(int(nif[7])*2+int(nif[6])*3+int(nif[5])*4+int(nif[4])*5+int(nif[3])*6+int(nif[2])*7+int(nif[1])*8+int(nif[0])*9) % 11
        
        #If the validation number (nif[8]) is equal to the true valdiation number replace it with a incorret one
        if ( ((val0==0)|(val0==1)) & (nif[8]=='0')):
            nif=nif[0:8]+str(random.randint(1,9))
        elif ((val0!=0) & (val0!=1) & (nif[8]==str(11-val0))):
            nif= nif[0:8]+ str( random.choice([x for x in range(10) if x != (11-val0)]))
        
        #print([nif])   
        writer.writerow([nif])
        
    f.close()


# In[61]:


generate_nifs(100000)


# In[58]:


'''
with open('data_nifs.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row[0])
'''


# In[ ]:




