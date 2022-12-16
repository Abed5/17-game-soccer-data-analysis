import re
def jackpot_games_results_from_datum(datum):
    resultsRegex = re.compile(r'\d-\d')
    for i in range(len(datum[0])):
        mo = resultsRegex.search(datum[0][i])
        if mo != None:
            return [[elem[i] for elem in datum],[elem[-1] for elem in datum]]
    return 'Not found'

def jackpot_games_results_from_data(data):
    return [jackpot_games_results_from_datum(i) for i in data]

def has_all_entries(datum):
    d = datum[0]
    resultsRegex = re.compile(r'\d-\d')
    for i in range(len(d)):
        mo = resultsRegex.search(d[i])
        if mo == None:
            return False
    return True

def results_cleaning(result):
    prediction = result[1]
    results = [results_cleaning_(i) for i in result[0]]
    return [results,prediction]
def results_cleaning_(result):
    resultRegex = re.compile(r'\d-\d')
    mo = resultRegex.search(result)
    return mo.group()

def raw_results_to_outcome(result):
    goals_scored = result.split('-')
    if goals_scored[0] == goals_scored[1]:
        return 'X'
    elif int(goals_scored[0]) > int(goals_scored[1]):
        return '1'
    else:
        return '2'
    
def raw_results_to_outcome_(result):
    prediction = result[1]
    outcome = [raw_results_to_outcome(i) for i in result[0]]
    return [outcome, prediction]

def correct_prediction_count(outcome_prediction):
    count = 0
    for i in range(len(outcome_prediction[0])):
        if outcome_prediction[0][i] in outcome_prediction[1][i]:
            count+=1
    return count

def countconf(xs):
    mydict = {}
    mydict[0] = xs.count(0)
    mydict[1] = xs.count(1)
    mydict[2] = xs.count(2)
    mydict[3] = xs.count(3)
    mydict[4] = xs.count(4)
    mydict[5] = xs.count(5)
    mydict[6] = xs.count(6)
    mydict[7] = xs.count(7)
    mydict[8] = xs.count(8)
    mydict[9] = xs.count(9)
    mydict[10] = xs.count(10)
    mydict[11] = xs.count(11)
    mydict[12] = xs.count(12)
    mydict[13] = xs.count(13)
    mydict[14] = xs.count(14)
    mydict[15] = xs.count(15)
    mydict[16] = xs.count(16)
    mydict[17] = xs.count(17)

    return mydict

def list_of_lists_into_List(list_of_lists):
    big_list = []
    for i in list_of_lists:
        for j in i:
            big_list.append(j)
    return big_list

def count_instances_of(list_, item):
    counter = 0
    for i in list_:
        if i == item:
            counter += 1
    return counter

def unique_items(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

def get_first_item(element):
    return element[0]

if __name__ == "__main__":
    #import statements
    import shelve
    import matplotlib.pyplot as plt
    import numpy as np
    #program
    shelfFile = shelve.open('soccerplatform-mega-jackpot-data')
    data_ = shelfFile['data0']
    shelfFile.close()
    #print(data_[0])
    jackpotGamesResultsFromData = jackpot_games_results_from_data(data_)
    #print(jackpotGamesResultsFromData[-1])
    filteredObject = filter(has_all_entries, jackpotGamesResultsFromData)
    listOfFilteredGames = list(filteredObject)
    #print(len(listOfFilteredGames), len(data_))
    cleanedResults = [results_cleaning(i) for i in listOfFilteredGames]
    #print(cleanedResults[0])
    outcomeVsPrediction = [raw_results_to_outcome_(i) for i in cleanedResults]
    #print(outcomeVsPrediction[50])
    correctPredictionCount = [correct_prediction_count(i) for i in outcomeVsPrediction]
    #print(correctPredictionCount[0])
    myDict = countconf(correctPredictionCount)
    print(myDict)

    #Plotting number of correct predictions per jackpot
    xx = [item[0] for item in myDict.items()]
    yy = [item[1] for item in myDict.items()]
    xaxis = np.array(xx)
    yaxis = np.array(yy)

    plt.plot(xaxis,yaxis)
    plt.title("Soccerplatform Megajackpot Prediction Plot")
    plt.xlabel("Number of games predicted correctly out of 17")
    plt.ylabel("Count of jackpots")

    plt.show()

    #Basic Statistics
    outcomeListofLists = [i[0] for i in outcomeVsPrediction]
    print('Total number of jackpots: ' + str(len(outcomeListofLists)))
    outcomeBigList = list_of_lists_into_List(outcomeListofLists)
    print('Total number of games: ' + str(len(outcomeBigList)))

    print('Total number of outcome 1: ' + str(count_instances_of(outcomeBigList, '1')) + ' ' + str(count_instances_of(outcomeBigList, '1')/len(outcomeBigList)*100) + '% ' + str(count_instances_of(outcomeBigList, '1')/len(outcomeBigList)*17) + '/17')
    print('Total number of outcome 2: ' + str(count_instances_of(outcomeBigList, '2')) + ' ' + str(count_instances_of(outcomeBigList, '2')/len(outcomeBigList)*100) + '% ' + str(count_instances_of(outcomeBigList, '2')/len(outcomeBigList)*17) + '/17')
    print('Total number of outcome X: ' + str(count_instances_of(outcomeBigList, 'X')) + ' ' + str(count_instances_of(outcomeBigList, 'X')/len(outcomeBigList)*100) + '% ' + str(count_instances_of(outcomeBigList, 'X')/len(outcomeBigList)*17) + '/17')
    """
    print(count_instances_of(outcomeBigList, '1')/len(outcomeBigList)*17)
    print(count_instances_of(outcomeBigList, '2')/len(outcomeBigList)*17)
    print(count_instances_of(outcomeBigList, 'X')/len(outcomeBigList)*17)
    """

    #Count of jackpots with 1:2:X ration of 6:6:5
    l = [[count_instances_of(i, '1'), count_instances_of(i, '2'), count_instances_of(i, 'X')] for i in outcomeListofLists]
    k = count_instances_of(l, [6,6,5])

    #Count of ratios of 1:2:X
    uniqueInstances = unique_items(l)
    #print(uniqueInstances)
    m = [[count_instances_of(l,i), i] for i in uniqueInstances]
    #print(m)
    n = [i[0] for i in m]
    p = sorted(m, key = get_first_item, reverse=True)
    print('Count of ratios of 1:2:X')
    [print(i) for i in p]
    