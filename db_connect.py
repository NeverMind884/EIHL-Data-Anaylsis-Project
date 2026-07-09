import mysql.connector
import KEYS

mydb = mysql.connector.connect(host="localhost", user="root", passwd=KEYS.pass_key, database="eihl")
mycursor = mydb.cursor()

def uploadGames(val):

    sql = "INSERT INTO matches (match_date, home_team_id, away_team_id, match_score, venue_id, league_id) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(sql, val)
    
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted.")


def getTeamID(team_name):
    sql = "SELECT team_id FROM teams WHERE team_name = %s"

    mycursor.execute(sql, (team_name,))
    result = mycursor.fetchone()

    if result is None:
        raise ValueError(f"Team '{team_name}' not found.")

    return result[0]

def getVenueID(venue_name):
    # Check if venue already exists
    sql = "SELECT venue_id FROM venues WHERE venue_name = %s"

    mycursor.execute(sql, (venue_name,))
    result = mycursor.fetchone()

    if result:
        return result[0]

    # Venue does not exist, insert it
    insert_sql = "INSERT INTO venues (venue_name) VALUES (%s)"

    mycursor.execute(insert_sql, (venue_name,))
    mydb.commit()

    return mycursor.lastrowid

def getLeagueID(league_name):
    # Check if tournament already exists
    sql = "SELECT league_id FROM tournament WHERE league_name = %s"

    mycursor.execute(sql, (league_name,))
    result = mycursor.fetchone()

    if result:
        return result[0]

    # Tournament does not exist, insert it
    insert_sql = "INSERT INTO tournament (league_name) VALUES (%s)"

    mycursor.execute(insert_sql, (league_name,))
    mydb.commit()

    return mycursor.lastrowid