def list_of_links_to_tables(path_to_txt_file):
    with open(path_to_txt_file, 'r') as f:
        lines = f.readlines()
    lines = [line for line in lines if line != '\n']
    stripped_lines = [line.strip() for line in lines]
    return stripped_lines

def jackpot_games_results_from_link(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(link, headers = headers)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    table = soup.table
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        #print(cols[2])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    #if len(data[0]) == 6: 
    #    return [elem[4] for elem in data]
    #elif len(data[0]) == 3:
    #    return [elem[1] for elem in data]
    #else:
    return data

def jackpot_games_results_from_links(links):
    results = []
    num_links = len(links)
    for i in range(num_links):
        clear_output(wait=True)
        result = jackpot_games_results_from_link(links[i])
        results.append(results)
        print(str(i + 1) + ' out of ' + str(num_links) + ' links processed. ' + "{:.2f}".format((i + 1)/num_links*100) + '%')
    return results




if __name__ == "__main__":
    #import statements
    import requests, bs4, re
    from IPython.display import clear_output

    
    #program body
    pathToTxtFile = 'soccerplatform-mega-jackpot-history-2016-2022.txt'
    my_list = list_of_links_to_tables(pathToTxtFile)
    #print(len(my_list))
    raw_data = jackpot_games_results_from_links(my_list[0:5])
    #print(raw_data)