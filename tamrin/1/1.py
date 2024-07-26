import re

def email_reg(email):
    # regex for email 
    email_pattern = re.compile(r"([A-Za-z0-9]+[.])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

    if re.fullmatch(email_pattern, email):  
        print("email is ok!")  
    else:  
        print("email is wrong!")  



def math_reg(math):
    # regex for mathmatical phrases 
    math_pattern = r'^-?\d+([-+*/]-?\d+)*$'
    
    if re.match(math_pattern, math):
        print("math is ok!")  
    else:  
        print("math is wrong!")  



def URL_reg(URL):
    # regex for URL  
    URL_pattern = r'[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)'
    
    if re.match(URL_pattern, URL):
        print("URL is ok!")  
    else:  
        print("URL is wrong!")  


def post_reg(post):
    # regex for post  
    post_pattern = r'^\d{5}[-\s]\d{5}?$'
    
    if re.match(post_pattern, post):
        print("post is ok!")  
    else:  
        print("post is wrong!")  



def phone_reg(phone):
    # regex for phone  
    phone_pattern = r'^0098-\d{3}-\d{3}-\d{4}$'
    
    if re.match(phone_pattern, phone):
        print("phone is ok!")  
    else:  
        print("phone is wrong!")  


input0 = "saba.razi@il.IO"
email_reg(input0)

input1 = "saba.razi@gmail.com"
email_reg(input1)

input2 = "saba#@gmail.com"
email_reg(input2)

input3 = "2+3-7/4"
math_reg(input3)

input4 = "2++-7/4"
math_reg(input4)

input5 = "-27+1"
math_reg(input5)

input6 = "https://github.com/G-force-Software-Engineering-gp"
URL_reg(input6)

input7 = "https://trello.com/b/8VjDchnN/g-force"
URL_reg(input7)

input8 = "https://trello/b/8VjDchnN/g-force"
URL_reg(input8)

input9 = "22222-7777"
post_reg(input9)

input10 = "2222-77778"
post_reg(input10)

input11 = "83702 29304"
post_reg(input11)

input12 = "0098-935-695-0935"
phone_reg(input12)

input13 = "0098-021-240-7394"
phone_reg(input13)

input14 = "0097-021-240-7394"
phone_reg(input14)

input15 = "0098-1-240-7394"
phone_reg(input15)