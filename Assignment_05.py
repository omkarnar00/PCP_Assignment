def swap_case(str):
    str1=str()
    for i in s:
        if i.isupper():
            i=i.lower()
            str1=str1+i
        else:
            i=i.upper()
            str1=str1+i
    return s


s=input(("ENTER A STRING : "))
res=swap_case(s)




