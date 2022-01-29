def Main():
    combinations = Combinations(['p', 'q'],['T', 'F'])
    ##### Prints Header #####
    print("+--------------------------------------------------------------+")
    print("+  p       q     |       p^q       pvq       p->q       p<->q  +")
    print("+--------------------------------------------------------------+")
    ##### Prints Header #####

    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        
    ##### comparison for p^q #####
        if variableSetDict['p'] == 'T' and variableSetDict['q'] == 'T':
            pAq = 'T'
        else:
            pAq = 'F'
    ##### comparison for p^q #####

    ##### comparison for pvq #####
        if variableSetDict['p'] == 'T' or variableSetDict['q'] == 'T':
            pvq = 'T'
        else:
            pvq = 'F'
    ##### comparison for pvq #####

    ##### comparison for p->q #####
        if (variableSetDict['q'] == 'T') or (variableSetDict['p'] == variableSetDict['q']):
            p_than_q = 'T'
        else:
            p_than_q = 'F'
    ##### comparison for p->q #####

    ##### comparison for p<->q #####
        if variableSetDict['p'] == variableSetDict['q']:
            p_and_than_q = 'T'
        else:
            p_and_than_q = 'F'
    ##### comparison for p<->q #####

    ##### Prints Values #####
        print("+  " + variableSetDict['p'] + "       " + variableSetDict['q'] + "     |        "+ pAq + "         " + pvq + "         " + p_than_q + "           " + p_and_than_q + "    +")
    ##### Prints Values #####

    ##### Prints Footer #####
    print("+--------------------------------------------------------------+")
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