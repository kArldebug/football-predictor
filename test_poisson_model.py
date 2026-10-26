"""
Basic sanity checks for the Poisson model.
Run with: python test_poisson_model.py
"""
from poisson_model import predict_match, team_strengths


def test_probabilities_sum_close_to_one():
    results = [
        {"home_team": "A", "away_team": "B", "home_goals": 2, "away_goals": 1},
        {"home_team": "B", "away_team": "A", "home_goals": 1, "away_goals": 1},
        {"home_team": "A", "away_team": "B", "home_goals": 3, "away_goals": 0},
        {"home_team": "B", "away_team": "A", "home_goals": 0, "away_goals": 2},
    ]
    strengths, avg_home, avg_away = team_strengths(results)
    p_home, p_draw, p_away = predict_match("A", "B", strengths, avg_home, avg_away)

    total = p_home + p_draw + p_away
    assert 0.95 < total <= 1.0, f"probabilities should sum close to 1, got {total}"


def test_stronger_attack_wins_more_often():
    # Team A scores a lot, team B barely scores - A should be favoured at home
    results = []
    for _ in range(10):
        results.append({"home_team": "A", "away_team": "B", "home_goals": 3, "away_goals": 0})
        results.append({"home_team": "B", "away_team": "A", "home_goals": 0, "away_goals": 3})

    strengths, avg_home, avg_away = team_strengths(results)
    p_home, p_draw, p_away = predict_match("A", "B", strengths, avg_home, avg_away)

    assert p_home > p_away, "the much stronger attacking team should be favoured"


if __name__ == "__main__":
    test_probabilities_sum_close_to_one()
    test_stronger_attack_wins_more_often()
    print("All tests passed.")
