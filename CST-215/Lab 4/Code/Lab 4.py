##### Incomplete!!! #####

def Main():
    Variables = ['A', 'B']
    combinations = Combinations(Variables,['T', 'F'])
    ##### Prints Header #####
    header = "+  "+ str(Variables[0]) + "       "+ str(Variables[0]) + "     |       "+ str(Variables[0]) + " AND "+ str(Variables[1]) + "       "+ str(Variables[0]) + " OR "+ str(Variables[1]) + "       "+ str(Variables[0]) + " NAND "+ str(Variables[1]) +"       "+ str(Variables[0]) +" NOR "+ str(Variables[1]) +"  +"
    divider = "+"
    for dashes in range(1,len(header)-1):
        divider += '-'
    divider += '+'

    print(divider)
    print(header)
    print(divider)
    
    ##### Prints Header #####

    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        
    ##### comparison for p^q #####
        if variableSetDict[Variables[0]] == 'T' and variableSetDict[Variables[1]] == 'T':
            _and_ = 'T'
            _nand_ = 'F'
        else:
            _and_ = 'F'
            _nand_ = 'T'
    ##### comparison for p^q #####

    ##### comparison for pvq #####
        if variableSetDict[Variables[0]] == 'T' or variableSetDict[Variables[1]] == 'T':
            _or_ = 'T'
            _nor_ = 'F'
        else:
            _or_ = 'F'
            _nor_ = 'T'
    ##### comparison for pvq #####

    ##### comparison for p->q #####
        if (variableSetDict[Variables[1]] == 'T') or (variableSetDict[Variables[0]] == variableSetDict[Variables[1]]):
            _than_ = 'T'
        else:
            _than_ = 'F'
    ##### comparison for p->q #####

    ##### comparison for p<->q #####
        if variableSetDict[Variables[0]] == variableSetDict[Variables[1]]:
            _and_than_ = 'T'
        else:
            _and_than_ = 'F'
    ##### comparison for p<->q #####

    ##### Prints Values #####
        print("+  " + variableSetDict[Variables[0]] + "       " + variableSetDict[Variables[1]] + "     |          "+ _and_ + "            " + _or_ + "              " + _nand_ + "             " + _nor_ + "     +")
    ##### Prints Values #####

    ##### Prints Footer #####
    print(divider)
    ##### Prints Footer #####

def Combinations(variableArray, valuesArray):
    combinations = {}
    for variableIndex, variable in enumerate(variableArray):
        newCombinations = {}
        for value in valuesArray:
            if variableIndex == 0:
                newCombinations[variable + ':' + value] = ''
            else:
                for combination in combinations:
                    newCombination = combination + " " + variable + ':' + value
                    if newCombination not in combinations:
                        for variableSetIndex, variableSet in enumerate(newCombination.split(' ')):
                            letterVariable = variableSet.split(':')[0]
                            letterVariableValue = variableSet.split(':')[1]
                            if newCombination not in newCombinations:
                                newCombinations[newCombination] = {letterVariable:letterVariableValue}
                            else:
                                newCombinations[newCombination][letterVariable] = letterVariableValue
        combinations = newCombinations
    
    numberOfVariables = len(valuesArray)
    numberOfValues = len(variableArray)
    numberOfCombinations = numberOfVariables**numberOfValues
    distanceBetweenValues = numberOfCombinations/numberOfValues

    sortedCombinations = {}
    combinationsArray = []
    for combination in combinations:
        combinationsArray.append(combination)
    combinationsArray.sort(reverse=True)
    sortedCombinationsArray = combinationsArray
    for combination in sortedCombinationsArray:
        sortedCombinations[combination] = {}
        for variable in combinations[combination]:
            sortedCombinations[combination][variable] = combinations[combination][variable]
    return sortedCombinations

Main()