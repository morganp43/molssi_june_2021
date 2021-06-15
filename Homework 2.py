#!/usr/bin/env python
# coding: utf-8

# # Homework 2
# Calculating Distances in water molecule

# In[5]:


import os,numpy



mol_file = os.path.join('data','water.xyz')


# In[60]:


data = numpy.genfromtxt(fname=mol_file,delimiter='',dtype='unicode',skip_header=2)


# In[61]:


num_atoms=len(data)


# In[62]:


label = data[:num_atoms,0] #row, col
coords = data[:num_atoms,1:].astype(float) #get float array of coords


# In[64]:


for i in range(0,num_atoms):
    for j in range(0,i):
        dist = numpy.sqrt( (coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2 + (coords[i][2]-coords[j][2])**2 )
        print(F'{label[i]}-{label[j]:4} : {dist:.3f}')


# In[ ]:




