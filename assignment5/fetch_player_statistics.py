import sys, os, re
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from filter_urls import find_urls
from requesting_urls import get_html


def extract_teams():
    """
    Extract team names and urls from the NBA Playoff 'Bracket' section table.
    URL: https://en.wikipedia.org/wiki/2021_NBA_playoffs
    Returns :
        team_names(list): A list of team names that made it to the conference semifinals.
        team_urls(list): A list of absolute Wikipedia urls corresponding to team_names.
    """
    url = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    base_url = "https://en.wikipedia.org"
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")
    # find the wanted brackets
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")

    team_list = []
    team_names = []
    team_urls = []

    for i in range(1, len(rows)):
        # cells = rows[i].find_all('td')
        # cells_text = [cell.get_text(strip=True) for cell in cells]
        # # filter out empty cells
        # cells_text = [cell for cell in cells_text if cell]

        # find out the team name
        name = rows[i].find_all("a")
        team_name = [nm.get_text(strip=True) for nm in name]
        # 1st element is not team info
        if i >= 1:
            excluded = ["Eastern Conference", "Western Conference"]
            # ensure the team name is not empty
            if len(team_name) >= 1 and team_name[0] not in excluded:
                team_names.append(team_name[0])

        # find the team url as turl
        turl = rows[i].find_all("a")
        team_url = [base_url + trl.get("href") for trl in turl]
        if i >= 1:
            excluded = [
                "https://en.wikipedia.org/wiki/Eastern_Conference_(NBA)",
                "https://en.wikipedia.org/wiki/Western_Conference_(NBA)",
            ]
            if len(team_url) >= 1 and team_url[0] not in excluded:
                team_urls.append(team_url[0])

    for team in team_names:
        if team not in team_list:
            team_list.append(team)
        # filter out the teams taht appear more than once, which means they made it to the conference semifinals
    team_list_filtered = []
    counts = 0
    for team in team_names:
        for i in range(len(team_names)):
            if team == team_names[i]:
                counts += 1
            # at the end of the list iteration reset counts values
            # and append values to team_list_filtered for repeated teams
            if i == len(team_names) - 1:
                if counts > 2:
                    if team not in team_list_filtered:
                        team_list_filtered.append(team)
                counts = 0

    return team_names, team_urls

def extract_players(team_url):
    """
    Extract team names and urls from the NBA Playoff 'Bracket' section table.
    team_url: https://en.wikipedia.org/wiki/2020%E2%80%9321_Milwaukee_Bucks_season
    Args:
        team_url(str): a url of the team containing player's info.
    Returns :
        team_names(list): A list of team names that made it to the conference semifinals.
        team_urls(list): A list of absolute Wikipedia urls corresponding to team_names.
    """

    base_url = "https://en.wikipedia.org"

    # get html for each page using the team url extracted before
    html = get_html(team_url)

    soup = BeautifulSoup(html, "html.parser")
    roster_header = soup.find(id="Roster")
    # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # initialize empty lists for player names and urls
    player_names = []
    player_urls = []

    for i in range(0, len(rows)):
        # cells =  rows[i].find_all('td')
        # cells_text = [cell.get_text(strip=True) for cell in cells]

        # if len(cells_text) == 7:
        #     rel_url = cells[2].find_next('a').attrs['href']
        #     player_urls.append(base_url+rel_url)

        name = rows[i].find_all("a")
        player_name = [nm.get_text(strip=True) for nm in name]
        # find player url
        purl = rows[i].find_all("a")
        player_url = [base_url + prl.get("href") for prl in purl]
        # append only the player info
        if len(player_name) > 1 and len(player_name) <= 3:
            player_names.append(player_name[1])
            player_urls.append(player_url[1])

    return player_names, player_urls

def extract_player_statistics(player_url):
    """
    Extract player statistics for NBA player.
    Player url: https://en.wikipedia.org/wiki/Giannis_Antetokounmpo.
    Args :
        player_url(str): URL to the Wikipedia article of a player.
    Returns :
        ppg(float): Points per Game.
        bpg(float): Blocks per Game.
        rpg(float): Rebounds per Game.
    """
    ppg = 0.0  # Points per Game: defines the best player
    bpg = 0.0  # Blocks per Game
    rpg = 0.0  # R ebounds per Game

    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")
    nba_header = soup.find(id="NBA_career_statistics")
    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")

    try:
        # check for different spellings, e.g. capitalization
        # take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season ")
        # identify thhe table
        nba_table = regular_season_header.find_next("table")
    except:
        try:
            # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")
        except:
            return ppg, bpg, rpg
    try:
        # find rows
        rows = nba_table.find_all("tr")
        # preare ppg, bpg and rpg lists
        ppgs, bpgs, rpgs = [], [], []
        for row in rows:
            # extract the year row
            year = row.find_all("td")
            # strip off the redandent info, get the desired info
            year_text = [info.get_text(strip=True) for info in year]
            # append only the sub-list that is 13 element long
            if len(year_text) >= 13:
                # ppg is the last item in the sub-list, bpg and rpg accordingly
                ppgs.append(year_text[-1])
                bpgs.append(year_text[-2])
                rpgs.append(year_text[-5])

        # make the result float, use try in case of none number string values.
        try:
            ppg = float(ppgs[-1].strip("\\n"))
            bpg = float(bpgs[-1])
            rpg = float(rpgs[-1])
        except ValueError:  # assing non-number string values to float(0)
            ppg = 0.0
            bpg = 0.0
            rpg = 0.0
    except:
        return ppg, bpg, rpg
    return ppg, bpg, rpg

# def best_player(teamX_url):
#     """
#     """
#     teams = extract_teams()
#     team_names = teams[0]
#     team_urls = teams[1]
    
#     for player_url in team_urls:

# def plot_NBA_player_statistics(teams):
#     """
#     """
#     # extrac_etams() returns team_names, team_urls
#     # extract_players() returns player_names, player_urls
#     # return ppg, bpg, rpg returns extract_player_statistics() 
    
#     teams={}
