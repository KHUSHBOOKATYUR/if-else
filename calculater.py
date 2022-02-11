num=int(input("enter the number:-"))
num1=int(input("enter the number:-")) 
symbol=input("enter any symbol:-")
if symbol=="+":
    print(num+num1)
elif symbol=="-":
    print(num-num1)
elif symbol=="*":
    print(num*num1)
elif symbol=="%":
    print(num%num1)
elif symbol=="**":
    print(num**num1)
elif symbol=="//":
    print(num//num1)
else:
    print("error")
                               