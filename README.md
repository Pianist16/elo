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
       winner_name            loser_name  winner_elo_before  loser_elo_before  winner_elo_after  loser_elo_after
     Roger Federer Roberto Bautista Agut        2336.700518       2024.629081       2339.546247      2018.937621
Jo-Wilfried Tsonga         Roger Federer        2129.295828       2339.546247       2144.702864      2324.139212
     Roger Federer      Alexander Zverev        2324.139212       1875.160922       2325.542030      1872.355285
     Dominic Thiem         Roger Federer        2022.876648       2325.542030       2056.915715      2308.522496
     Roger Federer    Jan-Lennard Struff        2308.522496       1751.958375       2309.302925      1750.397517
```

## Sample maximum Elo output

```text
player_id      max_elo            player_name
d643         2478.811170         Novak Djokovic
n409         2406.871068           Rafael Nadal
mc10         2403.243420            Andy Murray
f324         2369.511314          Roger Federer
d683         2256.000005  Juan Martin del Potro
f401         2239.786477           David Ferrer
w367         2217.797230          Stan Wawrinka
n552         2209.618646          Kei Nishikori
ba47         2193.427780          Tomas Berdych
r975         2186.429946           Milos Raonic
```

## Development status

Working prototype completed and tested on a historical ATP tennis dataset.