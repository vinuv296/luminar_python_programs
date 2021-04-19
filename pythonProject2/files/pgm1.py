#file
#file operations
#1. Read - Read data from a file - ' r ' (symbol)
#2. Write - write data to a file - ' w '
#3. Append - Add data into a file - ' a '

#first create a file reference
# f=open("filepath","mode of operation")
#
# f=open("filepath","r")
# f=open("filepath","w")
# f=open("filepath","a")

f=open("sample","r")
for i in f:
    print(i)

r=open("C:/Users/HP/PycharmProjects/pythonProject2/text.txt","r")
for j in r:
    print(j)






