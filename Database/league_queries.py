import db_connect as db

def getLeagueID(league_name):
    # Check if tournament already exists
    sql = "SELECT league_id FROM tournament WHERE league_name = %s"

    db.mycursor.execute(sql, (league_name,))
    result = db.mycursor.fetchone()

    if result:
        return result[0]

    # Tournament does not exist, insert it
    insert_sql = "INSERT INTO tournament (league_name) VALUES (%s)"

    db.mycursor.execute(insert_sql, (league_name,))
    db.mydb.commit()

    return db.mycursor.lastrowid