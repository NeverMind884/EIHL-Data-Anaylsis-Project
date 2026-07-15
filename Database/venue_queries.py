import db_connect as db

def getVenueID(venue_name):
    # Check if venue already exists
    sql = "SELECT venue_id FROM venues WHERE venue_name = %s"

    db.mycursor.execute(sql, (venue_name,))
    result = db.mycursor.fetchone()

    if result:
        return result[0]

    # Venue does not exist, insert it
    insert_sql = "INSERT INTO venues (venue_name) VALUES (%s)"

    db.mycursor.execute(insert_sql, (venue_name,))
    db.mydb.commit()

    return db.mycursor.lastrowid