f=open('myfile.txt','w') 
r='Name:Soumya M.\nAge:19\nI am currently doing btech in electronics and communication engineering' 
f.write(r) 
f.close() 
f1=open('myfile.txt','r') 
p=f1.read() 
print(p) 
f1.close()