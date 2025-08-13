friends = ["apple", "orange", 4, 573.34,  "False", "kaif"]
print(friends)
friends.append("Harry")
print(friends) # this happens because lists are mutable

# reverse and sort method
l1 = [1, 2, 4, 5, 534, 52,42, 43, 52, 54]
l1.reverse()
print(l1)
l1.sort()
print(l1)

# insert method : uses for inserting element in list
l2 =[ 3, 4, 5, 6, 7, 8]
l2.insert(5, 53434)
print(l2)
print(l2.pop(2))