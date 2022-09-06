#!/usr/bin/env python
# coding: utf-8

# **<center>Solve the following Linear Program: <br>
# Min 5x+4y<br>
# s.t. 
#    x+y>=8<br>
#    2x+y>=10<br>
#    x+4y>=11**<br>
# 

# In[3]:


from gurobipy import *


# In[4]:


opt_mod=Model(name='linear program')


# In[6]:


x=opt_mod.addVar(name='x', vtype=GRB.CONTINUOUS, lb=0)
y=opt_mod.addVar(name='y', vtype=GRB.CONTINUOUS, lb=0)


# In[8]:


obj_fn=5*x+4*y
opt_mod.setObjective(obj_fn, GRB.MINIMIZE)


# In[9]:


c1=opt_mod.addConstr(x+y>=8, name='c1')
c2=opt_mod.addConstr(2*x+y>=10, name='c2')
c3=opt_mod.addConstr(x+4*y>=11, name='c3')


# In[10]:


opt_mod.optimize()
opt_mod.write("linear model.lp")


# In[11]:


print('Objective Function Value: %f' % opt_mod.objVal)
for v in opt_mod.getVars():
    print('%s: %g' % (v.varName, v.x))


# In[ ]:




