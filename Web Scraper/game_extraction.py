import imports as imp

BASE_URL = "https://www.eliteleague.co.uk"
URL = "https://www.eliteleague.co.uk/schedule?id_season=43&id_team=0&id_month=999"
BASE_PDF_URL = ""
details_links = []

def getGames():
    response = imp.session.get(URL)
    response.raise_for_status()
#If the URL is invalid or returns a 4xx/5xx status code, it raises an HTTPError

    soup = imp.BeautifulSoup(response.text, "html.parser")

    for a in soup.find_all("a", href=True):
        if "Details" in a.text:
            full_url = imp.urljoin(BASE_URL, a["href"])
            details_links.append(full_url)

    print(f"\nFound {len(details_links)} Detail links")