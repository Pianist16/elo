# elo

This project implements an Elo rating system in Python using the pandas library.

The module calculates Elo ratings based on match results supplied in a dataset. The input data contains two main columns:
- winner player ID
- loser player ID

The Elo rating system was originally developed by Hungarian-American physics professor Arpad Elo as a method for estimating the relative skill levels of players in competitive games and sports. Since then, it has become one of the most widely used rating systems across many competitive fields.

Although this prototype was tested on a historical tennis dataset, the algorithm can be applied to virtually any sport or competitive environment where participants compete head-to-head.

## Development status

In development.  
Working prototype completed and tested on the attached tennis dataset.

## Technologies used

- Python
- pandas

## Sample output

```text
   player_id      max_elo            player_name
0       d643  2559.414106         Novak Djokovic
1       mc10  2477.419772            Andy Murray
2       n409  2472.676937           Rafael Nadal
3       f324  2432.117534          Roger Federer
4       n552  2375.928400          Kei Nishikori
5       d683  2366.231193  Juan Martin del Potro
6       w367  2347.226616          Stan Wawrinka
7       r975  2336.578313           Milos Raonic
8       f401  2336.525187           David Ferrer
9       ba47  2329.581955          Tomas Berdych
10      t786  2279.939178     Jo-Wilfried Tsonga
11      c977  2269.593040            Marin Cilic
12      mc65  2265.887853           Gael Monfils
13      g628  2245.940898        Richard Gasquet
14      sa49  2240.517980        Robin Soderling
15      d875  2237.585846        Grigor Dimitrov
16      d402  2236.262770      Nikolay Davydenko
17      s402  2229.824505           Pete Sampras
18      r485  2228.627384           Andy Roddick
19      tb69  2228.411462          Dominic Thiem
```