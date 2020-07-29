#!/usr/bin/env python
# coding: utf-8

# # Assignment day 7

# # assignment 1
# - port1 = {21 : "FTP" , 22 : "SSH" , 23 : "telnet" , 80 :"http"}
# - make a new dictionary in which key become values and value become keys 
# - output : {'FTP': 21, 'SSH': 22, 'telnet': 23, 'http': 80}

# In[10]:


port1 = {21 : "FTP" , 22 : "SSH" , 23 : "telnet" , 80 :"http"}
print("port1 =", port1)

port2 = {value:key for key, value in port1.items()}
print("port2 =" , port2)


# # Assignment 2
# - list1=[(1,2) , (3,4) ,(5,6) ,(4,5)]
# - make new list which contain sum of the number of the tuples
# - input ;[(1,2) , (3,4) ,(5,6) ,(4,5)]
# - outpu : [3,7,11,9]

# In[11]:


list1=[(1,2),(3,4),(5,6),(4,5)]
res=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    res.append(a+b)
print(res)


# In[ ]:




