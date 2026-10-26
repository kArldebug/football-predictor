# Football Match Outcome Predictor

Personal project to practice probability modeling in Python: predicting
football match outcomes (home win / draw / away win) from historical
results, using a classic Poisson goals model.

This is a statistics project, not a betting tool — the output is a
probability estimate based on past performance, nothing more.

## What it does

1. Downloads a season of match results (free public CSV, no API key).
2. Computes each team's attack and defense strength relative to the
   league average, based on goals scored/conceded.
3. Uses those strengths to estimate each team's expected goals in a
   given matchup, then applies a Poisson distribution to turn expected
   goals into win/draw/loss probabilities.
4. Prints the top attacking teams and an example prediction.

## The model, in plain terms

Goals scored in a football match roughly follow a Poisson distribution.
If I know roughly how many goals a team tends to score and concede
compared to the league average, I can estimate the expected goals for
a specific matchup, then compute the probability of every reasonable
scoreline (0-0, 1-0, 2-1, ...) and sum them up into win/draw/loss
probabilities. This is a well-known, classic approach — not something
I invented — but implementing it from scratch was a good way to
actually understand it instead of just reading about it.

## How to run it

```bash
pip install -r requirements.txt
python demo.py
```

By default it uses Premier League 2023/24 data. To try another league
or season, change `DEFAULT_URL` in `data_fetch.py` — football-data.co.uk
hosts the same CSV format for most major European leagues.

## Tests

```bash
python test_poisson_model.py
```

## Limitations

- Doesn't account for injuries, suspensions, or current form — only
  season-long averages.
- Home/away strength is estimated from the same season's data,
  not adjusted for schedule difficulty.
- A good next step would be comparing these probabilities against
  real bookmaker odds, just to see how far off a simple model is from
  the market — purely as a sanity check, not a betting strategy.

## Tech

Python, Pandas
