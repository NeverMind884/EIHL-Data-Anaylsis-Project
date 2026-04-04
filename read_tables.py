import imports as imp
import PDF_extraction as pe

pdf_links = []

def getTable():

    with open("pdf_links.json", 'r') as f:
        pdf_links = imp.json.load(f)

    for pdf in pdf_links:
        url = pdf
        #all_tables = imp.pd.read_html(url)
        #print(f"Found {len(all_tables)} tables")

        getMatchScore(url)
        getHomeAwayTeam(url)
        getStadium(url)
        break
        

def getMatchScore(url):
    version_tables = imp.pd.read_html(url, match='G A:B')
    results = version_tables[1]["G A:B"]
    total = results.dropna().iloc[-1]  
    print(total)

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
    print(home)
    away_team = gameData.iloc[0, 3]

    #Removing Visitor before team name 
    stringArray = away_team.split()
    team = []
    for i in stringArray:
        if i != 'Visitor':
            team.append(i)
            away = " ".join(team)
    print(away)

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
    print(stadium)