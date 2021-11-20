#!/usr/bin/env python
# coding: utf-8

# In[13]:


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
    f=open("data.nifs.csv","a",newline='')
    writer=csv.writer(f,delimiter=' ')
    
    for i in range(n):
        #pick a random first digit
        p=random.choice(init_dig)
        #Randomize the rest of the number
        nif= p + numb_(9-len(p))

        #Calculate the true validaion number
        val=(int(nif[7])*2+int(nif[6])*3+int(nif[5])*4+int(nif[4])*5+int(nif[3])*6+int(nif[2])*7+int(nif[1])*8+int(nif[0])*9) % 11
        
        #If the validation number is 0 or 1 then nif[8] is 0 oherwise is 11-validation number
        if ( (val==0) | (val==1) ):
            nif=nif[0:8] + '0'
        else:
            nif= nif[0:8] + str(11-val)
           
        writer.writerow([nif])
        
    f.close()


# In[14]:


generate_nifs(100000)

