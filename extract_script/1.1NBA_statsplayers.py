from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# List of player names to search 
player_names = ["LeBron James", "Stephen Curry", "Kevin Durant", "Michael Jordan","Kareem Abdul-Jabbar","Kobe Bryant","Tim Duncan","Larry Bird"]

#Empty list to store DataFrames
dfs = []

# Loop through each player name
for name in player_names:
    
    player_dict = players.find_players_by_full_name(name)
    if player_dict:  # Ensure player was found
        player_id = player_dict[0]['id']
        
        # Retrieve career stats
        career = playercareerstats.PlayerCareerStats(player_id=player_id)
        
        # Convert to DataFrame and store it
        df = career.get_data_frames()[0]
        df["Player"] = name  
        dfs.append(df)

# Combine all player data into a single DataFrame
final_df = pd.concat(dfs, ignore_index=True)

# Display summary
print(final_df.describe())

final_df.to_csv("players_career_stats.csv", index=False)
print("Data saved to players_career_stats.csv")