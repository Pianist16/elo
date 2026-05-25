import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

import elo

matches_with_elo = elo.elo(
    df="match_scores_1991-2016_unindexed_csv.csv",
    winner_col="winner_player_id",
    loser_col="loser_player_id",
    sort_cols=["tourney_year_id", "tourney_order", "round_order"],
    ascending=[True, True, False]
)

max_elo = elo.elo_max(
    df=matches_with_elo,
    winner_col="winner_player_id",
    loser_col="loser_player_id",
    winner_name_col="winner_name",
    loser_name_col="loser_name"
)

print(
matches_with_elo[
    (
        matches_with_elo['winner_name'] == 'Roger Federer'
    ) |
    (
        matches_with_elo['loser_name'] == 'Roger Federer'
    )
][[
    'winner_name',
    'loser_name',
    'winner_elo_before',
    'loser_elo_before',
    'winner_elo_after',
    'loser_elo_after'
]].tail(20).to_string(index=False)
)

print()

print(max_elo.head(20))