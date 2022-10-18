def myFunction(*nombres):
    
    mylist = []   

    for i in range(0, len(mylist)):  
        mylist.append(i)
        temporaire=mylist[i]
        j = i - 1 
        while   j >=0 and mylist[j] > temporaire: 
            mylist[j+1] = mylist[j]
            j -= 1
    
        mylist[j+1] = temporaire

        
    
    return mylist

print(myFunction(1, 6, 81, 48, 10, 7, 14, 4, 2))