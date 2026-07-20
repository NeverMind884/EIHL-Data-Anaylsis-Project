from Database import db_connect as db
from Database import match_queries as mq
from Database import league_queries as lq

def getTeamID(team_name):
    sql = "SELECT team_id FROM teams WHERE team_name = %s"

    db.mycursor.execute(sql, (team_name,))
    result = db.mycursor.fetchone()

    if result is None:
        raise ValueError(f"Team '{team_name}' not found.")

    return result[0]

def getTeamName(team_id):
    sql = "SELECT team_name FROM teams WHERE team_id = %s"
    db.mycursor.execute(sql,(team_id,))
    result = db.mycursor.fetchone()
    if result is None:
        raise ValueError(f"Team '{team_id}' not found.")
    
    return result[0]

def searchTeamName(query):
    sql = "SELECT team_name FROM teams WHERE team_name = %s"
    db.mycursor.execute(sql,(query,))
    result = db.mycursor.fetchone()
    #print(result) #Debug
    if result is None:
        raise ValueError(f"Team '{query}' not found.")
    
    return result[0]

def getIdFromTeamName(team_name):
     sql = "SELECT team_id FROM teams WHERE team_name = %s"
     db.mycursor.execute(sql,(team_name,))
     result = db.mycursor.fetchone()
     if result is None:
          raise ValueError(f"Team '{team_name}' not found.")
     
     return result[0]

#working
def teamMatchesInLeague(league_name,team_name):
        league_id = lq.getLeagueID(league_name)
        #print("Print League id: " + str(league_id))
        team_id = getIdFromTeamName(team_name)

        sql = "SELECT * FROM matches WHERE league_id = %s AND (home_team_id = %s OR away_team_id = %s)"

        db.mycursor.execute(sql, (league_id, team_id, team_id))

        result = db.mycursor.fetchall()
        #for row in result :
        #     print(row)
        return result

def teamMatchesInLeagueCount(league_name,team_name):
        total_matches = 0

        matches = teamMatchesInLeague(league_name,team_name)
        for match in matches:
             total_matches += 1
            
        return total_matches

#NOT db query move later
def TeamHomeMatchesInLeague(league_name, team_name):
    league_matches = teamMatchesInLeague(league_name, team_name)
    team_id = getIdFromTeamName(team_name)

    home_matches = []

    for match in league_matches:
        if match[2] == team_id:
            home_matches.append(match)

    return home_matches
               


def homeTeamWins(name):
    sql = "COUNT() "