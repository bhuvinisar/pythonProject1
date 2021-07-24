books=['novels','magazines','stories','dictionaries','thesarus','travelouges']
x={'sections':books}
print(x['sections'])
row=int(input("Enter a number:"))
if row<=5:
    b=input("Enter the book:")
    if b in x:
        print("book available")
    else:
        print("not available")
else:
    print("Enter row below 5")


