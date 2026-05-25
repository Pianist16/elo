# elo

Generic Elo rating system implementation in Python using the pandas library.

The module calculates retrospective Elo ratings from match results supplied in a dataset. It is designed to work with any head-to-head competitive environment where participants compete against each other over time.

The project currently provides two main functions:

- `elo()`  
  Calculates Elo ratings before and after every match.

- `elo_max()`  
  Returns the maximum Elo rating ever achieved by each player.

Although the prototype was tested on a historical tennis dataset, the module is intentionally generic and can be applied to virtually any sport or competitive system.

## Main features

- Generic dataframe-based API
- No hardcoded dataset structure
- Optional chronological sorting
- Configurable Elo parameters
- Match-level Elo history
- Maximum historical Elo summaries

## Technologies used

- Python
- pandas

## Example usage

```python
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
```

## Sample match-level Elo output

```text
winner_name             loser_name              winner_elo_before  loser_elo_before  winner_elo_after  loser_elo_after
Roger Federer           Roberto Bautista Agut             2336.70            2024.63           2339.55           2018.94
Jo-Wilfried Tsonga      Roger Federer                     2129.30            2339.55           2144.70           2324.14
Roger Federer           Alexander Zverev                  2324.14            1875.16           2325.54           1872.36
Dominic Thiem           Roger Federer                     2022.88            2325.54           2056.92           2308.52
Roger Federer           Jan-Lennard Struff                2308.52            1751.96           2309.30           1750.40
```

## Sample maximum Elo output

```text
player_id  max_elo  player_name
d643        2478.81  Novak Djokovic
n409        2406.87  Rafael Nadal
mc10        2403.24  Andy Murray
f324        2369.51  Roger Federer
d683        2256.00  Juan Martin del Potro
f401        2239.79  David Ferrer
w367        2217.80  Stan Wawrinka
n552        2209.62  Kei Nishikori
ba47        2193.43  Tomas Berdych
r975        2186.43  Milos Raonic
```

## Development status

Working prototype completed and tested on a historical ATP tennis dataset.