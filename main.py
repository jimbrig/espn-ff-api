import os
from espn_api.football import League
from dotenv import load_dotenv

load_dotenv()

ESPN_SWID = os.getenv('ESPN_SWID')
ESPN_S2 = os.getenv('ESPN_S2')
ESPN_LEAGUE_ID = os.getenv('ESPN_LEAGUE_ID')
ESPN_TEAM_ID= os.getenv('ESPN_TEAM_ID')
ESPN_SEASON_ID = os.getenv('ESPN_SEASON_ID')

print(f"ESPN_SWID: {ESPN_SWID}")
print(f"ESPN_S2: {ESPN_S2}")
print(f"ESPN_LEAGUE_ID: {ESPN_LEAGUE_ID}")
print(f"ESPN_TEAM_ID: {ESPN_TEAM_ID}")
print(f"ESPN_SEASON_ID: {ESPN_SEASON_ID}")

league = League(league_id=ESPN_LEAGUE_ID, year=2023, espn_s2=ESPN_S2, swid=ESPN_SWID)

teams = league.teams
for team in teams:
    print(f"Team Name: {team.team_name}")
    print(f"Team ID: {team.team_id}")
    print(f"Team Wins: {team.wins}")
    print(f"Team Roster: {team.roster}")
    print("\n")

my_team = league.teams[2]

team_name = my_team.team_name
team_wins = my_team.wins
team_roster = my_team.roster

print(f"Team Name: {team_name}")
print(f"Team Wins: {team_wins}")
print(f"Team Roster: {team_roster}")

players = my_team.roster

for player in players:
    print("---------------------")
    print(f"Player Name: {player.name}")
    print(f"Player ID: {player.playerId}")
    print(f"Player Team: {player.proTeam}")
    print(f"Player Position: {player.position}")
    print(f"Player Rank: {player.posRank}")
    print(f"Player Eligible Positions: {player.eligibleSlots}")
    print(f"Player Acquisition Type: {player.acquisitionType}")
    print("---------------------")
    print("\n")


# free_agents = league.free_agents(size=5)

# qb_free_agents = league.free_agents(size=5, position='QB')

# wr_free_agents = league.free_agents(size=5, position='WR')

# rb_free_agents = league.free_agents(size=5, position='RB')

# league.free_agents()

# draft = league.draft

# settings = league.settings

# power_ranks = league.power_rankings()

# box_scores = league.box_scores()

# activity = league.recent_activity()
