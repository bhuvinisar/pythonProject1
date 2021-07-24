try:
    f=open("write.txt","x")
    f.close()
    print("julie")
except Exception as e:
    print(e)
f=open("my1.doc","w")
f.write("Hello world!")
f.close()