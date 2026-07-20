import imports as imp
import PDF_extraction as pe
import Database.league_queries as lq
import Database.match_queries as mq
import Database.team_queries as tq
import Database.venue_queries as vq

from datetime import datetime

pdf_links = []

def getTable():

    with open("pdf_links.json", "r") as f:
        pdf_links = imp.json.load(f)

    if pdf_links:
        print("Links retrieved")

    for url in pdf_links:

        match_score = getMatchScore(url)
        home_team, away_team = getHomeAwayTeam(url)
        home_team_id = tq.getTeamID(home_team)
        away_team_id = tq.getTeamID(away_team)
        stadium_name = getStadium(url)
        venue_id = vq.getVenueID(stadium_name)
        match_date = getdate(url)
        league_name = getLeague(url)
        league_id = lq.getOrInsertLeagueID(league_name)

        val = (
            match_date,
            home_team_id,
            away_team_id,
            match_score,
            venue_id,
            league_id
        )

        mq.uploadGames(val)

        

def getMatchScore(url):
    version_tables = imp.pd.read_html(url, match='G A:B')
    results = version_tables[1]["G A:B"]
    total = results.dropna().iloc[-1]  
    return total

def getHomeAwayTeam(url):
    version_tables = imp.pd.read_html(url, match='Home')

    gameData = version_tables[2].head(2)
    home_team = gameData.iloc[0, 2]

    #Removing Home before team name 
    stringArray = home_team.split()
    team = []
    for i in stringArray:
        if i != 'Home':
            team.append(i)
            home = " ".join(team)
    
    away_team = gameData.iloc[0, 3]

    #Removing Visitor before team name 
    stringArray = away_team.split()
    team = []
    for i in stringArray:
        if i != 'Visitor':
            team.append(i)
            away = " ".join(team)
    return home, away

def getStadium(url):
    version_tables = imp.pd.read_html(url, match='Home')
    gameData = version_tables[2].head(2)
    location = gameData.iloc[1, 2]

    #Removing Palce before stadium name 
    stringArray = location.split()
    loc = []
    for i in stringArray:
        if i != 'Place':
            loc.append(i)
            stadium = " ".join(loc)
    return stadium

def getdate(url):
    version_tables = imp.pd.read_html(url, match='Home')
    gameData = version_tables[2].head(2)
    date = gameData.iloc[1, 0]

    date_str = " ".join(
        word.replace(".", "-")
        for word in date.split()
        if word != "Date"
    )
    formatted_date = datetime.strptime(date_str, "%d-%m-%Y").strftime("%Y-%m-%d")
    return formatted_date 

def getLeague(url):
    version_tables = imp.pd.read_html(url, match='EIHL')
    leagueData = version_tables[0].head(1)
    print (leagueData)
    league = leagueData.iloc[0, 1]
    print(league)
    return league