FILE = open('file-test.txt', 'r+')
value = FILE.read()
print (value)
i=0
while(i<5):
    FILE.write("qweyrty\n")
    i+=1
FILE.close()