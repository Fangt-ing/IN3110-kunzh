from pydoc import stripid
import sys, os, re
import numpy as np
import matplotlib as plt
from bs4 import BeautifulSoup
from filter_urls import find_urls
from requesting_urls import get_html


def extrac_etams():
    """
    Extract team names and urls from the NBA Playoff 'Bracket' section table.
    URL: https://en.wikipedia.org/wiki/2021_NBA_playoffs
    Returns :
        team_names ( list ): A list of team names that made it to the conference semifinals.
        team_urls ( list ): A list of absolute Wikipedia urls corresponding to team_names .
    """
    url = 'https://en.wikipedia.org/wiki/2021_NBA_playoffs'
    base_url = 'https://en.wikipedia.org'
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    # find the wanted brackets
    bracket_header = soup.find(id='Bracket')
    bracket_table = bracket_header.find_next('table')
    rows = bracket_table.find_all('tr')
    
    team_list = []
    team_names = []
    team_urls = []
    
    for i in range (1, len(rows)):
        # cells = rows[i].find_all('td')
        # cells_text = [cell.get_text(strip=True) for cell in cells]
        # # filter out empty cells
        # cells_text = [cell for cell in cells_text if cell]
        
        # find out the team name
        name = rows[i].find_all('a')
        team_name = [nm.get_text(strip=True) for nm in name]
        # 1st element is not team info
        if i >= 1:
            excluded = ['Eastern Conference','Western Conference']
            # ensure the team name is not empty
            if len(team_name) >=1 and team_name[0] not in excluded :
                team_names.append(team_name[0])
                
        # find the team url as turl
        turl = rows[i].find_all('a')
        team_url = [base_url + trl.get('href') for trl in turl]
        if i >= 1:
            excluded = ['https://en.wikipedia.org/wiki/Eastern_Conference_(NBA)',
                        'https://en.wikipedia.org/wiki/Western_Conference_(NBA)']    
            if len(team_url) >= 1 and team_url[0] not in excluded:
                team_urls.append(team_url[0])
    
    for team in team_names:
        if team not in team_list:
            team_list.append(team)
        # filter out the teams taht appear more than once, which means they made it to the conference semifinals
    team_list_filtered = []
    counts = 0
    for team in team_names:
        for i in  range(len(team_names)):
            if team == team_names[i]:
                counts += 1
            # at the end of the list iteration reset counts values
            # and append values to team_list_filtered for repeated teams
            if i == len(team_names) -1:
                if counts >2:
                    if team not in team_list_filtered:
                        team_list_filtered.append(team)
                counts = 0
        
    return team_names, team_urls

def extract_players(team_url):
    """
    """
    
    base_url = 'https://en.wikipedia.org'
    
    # get html for each page using the team url extracted before
    html = get_html(team_url)
    
    soup = BeautifulSoup(html, 'html.parser')
    roster_header = soup.find(id='Roster')
    # identify table
    roster_table = roster_header.find_next('table')
    rows = roster_table.find('tr')
    
    # initialize empty lists for player names and urls
    player_names = []
    player_urls = []
    
    for i in range(0, len(rows)):
        cells =  rows[i].find_all('td')
        cells_text = [cell.get_text(strip=True) for cell in cells]
        
        if len(cells_text) == 7:
            rel_url = cells[2].find_next('a').attrs['href']
            
    return player_names, player_urls