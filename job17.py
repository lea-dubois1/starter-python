def myFunction(*nombres):
    
    mylist = []    
    
    for i in nombres:
        
        if i % 2 == 0:
            mylist.append(i)
    
    print(mylist)


myFunction(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)