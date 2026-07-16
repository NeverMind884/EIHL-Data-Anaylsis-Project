from Database import db_connect as db


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
    print(result)
    if result is None:
        raise ValueError(f"Team '{query}' not found.")
    
    return result[0]