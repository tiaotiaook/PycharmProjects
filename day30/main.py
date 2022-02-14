try:
    file=open("a_file.txt")
except:
    file=open("a_file.txt","w")
    file.write("something")