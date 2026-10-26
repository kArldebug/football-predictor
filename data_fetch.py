"""
Downloads a season of match results from football-data.co.uk — free,
public CSVs, no API key needed.
"""
import pandas as pd

# Premier League, 2023/24 season. Other leagues/seasons follow the same
# pattern, e.g. E0 = Premier League, SP1 = La Liga, I1 = Serie A, F1 = Ligue 1.
DEFAULT_URL = "https://www.football-data.co.uk/mmz4281/2324/E0.csv"


def get_results(url=DEFAULT_URL):
    df = pd.read_csv(url)
    results = []
    for _, row in df.iterrows():
        if pd.isna(row.get("FTHG")) or pd.isna(row.get("FTAG")):
            continue
        results.append({
            "home_team": row["HomeTeam"],
            "away_team": row["AwayTeam"],
            "home_goals": int(row["FTHG"]),
            "away_goals": int(row["FTAG"]),
        })
    return results


if __name__ == "__main__":
    results = get_results()
    print(f"Loaded {len(results)} matches")
    print(results[0])
