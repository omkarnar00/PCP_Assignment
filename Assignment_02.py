def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line


line=input("ENTER A STRING :")
result=split_and_join(line)
print(result)