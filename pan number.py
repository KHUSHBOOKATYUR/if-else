pan_num=input("enter your pan number-:")
len_pan_num=len(pan_num)
if len_pan_num==10:
    five_chars=pan_num[0:5]

    if five_chars.isupper()and five_chars.isalpha():
        four_num=pan_num[5:9]  

        if four_num.isdigit():
            last_letter=pan_num[9] 

            if last_letter.isupper() and last_letter.isalpha():
                print("valid pan number") 
            else:
                print("invalid pan number")
        else:
            print("invalid pan number")
    else:
        print("invalid pan number")
else:
    print("invalid pan number")