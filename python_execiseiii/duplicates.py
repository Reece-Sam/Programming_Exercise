num = [1, 2, 3, 2, 4, 5, 1, 6, 3]

def remove_duplicates(duplist):
    noduplist = []
    
    for element in duplist:
        if element not in noduplist:
             noduplist.append(element)
    
    return noduplist

print(remove_duplicates(num))