"""
Loads a season of results, computes team strengths, and predicts the
outcome probabilities for a match between two of that season's teams.
"""
from data_fetch import get_results
from poisson_model import predict_match, team_strengths


def main():
    results = get_results()
    print(f"Loaded {len(results)} matches")

    strengths, avg_home, avg_away = team_strengths(results)

    print("\nTop 5 attacking teams (1.0 = league average):")
    ranked = sorted(strengths.items(), key=lambda x: -x[1]["attack"])
    for team, s in ranked[:5]:
        print(f"  {team}: attack={s['attack']:.2f}, defense={s['defense']:.2f}")

    # Example: the two strongest attacking teams facing each other
    home_team, away_team = ranked[0][0], ranked[1][0]
    p_home, p_draw, p_away = predict_match(home_team, away_team, strengths, avg_home, avg_away)

    print(f"\n{home_team} (home) vs {away_team} (away)")
    print(f"  Home win: {p_home:.1%}")
    print(f"  Draw:     {p_draw:.1%}")
    print(f"  Away win: {p_away:.1%}")


if __name__ == "__main__":
    main()
