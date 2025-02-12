import re
from scipy import stats
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

def get_frequencies(xs):
    return {i:xs.count(i) for i in range(min(xs)-1,max(xs)+1)}


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

def standard_deviation(list):
    mean = sum(list)/len(list)
    squared_differences_from_mean = [(i - mean)**2 for i in list]
    variance = sum(squared_differences_from_mean)/len(list)
    standarddeviation = variance**0.5
    return standarddeviation

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
    myDict = get_frequencies(correctPredictionCount)
    print(myDict)

    #Plotting number of correct predictions per jackpot
    xx = [item[0] for item in myDict.items()]
    yy = [item[1] for item in myDict.items()]
    xaxis = np.array(xx)
    yaxis = np.array(yy)

    plt.plot(xaxis,yaxis)
    plt.title("Soccerplatform Prediction Plot")
    plt.xlabel("Number of games predicted correctly out of 17")
    plt.ylabel("Frequency of pools")

    #plt.show()

    #Standard deviation of correct predictions
    std_deviation = standard_deviation(correctPredictionCount)
    print('Standard Deviation of correct predictions is :' + "{:.2f}".format(std_deviation))


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
    # printing sorted list of ratio 1:2:X
    #[print(i) for i in p]
    
    print(outcomeListofLists[0])

    print("summary statistics on outcome 1")
    count_of_1 = [count_instances_of(i, '1') for i in outcomeListofLists]
    print("mean: " + "{:.2f}".format(sum(count_of_1)/len(count_of_1)))
    print("median: " + "{:.1f}".format((count_of_1[int(len(count_of_1)/2)] + 
                                        count_of_1[int(len(count_of_1)/2)+1])/2))
    print("mode: " + str(list(stats.mode(count_of_1).mode)[0]))

    print("summary statistics on outcome 2")
    count_of_2 = [count_instances_of(i, '2') for i in outcomeListofLists]
    print("mean: " + "{:.2f}".format(sum(count_of_2)/len(count_of_2)))
    print("median: " + "{:.1f}".format((count_of_2[int(len(count_of_2)/2)] + 
                                        count_of_2[int(len(count_of_2)/2)+1])/2))
    print("mode: " + str(list(stats.mode(count_of_2).mode)[0]))

    print("summary statistics on outcome X")
    count_of_X = [count_instances_of(i, 'X') for i in outcomeListofLists]
    print("mean: " + "{:.2f}".format(sum(count_of_X)/len(count_of_X)))
    print("median: " + "{:.1f}".format((count_of_X[int(len(count_of_X)/2)] + 
                                        count_of_X[int(len(count_of_X)/2)+1])/2))
    print("mode: " + str(list(stats.mode(count_of_X).mode)[0]))