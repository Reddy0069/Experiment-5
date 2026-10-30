
tup = (20, 40, 60, 80, 100)

print("Elements:", tup)

print("First Value:", tup[0])
print("Last Value:", tup[-1])
print("Total Elements:", len(tup))
print("Occurrences of 20:", tup.count(20))
print("Position of 60:", tup.index(60))

print("Largest Value:", max(tup))
print("Smallest Value:", min(tup))
print("Total Sum:", sum(tup))

print("Is 40 available?", 40 in tup)

# Convert tuple to list
lst = list(tup)
print("List:", lst)

# Convert list back to tuple
new_tup = tuple(lst)
print("Tuple after conversion:", new_tup)
```
