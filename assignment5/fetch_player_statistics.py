import sys, os, re, operator
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
# from filter_urls import find_urls
from requesting_urls import get_html


def extract_teams():
    """
    Extract team names and urls from the NBA Playoff 'Bracket' section table.
    URL: https://en.wikipedia.org/wiki/2021_NBA_playoffs
    Returns :
        team_names_urls (dictionary): A dictionary in the pair of team_name: team_url.
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
    team_names_urls={}
    for i in range(1, len(rows)):

        # find out the team name
        name = rows[i].find_all("a")
        team_name = [nm.get_text(strip=True) for nm in name]
        
        if len(team_name) >= 1:
            team_names.append(team_name[0])
        
        # find the team url as turl
        turl = rows[i].find_all("a")
        team_url = [base_url + trl.get("href") for trl in turl]
            
        if len(team_url)>=1:
            team_urls.append(team_url[0])
        

    team_names_urls.update({team_names[k]: team_urls[k] for k in range(len(team_names))})
    excluded = ["Eastern Conference", "Western Conference"]
    for exclude in excluded:
        team_names_urls.pop(exclude)

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
    return team_names_urls

def extract_players(team_url):
    """
    Extract team names and urls from the NBA Playoff 'Bracket' section table.
    team_url: https://en.wikipedia.org/wiki/2020%E2%80%9321_Milwaukee_Bucks_season
    Args:
        team_url(str): a url of the team containing player's info.
    Returns :
        player_names_urls (dictionary): A dictionary in the pair of player_name: player_url.
    """
    base_url = "https://en.wikipedia.org"
    html = get_html(team_url)
    soup = BeautifulSoup(html, "html.parser")
    roster_header = soup.find(id="Roster")
    # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # prepare dictionary for playr info in pair of {player_names: urls}
    player_names_urls={}
    for i in range(0, len(rows)):

        name = rows[i].find_all("a")
        player_name = [nm.get_text(strip=True) for nm in name]
        # find player url
        purl = rows[i].find_all("a")
        player_url = [base_url + prl.get("href") for prl in purl]
        # append only the player info
        if len(player_name) > 1 and len(player_name) <= 3:
            player_names_urls.update({player_name[1]: player_url[1]})

    return player_names_urls

def extract_player_statistics(player_url):
    """
    Extract player statistics for NBA player.
    Player url: https://en.wikipedia.org/wiki/Giannis_Antetokounmpo.
    Args :
        player_url(str): URL to the Wikipedia article of a player.
    Returns :
        (tuple):
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

class Player():
    """
    Player class to store information of a NBA player in a clear way.

    Attributes:
        team_name (str): Name of team the player belongs to.
        player_name (str): Name of the player.
        ppg (float): Player's score in points per game category.
        bpg (float): Player's score in blocks per game category.
        rpg (float): Player's score in rebounds per game category.
    """

    def __init__(self, team, player_name, ppg, bpg, rpg):
        """
        Initiates class instance.
        Args:
            team (str): Name of team the player belongs to.
            player_name (str): Name of the player.
            ppg (float): Player's score in points per game category.
            bpg (float): Player's score in blocks per game category.
            rpg (float): Player's score in rebounds per game category.
        """
        self.team_name = team
        self.player_name = player_name
        self.ppg = ppg
        self.bpg = bpg
        self.rpg = rpg

def extract_best_players(playoff_url):
    """
    Find the top 3 NBA players by points per game,
    with players name and scores(ppg, bpg, rpg).
    Args:
        playoff_url (str): url to wikipedia page for NBA playoffs 2020-2021.
    Returns:
        best_players (list): [(best_ppg, best_bpg, best_rpg), ...] containing
            Player class objects for the top 3 players by ppg, bpg and rpg.
    """
    teams = extract_teams()  # (dict): {"team": "team_url"}
    best_players = []

    for team in teams:
        # players (dict): {"player": "player_url"}:
        players = extract_players(teams[team])
        # stats (dict): {"player": (stats)}:
        stats = dict([(name, extract_player_statistics(players[name])) for name in players])
        # team_player (list): List of Player class objects:
        team_player = [Player(team, player, *stats[player]) for player in players]
        # Sort team_player list by Player class attributes ppg, bpg and rpg.
        # And extract the top 3 players in each category:
        best_ppg = sorted(team_player, key=operator.attrgetter("ppg"))[-3:]
        best_bpg = sorted(team_player, key=operator.attrgetter("bpg"))[-3:]
        best_rpg = sorted(team_player, key=operator.attrgetter("rpg"))[-3:]
        best_players.append((best_ppg, best_bpg, best_rpg))

    return best_players

def plot_best_players(playoff_url, key="ppg"):
    """
    Creates a bar plot of the top 3 players by either ppg, bpg or rpg using
    extract_best_players() function. The plot is saved to file players_over_{key}.png
    Args:
        playoff_url (str): url to wikipedia page for NBA playoffs. Note that this
            function only works for the 2019-20 season.
        key (:obj:"str", optional): The category in which the players are compared
            in. Defaults to "ppg".
    Raises:
        KeyError: Raised if key is not "ppg", "bpg" or "rpg".
    """
    keys = ["ppg", "bpg", "rpg"]
    if key not in keys:
        raise KeyError("Please choose a key from {'ppg', 'bpg', 'rpg'}.")

    tick_vals = []  # need to store x values for bars for xticks to work
    tick_labels = []  # need to store bar labels for xticks to work
    best_players = extract_best_players(playoff_url)

    # iterate over tuples in best_players and keep track of index so that the
    # players from each team can be grouped together in the plot:
    for i, team in enumerate(best_players):
        x = np.linspace(i+1, i+2, 3) + i  # x values for plotting
        players = team[keys.index(key)]  # get best players in chosen category
        # scores: get scores from each Player class object's attribute:
        scores = [getattr(player, key) for player in players]
        # names: get names from each Player class object's attribute:
        names = [player.player_name for player in players]
        plt.bar(x, scores, 0.3, label=players[0].team_name)
        tick_vals.extend(x.tolist())  # add x values to list
        tick_labels.extend(names)  # add player names to list

    # Label each bar with corresponding player name:
    plt.xticks(tick_vals, tick_labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.3)  # tweak spacing to prevent clipping of tick-labels
    plt.ylabel(key)
    plt.title(f"Top 3 players from each team based on {key}")
    plt.legend()
    plt.gcf().set_size_inches(20, 12)
    
    try:
        os.mkdir(f"NBA_player_statistics")
    except FileExistsError:
        pass
    os.chdir(f"NBA_player_statistics")
    plt.savefig(f"players_over_{key}.png")
    os.chdir("..")
    
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    # plot_best_players(url, "ppg")
    # plot_best_players(url, "bpg")
    plot_best_players(url, "rpg")