# Assignment5 of IN4100

## Software version

Python 3.9.7

## Task 5.1

* manual_timing_.py runs the test of functions from test_slow_rectangle.py, each function is runned for 5 times. The time consumed by each run of coresponding function is saved to manual_report.txt.

* timeit_timing_.py runs the test of functions from test_slow_rectangle.py, each function is runned for 5 times.  In the meantime, it compares the time of coresponding function at each round to the ones in manual_timing_.py. The time consumed by each run of coresponding function and comparisons are saved to timeit_report.txt.

* cProfile_timing_.py compares the slowest function runned by using 2 different menthod defined in manual_timing_.py and timeit_timing_.py. Sata is saved to cProfile_report.txt.

Modules for this section:

```python
python3 -m pip install requests
```

## Task 5.2 Regex for filtering URLs

In this task, filter urls.py was created for finding urls in a body of html
using regex. ```find_urls``` receives a string of html and returns a list of all urls found in the text.

Files delivered in this taks are as the following:

* The urls:
  * <https://en.wikipedia.org/wiki/Nobel_Prize>
  * <https://en.wikipedia.org/wiki/Bundesliga>
  * <https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup>

* filter_urls.py containing ```find_urls()``` and ```find_articles()``` functions.
* Six files inside the filter_urls folder containing a list of urls and articles returned for each of the 3 example sites.

## 5.3 Regular Expressions for finnding Dates

In this task, functions were made for finnding "dates" in a body of html using regex. The script named collect_dates.py that includes a function ```find_dates()``` that receives a string of html and returns a list of all dates found in the text.

Files delivered:

* collect_dates.py containing the function ```find_dates()```
* Three files inside the collect dates regex folder containing a list of found dates in sorted order for each website given.

## 5.4 Using BeautifulSoup

Modules for this task:
```python3 -m pip install beautifulsoup4```

The functions saves to a markdown file as the following:

#### BETTING SLIP

Date | Venue | Discipline | Who wins?
--- | --- | --- | ---
{ date } | { venue } | { type } |

## 5.5 NBA Player Statistics Season

In this task, the a script fetch_player_statistics.py visits the 2020-2021 NBA playoffs" website on wikipedia (this one: <https://en.wikipedia.org/wiki/2021_NBA_playoffs>) and creates some player statistics.

This task is broken down into three subtasks:

1. Get the list of teams.
2. Given a team url, get the list of players.
3. Given a player url, get their statistics.
As in task 5.4 we will use BeautifulSoup for parsing.

Files delivered in task are as the following:

* fetch_player_stattistics.py
* NBA_player_statistics/players_over_ppg.png
* NBA_player_statistics/players_over_bpg.png
* NBA_player_statistics/players_over_rpg.png

## 5.6 Wiki race with URLs

This task aims to find the match to the end url from the given start url, and records the time taken to for the process.

Files delivered in task are as the following:

* wiki_race_challenge.py
* wiki_race_challenge/shortest_way.txt containing the list of URLs along the shortest path.
