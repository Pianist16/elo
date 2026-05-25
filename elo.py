import pandas as pd


def get_expected_score(player_elo, opponent_elo):
    return 1 / (1 + 10 ** ((opponent_elo - player_elo) / 400))


def get_k_factor(
    elo,
    k_low=40,
    k_middle=20,
    k_high=10,
    elo_low=2100,
    elo_middle=2400
):
    if elo < elo_low:
        return k_low
    elif elo_low <= elo < elo_middle:
        return k_middle
    else:
        return k_high


def elo(
    df,
    winner_col,
    loser_col,
    sort_cols=None,
    ascending=True,
    elo_init=1500,
    k_low=40,
    k_middle=20,
    k_high=10,
    elo_low=2100,
    elo_middle=2400
):
    if isinstance(df, str):
        df = pd.read_csv(df)
    else:
        df = df.copy()

    if sort_cols is not None:
        df = df.sort_values(
            by=sort_cols,
            ascending=ascending
        ).reset_index(drop=True)
    else:
        df = df.reset_index(drop=True)

    players_elo = {}

    winner_elo_before_vec = []
    loser_elo_before_vec = []
    winner_elo_after_vec = []
    loser_elo_after_vec = []

    for i in range(len(df)):

        winner_id = df.iloc[i][winner_col]
        loser_id = df.iloc[i][loser_col]

        winner_elo = players_elo.get(winner_id, elo_init)
        loser_elo = players_elo.get(loser_id, elo_init)

        winner_elo_before_vec.append(winner_elo)
        loser_elo_before_vec.append(loser_elo)

        winner_expect = get_expected_score(winner_elo, loser_elo)
        loser_expect = get_expected_score(loser_elo, winner_elo)

        winner_k = get_k_factor(
            winner_elo,
            k_low=k_low,
            k_middle=k_middle,
            k_high=k_high,
            elo_low=elo_low,
            elo_middle=elo_middle
        )

        loser_k = get_k_factor(
            loser_elo,
            k_low=k_low,
            k_middle=k_middle,
            k_high=k_high,
            elo_low=elo_low,
            elo_middle=elo_middle
        )

        winner_elo = winner_elo + winner_k * (1 - winner_expect)
        loser_elo = loser_elo + loser_k * (0 - loser_expect)

        players_elo[winner_id] = winner_elo
        players_elo[loser_id] = loser_elo

        winner_elo_after_vec.append(winner_elo)
        loser_elo_after_vec.append(loser_elo)

    df['winner_elo_before'] = winner_elo_before_vec
    df['loser_elo_before'] = loser_elo_before_vec
    df['winner_elo_after'] = winner_elo_after_vec
    df['loser_elo_after'] = loser_elo_after_vec

    return df


def elo_max(
    df,
    winner_col,
    loser_col,
    winner_elo_col='winner_elo_after',
    loser_elo_col='loser_elo_after',
    winner_name_col=None,
    loser_name_col=None
):
    winner_max = df.groupby(winner_col)[winner_elo_col].max().reset_index()

    winner_max = winner_max.rename(
        columns={
            winner_col: 'player_id',
            winner_elo_col: 'max_elo'
        }
    )

    loser_max = df.groupby(loser_col)[loser_elo_col].max().reset_index()

    loser_max = loser_max.rename(
        columns={
            loser_col: 'player_id',
            loser_elo_col: 'max_elo'
        }
    )

    max_elo = pd.concat([winner_max, loser_max])
    max_elo = max_elo.groupby('player_id')['max_elo'].max().reset_index()

    if winner_name_col is not None and loser_name_col is not None:
        winner_names = df[[winner_col, winner_name_col]].rename(
            columns={
                winner_col: 'player_id',
                winner_name_col: 'player_name'
            }
        )

        loser_names = df[[loser_col, loser_name_col]].rename(
            columns={
                loser_col: 'player_id',
                loser_name_col: 'player_name'
            }
        )

        player_names = pd.concat([winner_names, loser_names]).drop_duplicates()

        max_elo = max_elo.merge(
            player_names,
            on='player_id',
            how='left'
        )

    max_elo = max_elo.sort_values(
        by='max_elo',
        ascending=False
    ).reset_index(drop=True)

    return max_elo