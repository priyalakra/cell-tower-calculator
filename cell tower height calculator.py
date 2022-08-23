#!/usr/bin/env python
# coding: utf-8

# In[16]:


import math

#To read input.txt file
fout=open('C:\\Users\\Lenovo\\Documents\\input.txt','r')
f=fout.readlines()


# to read height of building A
bah=(int)(f[0].strip())
# to read height of building B
bab=(int)(f[1].strip())
# to read inter building distance between A and B
ibd=(int)(f[2].strip())
# Transmission frequency
freq=(int)(f[3].strip())
#Numbers of buildings
nob=int(f[4].strip())
#store the building distance from A
buildist=[]
#store height of each building
height=[]
#initializing tower1 height with building A height
tower1=bah
#list to keep status of each building for los,nlos
status=[0]*len(radius)
#store gap in height
interdist=[0]*len(radius)


x=(f[5].strip()).split(" ")
for i in x:
    buildist.append(int(i))
y=(f[6].strip()).split(" ")
for j in y:
    height.append(int(j))

#calculating wavelength
c=3*(10**8)
fre=freq*(10**9)
wavelength=c/fre


#calculating Distance D2 of building from B
radius=[]
for i in range(len(buildist)):
    d2=ibd-buildist[i]
    r=math.sqrt(wavelength*(buildist[i]*d2)/ibd)
    radius.append(r)
print(radius)


# main logic to calculate height of towers
while True:
    i=0  
    for i in range(len(height)):
    
        d=height[i]
        forlos=radius[i]*0.6
        los=tower1-forlos
        forNlos=radius[i]*0.4
        nlos=tower1-forNlos
        #print(d,los,nlos)
        if d<los:
             status[i]=1
        elif d<nlos:
             status[i]=2
        else:
             flag=1
        interdist[i]=los-d
    if flag==1:
        tower1+=1
        flag=0
    else:
        break
        
        
heightoftower1=tower1-bah
heightoftower2=tower1-bab
   
#Calculate gap in height of each building

if(tower1-bah> 20 or tower1-bab>20):
    print("Not feasible")
else:
    print("Feasible")
    for i in range(len(status)):
        if status[i]==1:
            print("Building",i," on LoS")
        elif status[i]==2:
            print("Building",i,"on NearLoS")
    
    print("Frequency ",freq)
    print("Height of anntenna 1 is",heightoftower1)
    print("Height of anntenna 2 is",heightoftower2)
    print(interdist)
    
    # transmit power
    x=(wavelength/(4*3.14*ibd))**2
    power=100/x
    print("Transmission power",power)
    

  


    



# In[ ]:





# In[ ]:




