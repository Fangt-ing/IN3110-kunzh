# Assignment6 of IN4100

## Software version

Python 3.9.7

## Packages, install if not existing in your system

* __pandas:__ Install with pip: _pip install pandas_
* __numpy:__ Install with pip: _pip install numpy_
* __matplotlib:__ Install with pip: _pip install matplotlib_
* __python-dateutil:__ Install with pip: _pip install python-dateutil_

## Task 6.2 Regex for filtering URLs

In 

* filter_urls.py containing ```find_urls()``` and ```find_articles()``` functions.
* Six files inside the filter_urls folder containing a list of urls and articles returned for each of the 3 example sites.

## 6.3 Regular Expressions for finnding Dates

In

* collect_dates.py containing the function ```find_dates()```
* Three files inside the collect dates regex folder containing a list of found dates in sorted order for each website given.

## 6.4 Using BeautifulSoup

Modules for this task:
```python3 -m pip install beautifulsoup4```

The functions saves to a markdown file as the following:

#### BETTING SLIP

Date | Venue | Discipline | Who wins?
--- | --- | --- | ---
{ date } | { venue } | { type } |

## 6.6 NBA Player Statistics Season

In this task, the a script fetch_player_statistics.py visits the 2020-2021 NBA playoffs" website on wikipedia (this one: <https://en.wikipedia.org/wiki/2021_NBA_playoffs>) and creates some player statistics.

This task is broken down into three subtasks:

1. Get the list of teams.
2. Given a team url, get the list of players.
3. Given a player url, get their statistics.
As in task 6.4 we will use BeautifulSoup for parsing.

Files delivered in task are as the following:

* fetch_player_stattistics.py
* NBA_player_statistics/players_over_ppg.png
* NBA_player_statistics/players_over_bpg.png
* NBA_player_statistics/players_over_rpg.png

## 6.6 Wiki race with URLs

This task aims to find the match to the end url from the given start url, and records the time taken to for the process.

Files delivered in task are as the following:

* wiki_race_challenge.py
* wiki_race_challenge/shortest_way.txt containing the list of URLs along the shortest path.
