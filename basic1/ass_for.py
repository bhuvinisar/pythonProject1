fruits=['apple','orange','watermelon','kiwi','litchi']
x=int(input("No. of fruits to add:"))
for i in range(x):
    f=input("Enter a fruit:")
    fruits.append(f)
    fruits.sort()
print(fruits)
