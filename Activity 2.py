set1={1,2,3,4,5,6}
print(set1)

set1.add(7)
print("After addition", set1)

set2={4,4,5,6,7,8}

set3=set1.difference(set2)
print("Difference of set1 and set2 is ",set3)

set4=set1.intersection(set2)
print("Intersection of set1 and set2 is", set4)

set5=set1.union(set2)
print("Union of set1 and set2 is", set4)

set6=set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2 is", set4)