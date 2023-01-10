def isSubset(A,B):
    if not A.difference(B):
        return True
    else:
        return False


A = {5, 7, 8}
B = {5, 7, 8, 9}

# Combination of A and B
print("Union: " + str(A.union(B)))
# Takes what is matching in A and B
print("Intersection: " + str(A.intersection(B)))
# Takes A-B (Subtracts all values of B from A and prints what is left over from A)
print("Difference: " + str(A.difference(B)))
# Takes A-B and B-A and combines it (what eve is Unique in both sets will be in this one)
print("Symmetric: " + str(A.symmetric_difference(B)))

# Returns true if all elements of A are in B
print("Is Subset: " + str(isSubset(A,B)))




