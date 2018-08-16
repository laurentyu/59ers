from requests import get

url = "https://www.49ers.com/team/players-roster/"

response = get(url)
print(response.status_code)

from bs4 import BeautifulSoup
nfl = BeautifulSoup(response.content, 'html.parser')
#print(nfl.prettify())

nfl_div = nfl.find_all('div')
print(nfl_div)

nfl_main = nfl.find(id="main-content")
print(nfl_main.prettify())

nfl_roster = nfl_main.find(summary= "Roster")
print(nfl_roster.prettify())

nfl_roster_body = nfl_roster.find( 'tbody')
print(nfl_roster_body.prettify())
nfl_roster_body_tr_first = nfl_roster_body.find('tr')
print(nfl_roster_body_tr_first.prettify())

first_name = nfl_roster_body_tr_first.find_all('td')[7].text
print(first_name)

import csv


with open('first_name.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([first_name])

