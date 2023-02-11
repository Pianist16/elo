# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
#pd.set_option('display.max_columns', None)
matches = pd.read_csv('/home/chyngyz/Desktop/tennis/match_scores_1991-2016_unindexed_csv.csv')
matches['year'] = matches['tourney_year_id'].str[:4]
matches = matches.sort_values(by = ['year', 'tourney_order', 'round_order'], ascending = [True, True, False])

winners = matches.filter(['winner_player_id', 'winner_name'])
losers = matches.filter(['loser_player_id', 'loser_name'])

winners.rename(columns={'winner_player_id': 'player_id', 'winner_name': 'player_name'}, inplace = True)
losers.rename(columns={'loser_player_id': 'player_id', 'loser_name': 'player_name'}, inplace = True)
players = pd.concat([winners, losers])
players = players.groupby(['player_id', 'player_name']).count().reset_index()

# initial elo rating before first iteration
elo_init = 1500
players['elo'] = pd.Series([elo_init for x in range(len(players.index))])

# initialize k factors for elo formula
k_low = 40
k_middle = 20
k_high = 10

elo_low = 2100
elo_middle = 2400

del(losers, winners)


matches = matches.filter(['winner_player_id', 'loser_player_id'])


players_elo = pd.DataFrame({'player_id': pd.Series(dtype='str'),
                            'elo': pd.Series(dtype='float')})

w_elo_vec = []
l_elo_vec = []
for i in range(len(matches)):
    
    w_id = matches.iloc[i]['winner_player_id']
    l_id = matches.iloc[i]['loser_player_id']
    
    if w_id in players_elo['player_id'].values:
        w_id_new = 0
        w_elo = players_elo.loc[players_elo['player_id'] == w_id]['elo'].values[0]
    else:
        w_id_new = 1
        w_elo = elo_init
    
    if l_id in players_elo['player_id'].values:
        l_id_new = 0
        l_elo = players_elo.loc[players_elo['player_id'] == l_id]['elo'].values[0]
    else:
        l_id_new = 1
        l_elo = elo_init
    
    w_expect = 1/(1 + 10**((l_elo-w_elo)/400))
    l_expect = 1/(1 + 10**((w_elo-l_elo)/400))
    
    if w_elo < elo_low:
        w_k = k_low
    elif elo_low <= w_elo < elo_middle:
        w_k = k_middle
    else:
        w_k = k_high
    
    if l_elo < elo_low:
        l_k = k_low
    elif elo_low <= w_elo < elo_middle:
        l_k = k_middle
    else:
        l_k = k_high
    
    w_elo = w_elo + w_k * (1 - w_expect)
    l_elo = l_elo + l_k * (0 - l_expect)
    
    if w_id_new == 0:
        players_elo.loc[players_elo['player_id'] == w_id, 'elo'] = w_elo
    else:
        w_id_add = pd.DataFrame([[w_id, w_elo]], columns = ['player_id', 'elo'])
        players_elo = pd.concat([players_elo, w_id_add])
    
    if l_id_new == 0:
        players_elo.loc[players_elo['player_id'] == l_id, 'elo'] = l_elo
    else:
        l_id_add = pd.DataFrame([[l_id, l_elo]], columns = ['player_id', 'elo'])
        players_elo = pd.concat([players_elo, l_id_add])
    
    w_elo_vec.append(w_elo)
    l_elo_vec.append(l_elo)


players_elo = players_elo.merge(players[['player_id', 'player_name']], on = 'player_id')

matches['w_elo'] = w_elo_vec
matches['l_elo'] = l_elo_vec

elo_max = matches.groupby(['winner_player_id'])['w_elo'].max().reset_index()
elo_max = elo_max.merge(players_elo[['player_id', 'player_name']], left_on = 'winner_player_id', right_on = 'player_id', how = 'left')









