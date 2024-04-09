need=0
print("Vyberte produkt (a,b,c)")
a=10
b=25
c=64
choice=input()
returnn=[]

if choice == "a":
    need+=a
if choice == "b":
    need+=b
if choice == "c":
    need+=c
print("Vložte",need)
money2=input()
money=money2
back=money-need
print(back, "Bude vráceno")

if back>50 or back==50:
    returnn.append (50)
    back-=50
if back>20 or back==20:
    returnn.append (20)
    back-=20
if back>10 or back==10:
    returnn.append (10)
    back-=10
if back>5 or back==5:
    returnn.append (5)
    back-=5
if back>2 or back==2:
    returnn.append (2)
    back-=2
if back>1 or back==1:
    returnn.append (1)
    back-=1

print("Vráceno",returnn)