from Database import db_connect as db
from Database import league_queries as lq
from Database import team_queries as tq
def uploadGames(val):

    sql = "INSERT INTO matches (match_date, home_team_id, away_team_id, match_score, venue_id, league_id) VALUES (%s, %s, %s, %s, %s, %s)"
    db.mycursor.execute(sql, val)
    
    db.mydb.commit()
    
    print(db.mycursor.rowcount, "record inserted.")

def matchesInLeague(league_name):
    league_id = lq.getLeagueID(league_name)

    sql = "SELECT * FROM matches WHERE league_id = %s"
    db.mycursor.execute(sql,(league_id,))
    result = db.mycursor.fetchall()

    if result is None:
        raise ValueError(f"League '{league_name}' not found.")
    
    return result[0]

def homeWinCount(league_name, Team_name): #league specific, get scores separate check 
    print("Home win Count Method Start")
    print(league_name)
    wincount = 0
    Home_matches = tq.TeamHomeMatchesInLeague(league_name, Team_name)
    for game in Home_matches:
        score = str(game[4])
        #print("matche ID: " + str(game[0]))
        home_score, away_score = score.split(":")

        home_score = int(home_score)
        away_score = int(away_score)

        if home_score > away_score:
            wincount += 1

    return wincount

def awayWinCount(league_name, Team_name): #league specific, get scores separate check 
    wincount = 0
    Home_matches = tq.TeamHomeMatchesInLeague(league_name, Team_name)
    for match in Home_matches:
        score = match[4]
        home_score, away_score = score.split(":")

        home_score = int(home_score)
        away_score = int(away_score)

        if  away_score > home_score:
            wincount += 1

    return wincount

def totalWinsInLeague(league_name, Team_name):
    home_wins = homeWinCount(league_name, Team_name)
    away_wins = awayWinCount(league_name, Team_name)
    home_wins = int(home_wins)
    away_wins = int(away_wins)

    totalWins = home_wins + away_wins

    return totalWins
