
import pandas as pd # pandas for aa behandle dataframes

#BPL = British Premier League

BPLurl1 = "https://www.fantrax.com/newui/EPL/statsPlayers.go?isSubmit=y&sId=&sortOrder=SCORING_CATEGORY&sortScId=6340&prevPageNumber=1&pageNumber=&season=918&maxResultsPerPage=100&scKind=NON_GOALIE_STANDARD&position=-2"
BPLurl2 = "https://www.fantrax.com/newui/EPL/statsPlayers.go?isSubmit=y&sId=&sortOrder=SCORING_CATEGORY&sortScId=6340&prevPageNumber=1&pageNumber=2&season=918&maxResultsPerPage=100&scKind=NON_GOALIE_STANDARD&position=-2"
BPLurl3 = "https://www.fantrax.com/newui/EPL/statsPlayers.go?isSubmit=y&sId=&sortOrder=SCORING_CATEGORY&sortScId=6340&prevPageNumber=2&pageNumber=3&season=918&maxResultsPerPage=100&scKind=NON_GOALIE_STANDARD&position=-2"
BPLurl4 = "https://www.fantrax.com/newui/EPL/statsPlayers.go?isSubmit=y&sId=&sortOrder=SCORING_CATEGORY&sortScId=6340&prevPageNumber=3&pageNumber=4&season=918&maxResultsPerPage=100&scKind=NON_GOALIE_STANDARD&position=-2"

BPLtabell1 = pd.read_html(BPLurl1, encoding='utf-8')
BPLtabell2 = pd.read_html(BPLurl2, encoding='utf-8')
BPLtabell3 = pd.read_html(BPLurl3, encoding='utf-8')
BPLtabell4 = pd.read_html(BPLurl4, encoding='utf-8')

#spiller stats side 1
playerStats1 = BPLtabell1[1]
playerStats1_header = playerStats1.iloc[0]
playerStats1 = playerStats1[1:]
playerStats1.columns = playerStats1_header

#spiller stats side 2
playerStats2 = BPLtabell2[1]
playerStats2_header = playerStats2.iloc[0]
playerStats2 = playerStats2[1:]
playerStats2.columns = playerStats2_header

#spiller stats side 3
playerStats3 = BPLtabell3[1]
playerStats3_header = playerStats3.iloc[0]
playerStats3 = playerStats3[1:]
playerStats3.columns = playerStats3_header

#spiller stats side 4
playerStats4 = BPLtabell4[1]
playerStats4_header = playerStats4.iloc[0]
playerStats4 = playerStats4[1:]
playerStats4.columns = playerStats4_header

playerStatsFrames = [playerStats1, playerStats2, playerStats3, playerStats4]
playerStats = pd.concat(playerStatsFrames)
playerStats = playerStats.reset_index(drop=True)

#splitter spillere fra lag
playerTeams = pd.DataFrame(playerStats.Player.str.split(' - ',1).tolist(),
                                   columns = ['Player','Team'])


del playerStats['Player']
stats = pd.merge(playerTeams, playerStats, left_on=playerStats.index,
                 right_on=playerStats.index, left_index=True, right_index=True)

stats.head()

print (stats)
