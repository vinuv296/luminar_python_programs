import re
f=open("test_file_2",'r')
for i in f:
    #r='^[+91]\d{10}'
    r='[+][9][1]\d{10}'
    m=re.fullmatch(r,i)
    if m is not None:
        print(i)
        f = open("valid_numbers", "w")
        f.write(i)
