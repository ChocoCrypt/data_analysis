#!/usr/bin/env python
# coding: utf-8

# In[5]:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# In[59]:
x_1 = [1,2,3,3,4,5,6,7,9,11]
x_2 = [18.95, 19.00 , 17.95,15.54,14.00,12.95,9.94,7.5,6.00,4]
# vamos a declarar el DataFrame 
# In[60]:
df_numeros=pd.DataFrame(data={'x1':x_1,'x2':x_2})
# In[61]:
df_numeros
# In[75]:
medias=df_numeros.mean()
# In[76]:
matriz_covarianza=df_numeros.cov()
# In[77]:


matriz_correlacion=df_numeros.corr()


# In[70]:


df_numeros.var()


# In[72]:


plt.scatter(df_numeros['x1'],df_numeros['x2'])


# In[78]:


medias


# In[82]:


matriz_covarianza


# In[79]:


matriz_correlacion


# #  aqui termina la tarea 1 

# In[ ]:





# In[13]:


aux=np.random.randint(10,15,10**8)


# In[19]:


get_ipython().run_cell_magic('time', '', 'np.mean(aux)')


# In[17]:


get_ipython().run_cell_magic('time', '', 'media(aux)')


# In[83]:


x1=[-6,-3,-2,1,2,5,6,8]
x2=[-2,-3,1,-1,2,1,5,3]


# In[89]:


numeros_dos=pd.DataFrame(data={'x1':x1,'x2':x2})


# In[90]:


plt.scatter(numeros_dos['x1'],numeros_dos['x2'])


# In[109]:


numeros_dos


# In[111]:


def rot_matrix(theta):
    theta=np.radians(theta)
    rotation_matrix=[[0]*2]*2
    cos_t=np.cos(theta)
    sin_t=np.sin(theta)
    rotation_matrix=np.array([[cos_t,-sin_t],[sin_t,cos_t]])
    return rotation_matrix


# In[112]:


rotation26deg=rot_matrix(26)


# In[113]:


rotation26deg


# In[118]:


rotated=pd.DataFrame(numeros_dos.values.dot(rotation26deg),columns=['rotated_x','rotated_y'])


# In[120]:


rotated


# metodo 2

# In[124]:


numeros_dos['x1_gorro']=numeros_dos['x1']*cos_t+numeros_dos['x2']*sin_t
numeros_dos['x2_gorro']=numeros_dos['x2']*cos_t-numeros_dos['x1']*sin_t


# In[125]:


numeros_dos


# In[123]:


theta=np.radians(26)
cos_t=np.cos(theta)
sin_t=np.sin(theta)


# Grafique los datos como un diagrama de dispersion y calcule s11 s12 y s22

# In[136]:


covarianzas=numeros_dos[['x1_gorro','x2_gorro']].cov()


# In[137]:


covarianzas


# In[130]:


numeros_dos.mean()


# In[131]:


punto_nuevo=[4,-2]


# In[134]:


rotado_nuevo=[0,0]
rotado_nuevo[0]=punto_nuevo[0]*cos_t+punto_nuevo[1]*sin_t
rotado_nuevo[1]=punto_nuevo[1]*cos_t-punto_nuevo[0]*sin_t


# In[135]:


rotado_nuevo


# In[141]:


dist=np.sqrt(rotado_nuevo[0]**2/covarianzas.iloc[0,0]+rotado_nuevo[1]**2/covarianzas.iloc[1,1])


# In[142]:


dist

