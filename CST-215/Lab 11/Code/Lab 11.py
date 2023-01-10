# Calculated explicit equation
def Explicit(n):
    # equation: ((4/3)^(n-1))*5
    answer = ((4/3) ** (n-1)) * 5
    # in instances where it has a decimal of .0 it removes it for cleaner format
    if answer == int(answer):
        answer = int(answer)
    return answer

# given recursive function
def Recursive(an, n):
    #if it is a1 then because it is recursive, no equation would be applied
    if n != 1:
        an = (4*an)/3
    return an

### starting a1 value ###
a1 = 5
an = a1
### starting a1 value ###

### prints print statement header ###
print("Recursive     Explicit")
print("-------------------------")
### prints print statement header ###

for n in range(1,21):
    # runs explicet formula
    e_answer = Explicit(n)
    # runs recursive formula
    r_answer = Recursive(an, n)
    # gets raw an value from recursive function to put into new one
    an = r_answer
    ### rounds numbers same decimal place ###
    e_answer = round(e_answer,2)
    r_answer = round(r_answer,2)
    ### rounds numbers same decimal place ###
    
    ### prints a clean line ###
    line = str(r_answer) + str(e_answer).rjust(15)
    print(line)
    ### prints a clean line ###