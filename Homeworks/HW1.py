nums = list(range(21))

listOdd = []
listEven = []

for x in nums:
	if (x % 2 == 0) : 
		listEven.append(x)	
	if (x % 2 != 0) :
		listOdd.append(x)

print ("The even list: ", listEven)
print ("The odd list:  ", listOdd)

newlist = listOdd + listEven
print ("Merged list:  ", newlist)

newlist = [i * 2 for i in newlist]
newlist =sorted(newlist)

print ("Every element multiplied by 2 and sorted by ascending:  ", newlist)

for element in newlist:
    print(element, type(element))
