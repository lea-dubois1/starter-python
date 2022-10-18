myList = [1, 41, 8, 16, 39, 105, 6]

def mySort(*nombres):
    for i in nombres:
        myList.append(i)
    
    return(sorted(myList))

def myDisplay(*nombres):
    
    for i in nombres:
        myList.append()

    print(myList)

mySort()
myDisplay()
