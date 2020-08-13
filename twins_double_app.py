#!/usr/bin/env python

import datetime
import pytz
import statsapi

TWINS_TEAM_ID = 142

yesterday = (datetime.datetime.now(pytz.timezone("US/Central")) - datetime.timedelta(days=1)).date() 

game_ids = [game['game_id'] for game in statsapi.schedule(date=yesterday, team=TWINS_TEAM_ID)]

# did the twins get any doubles?
DOUBLE = False
for game_id in game_ids:
    boxscore = statsapi.boxscore_data(game_id)

    if boxscore['teamInfo']['away']['id'] == TWINS_TEAM_ID:
        home_or_away = 'away'
    elif boxscore['teamInfo']['home']['id'] == TWINS_TEAM_ID:
        home_or_away = 'home'
    else:
        raise ValueError("Cannot Find TWINs for this game")

    doubles = boxscore[home_or_away]['teamStats']['batting']['doubles']

    if doubles > 0:
        DOUBLE = True
        break

title = "## Did the Twins score a double yesterday?"
if DOUBLE:
    answer = "# Twins scored a double, get some chicken!"
else:
    answer = "# No double, no chicken"

output = '\n'.join([title, answer])

with open("README.md", 'w') as ans:
    ans.write(output)