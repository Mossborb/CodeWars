def abbrev_name(name):
    aList = name.split() #Splits name into a list
    initialList = [] #Creates a new list to store initials in
    for i in aList:
        
        initialList.append(i[0].upper())

    initials = initialList[0] + "." + initialList[1] #Adds initials together
    return initials



