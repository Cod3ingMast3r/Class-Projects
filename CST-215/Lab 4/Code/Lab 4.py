##### Incomplete!!! #####
from itertools import combinations


def Main():
    Variables = ['A', 'B']
    combinations = Combinations(Variables,['T', 'F'])
        
##### comparison for AND #####
    rowVals = []
    title = 'AND'
    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        if variableSetDict[Variables[0]] == 'T' and variableSetDict[Variables[1]] == 'T':
            bool_Val = 'True '
        else:
            bool_Val = 'False'

        row_val = "|  " + Variables[0] + " = " + variableSetDict[Variables[0]] + ", " + Variables[1] + " = " + variableSetDict[Variables[1]] + "  | "+ Variables[0] + " " + title + " " + Variables[1] + " = " + bool_Val + "  |"
        rowVals.append(row_val)
    FormTable(title, rowVals)
##### comparison for AND #####
    print()
##### comparison for NAND #####
    rowVals = []
    title = 'NAND'
    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        if variableSetDict[Variables[0]] == 'T' and variableSetDict[Variables[1]] == 'T':
            bool_Val = 'False'
        else:
            bool_Val = 'True '

        row_val = "|  " + Variables[0] + " = " + variableSetDict[Variables[0]] + ", " + Variables[1] + " = " + variableSetDict[Variables[1]] + "  | "+ Variables[0] + " " + title + " " + Variables[1] + " = " + bool_Val + "  |"
        rowVals.append(row_val)
    FormTable(title, rowVals)
##### comparison for NAND #####


##### comparison for OR #####
    rowVals = []
    title = 'OR'
    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        if variableSetDict[Variables[0]] == 'T' or variableSetDict[Variables[1]] == 'T':
            bool_Val = 'True '
        else:
            bool_Val = 'False'

        row_val = "|  " + Variables[0] + " = " + variableSetDict[Variables[0]] + ", " + Variables[1] + " = " + variableSetDict[Variables[1]] + "  | "+ Variables[0] + " " + title + " " + Variables[1] + " = " + bool_Val + "  |"
        rowVals.append(row_val)
    FormTable(title, rowVals)
##### comparison for OR #####
    print()
##### comparison for NOR #####
    rowVals = []
    title = 'NOR'
    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        if variableSetDict[Variables[0]] == 'T' or variableSetDict[Variables[1]] == 'T':
            bool_Val = 'False'
        else:
            bool_Val = 'True '

        row_val = "|  " + Variables[0] + " = " + variableSetDict[Variables[0]] + ", " + Variables[1] + " = " + variableSetDict[Variables[1]] + "  | "+ Variables[0] + " " + title + " " + Variables[1] + " = " + bool_Val + "  |"
        rowVals.append(row_val)
    FormTable(title, rowVals)
##### comparison for NOR #####
    print()
##### comparison for XOR #####
    rowVals = []
    title = 'XOR'
    for variableSet in combinations:
        variableSetDict = combinations[variableSet]
        if (variableSetDict[Variables[0]] == 'T' or variableSetDict[Variables[1]] == 'T') and (variableSetDict[Variables[0]] != variableSetDict[Variables[1]]) :
            bool_Val = 'True '
        else:
            bool_Val = 'False'

        row_val = "|  " + Variables[0] + " = " + variableSetDict[Variables[0]] + ", " + Variables[1] + " = " + variableSetDict[Variables[1]] + "  | "+ Variables[0] + " " + title + " " + Variables[1] + " = " + bool_Val + "  |"
        rowVals.append(row_val)
    FormTable(title, rowVals)
##### comparison for XOR #####
    print()
##### comparison for NOT #####
    NOTcombinations = {Variables[0] +':T':{Variables[0] : 'T'},Variables[0] +':F':{Variables[0] : 'F'}}
    rowVals = []
    title = 'NOT'
    for variableSet in NOTcombinations:
        NOTVariableSetDict = NOTcombinations[variableSet]
        if (NOTVariableSetDict[Variables[0]] == 'T') :
            bool_Val = 'False'
        else:
            bool_Val = 'True '

        row_val = "|     " + Variables[0] + " = " + NOTVariableSetDict[Variables[0]] + "    |    " + title + " " + Variables[0] + " = " + bool_Val + "   |"
        rowVals.append(row_val)
    FormTable(title, rowVals)
##### comparison for NOT #####


def FormTable(title, rows = []):
    ##### Prints Header #####
    header = header = "|          "+ title + ' truth table' +"          |"
    divider = "+"
    for dashes in range(1,len(header)-1):
        divider += '-'
    divider += '+'

    print(divider)
    print(header)
    print(divider)
    for row in rows:
        print(row)
    print(divider.replace('+', ""))
    ##### Prints Header #####

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