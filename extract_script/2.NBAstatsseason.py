from nba_api.stats.endpoints import leaguegamelog
import pandas as pd
import time

# Define all seasons from 1985-86 to 2024-25
seasons = ['1985-86', '1986-87', '1987-88', '1988-89', '1989-90', '1990-91', '1991-92', '1992-93','1993-94','1994-95',
'1995-96', '1996-97', '1997-98', '1998-99', '1999-00', '2000-01', '2001-02',
'2002-03', '2003-04','2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10','2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16',
'2016-17','2017-18','2018-19','2019-20', '2020-21', '2021-22', '2022-23', '2023-24','2024-25']
# Create an empty list to store data
season_summaries = []

# Loop through all seasons
for season in seasons:
    
    try:
        time.sleep(2)
        # Retrieve data for the given season
        games = leaguegamelog.LeagueGameLog(season=season, season_type_all_star="Regular Season")
        games_df = games.get_data_frames()[0]  # Extract DataFrame

        # Add a season column for reference
        games_df["Season"] = season

        # Append the DataFrame to the list
        season_summaries.append(games_df)

        print(f"Data retrieved for season: {season}")  # Confirmation message

    except Exception as e:
        print(f"Error retrieving data for season {season}: {e}")

# Combine all seasons into a single DataFrame
final_df = pd.concat(season_summaries, ignore_index=True)

# Display column names
print(final_df.columns)

# Display descriptive statistics
print(final_df.describe())
print(final_df.head())
final_df.to_csv("NBA_GameLogs_1985-2025regs.csv", index=False)
print("Data saved to NBA_GameLogs_1985-2025.csv")


