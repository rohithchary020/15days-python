
# by using read , write and append
a=open('bio.txt','r')
l=[]
res=a.readlines()
while res:
    l.append(res)
    res=a.readlines()
a.close()
for i in l:
    print(i)
with open('bio.txt','w') as file:
  file.write("res")


a=open('bio.txt','a')
n1=int(input("ente any no1:"))
n2=int(input("ente any no2:"))

sum=n1+n2
a.write(str(n1)+"\n")
a.write(str(n2)+"\n")
a.write(str(sum)+"\n")
print("ok")
