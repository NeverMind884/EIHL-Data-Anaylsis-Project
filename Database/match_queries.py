import db_connect as db

def uploadGames(val):

    sql = "INSERT INTO matches (match_date, home_team_id, away_team_id, match_score, venue_id, league_id) VALUES (%s, %s, %s, %s, %s, %s)"
    db.mycursor.execute(sql, val)
    
    db.mydb.commit()
    
    print(db.mycursor.rowcount, "record inserted.")