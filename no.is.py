amt=int(input("enter the amount:-"))
a=note500=amt//500
b=note400=amt//400
c=note300=amt//300
d=note200=amt//200
e=note100=amt//100
f=note50=amt//50
g=note20=amt//20
h=note10=amt//10
i=note5=amt//5
j=note2=amt//2
if a>=500:
    amt500=amt//500
    amt=a-note*500
if b>=400:
     note400=amt//400
     amt=b-note*400
if c>=300:
    note300=amt//300
    amt=c-note*300
if d>=200:
    note200=amt//200
    amt=d-note*200
if e>=100:
    note100=amt//100
    amt=e-note*100
if f>=50:
    note50=amt//50
    amt=f-note*50
if g>=20:
    note20=amt//20
    amt=g-note*20
if h>=10:
    note10=amt//10
    amt=h-note*10
if i>=5:
    note5=amt//5
    amt=i-note*5
if j>=2:
    note2=amt//2
    amt=j-note*2


print("500=","=",note500)
print("400=","=",note400)
print("300=","=",note300)
print("200=","=",note200)
print("100=","=",note100)
print("50=","=",note50)
print("20=","=",note20)
print("10=","=",note10)
print("2=","=",note2)