def myFunction(*nombres):
    
    mylist = []    
    
    for i in nombres:
        mylist.append(i)
    
    print(sorted(mylist))


myFunction(1, 6, 81, 48, 10, 7, 14, 4, 2)