a=input("Enter driver name: ")
b=input("Enter destination ")
c=float(input("Enter distance (km): "))
d=float(input("Enter fuel consupmtion (L/100km): "))
e=float(input("Enter fuel cost (KZT/L): "))
print("="*30)
print("Driver: "+a)
print("Destination: "+b.upper())
print("Distance:",c,"km")
print("Fuel cost",c/100*d*e,"KZT")
if c<100:
    print("Category: Short trip")
elif c>100 and c<500:
    print("Category: Medium trip")
else:
    print("Category: Long trip")

print("="*30)
print("Cost breakdown:")
for i in range(100,int(c),100):
    print(i,"km → ",e*i,"KZT")
print("Destination uppercase : ", b.upper())
print("Destination lowercase : ", b.lower())
print("Length", len(b))
print("Letter 'a' count :" ,b.count("a"))