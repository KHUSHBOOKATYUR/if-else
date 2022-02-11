print("welcome to the state bank of india")
ATM_card=input("please enter your atm card : - ")
if ATM_card=="debit card" or ATM_card=="credit card":
    print(ATM_card,"your are card is execuded")
    language=input("enter your language : - ")
    if language=="english" or  language=="hindi" or language=="urdu":
        print(language,"it is selected")
        account=input("enter your account : - ") 
        if account=="saving" or account=="salrid":
            print(account,"enter your account")
            pin_number=input("enter your pin_number:-")
            if pin_number=="2634":
                print(pin_number,"enter your pin_number")
                amount=input("enter your amount:-")
                if amount==2000:
                    print(amount,"yes I goted amount")
                    remove=input("remove your card")
                    if remove=="card is remove":
                        print(yes,"your card is remved")
                    else:
                        print("your tranjestion is sucessfully thankyou so much")
                else:
                    print("nothing")
            else:
                print("no")
        else:
            print("yes")
    else:
        print("no")
else:
    print("everything")

                    
            


    

