"""
A simple Poisson-based model for predicting football match outcomes.

This is a well-known, classic approach (not something I invented): goals
scored in a match roughly follow a Poisson distribution, and a team's
attack/defense strength can be estimated from its historical goals
scored/conceded compared to the league average.
"""
import math


def team_strengths(results):
    """
    results: list of dicts with home_team, away_team, home_goals, away_goals
    Returns {team: {"attack": x, "defense": y}}, plus the league's average
    home and away goals per match (1.0 = exactly average).
    """
    teams = {r["home_team"] for r in results} | {r["away_team"] for r in results}

    avg_home_goals = sum(r["home_goals"] for r in results) / len(results)
    avg_away_goals = sum(r["away_goals"] for r in results) / len(results)
    league_avg_goals = (avg_home_goals + avg_away_goals) / 2

    strengths = {}
    for team in teams:
        home_games = [r for r in results if r["home_team"] == team]
        away_games = [r for r in results if r["away_team"] == team]
        games_played = len(home_games) + len(away_games)
        if games_played == 0:
            continue

        goals_scored = sum(r["home_goals"] for r in home_games) + sum(r["away_goals"] for r in away_games)
        goals_conceded = sum(r["away_goals"] for r in home_games) + sum(r["home_goals"] for r in away_games)

        strengths[team] = {
            "attack": (goals_scored / games_played) / league_avg_goals,
            "defense": (goals_conceded / games_played) / league_avg_goals,
        }

    return strengths, avg_home_goals, avg_away_goals


def poisson_prob(k, lam):
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def predict_match(home_team, away_team, strengths, avg_home_goals, avg_away_goals, max_goals=10):
    """Returns (p_home_win, p_draw, p_away_win) using the Poisson model."""
    home, away = strengths[home_team], strengths[away_team]

    expected_home_goals = home["attack"] * away["defense"] * avg_home_goals
    expected_away_goals = away["attack"] * home["defense"] * avg_away_goals

    p_home_win = p_draw = p_away_win = 0.0
    for h in range(max_goals):
        for a in range(max_goals):
            p = poisson_prob(h, expected_home_goals) * poisson_prob(a, expected_away_goals)
            if h > a:
                p_home_win += p
            elif h == a:
                p_draw += p
            else:
                p_away_win += p

    return p_home_win, p_draw, p_away_win
