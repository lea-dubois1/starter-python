def myFunction(*nombres):
    
    mylist = []    
    
    for i in nombres:
        mylist.append(i)
        mylist.sort()
    
    print(mylist)


myFunction(1, 6, 81, 48, 10, 7, 14, 4, 2)