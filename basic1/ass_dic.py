shop={'biscuits':50,'chocolates':80,'millets':150,'grains':160,'nuts':500,'aashirvad':100}
while True:
    s=input("Want to buy:")
    if s=='yes':
        x=input("Enter a item:")
        if x in shop:
            q=int(input("Enter quantity:"))
            q=q*(shop[x])
            print(q)
        else:
            print("Enter items in list")
    else:
        break