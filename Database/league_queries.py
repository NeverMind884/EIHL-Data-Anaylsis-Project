from Database import db_connect as db

def getOrInsertLeagueID(league_name): 
    # Check if tournament already exists
    league_id = getLeagueID(league_name)

    if league_id:
        return league_id

    # Tournament does not exist, insert it
    insert_sql = "INSERT INTO tournament (league_name) VALUES (%s)"

    db.mycursor.execute(insert_sql, (league_name,))
    db.mydb.commit()

    return db.mycursor.lastrowid

def getLeagueID(league_name): 
    # Check if tournament already exists
    sql = "SELECT league_id FROM tournament WHERE league_name = %s"

    db.mycursor.execute(sql, (league_name,))
    result = db.mycursor.fetchone()

    if result:
        return result[0]
    
    return None

def getLeagueFromDate(date):
    print(date)
    sql = "SELECT league_name FROM tournament WHERE %s BETWEEN league_start_date AND league_end_date"
    db.mycursor.execute(sql, (date,))
    result = db.mycursor.fetchone()
    if result is None:
        raise ValueError(f"Team '{date}' not found.")
    print(result)
    return result[0]

def getcurrLeague():
    sql = "SELECT league_id FROM matches ORDER BY match_date DESC LIMIT 1"
    db.mycursor.execute(sql)
    result = db.mycursor.fetchone()
    league_id = result[0]

    sql2 = "SELECT league_name FROM tournament WHERE league_id = %s"
    db.mycursor.execute(sql2,(league_id,))
    currLeague = db.mycursor.fetchone()

    return currLeague[0]