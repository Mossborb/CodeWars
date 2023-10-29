def abbrev_name(name):
    aList = name.split() #Splits name into a list
    initialList = [] #Creates a new list to store initials in
    for i in aList:
        
        initialList.append(i[0].upper())

    initials = initialList[0] + "." + initialList[1] #Adds initials together
    return initials

def reverse_seq(n):
    sequenceList = [] #Create an empty List
    while n > 0: #Iterate through all numbers and add them into a list counting down
        sequenceList.append(n)
        n -= 1
    return sequenceList



def reverse_words(text):
    reversedString = ""
    for i in text:
        reversedString = i + reversedString

    return reversedString


def count_sheep(sheep):
    sheepAmount = 0
    for i in sheep:
        if i == True:
            sheepAmount += 1

    return sheepAmount


