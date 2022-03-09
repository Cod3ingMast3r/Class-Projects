
def Collatz(C = 0):
    # forces positive non-zero int
    # while (C%2 != 0) or (C == 0): 
    #         C = int(input("Enter positive Int: "))
    initialC = C
    Sequence = []
    Sequence.append(initialC)
    while C != 1:
        if (C%2 == 0):
            C = int(C/2)
        else:
            C = int(((3*C) + 1))
        Sequence.append(C)
    
    print("C[0] = " + str(initialC) + " has " + str(len(Sequence)) + " terms")
Collatz(65)
Collatz(66)
Collatz(67)
print()
Collatz(98)
Collatz(99)
Collatz(100)
Collatz(101)
Collatz(102)

Collatz(102342)