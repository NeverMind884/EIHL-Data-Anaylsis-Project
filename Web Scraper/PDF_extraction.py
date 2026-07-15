import imports as imp
import game_extraction as gl

pdf_links = []

def getPDFs():
    

    for link in gl.details_links:

        response = imp.session.get(link)
        response.raise_for_status()
#If the URL is invalid or returns a 4xx/5xx status code, it raises an HTTPError

        soup = imp.BeautifulSoup(response.text, "lxml")

        a = soup.find("a", string=lambda s: s and "Gamesheet" in s)
        if a:
            full_url = a["href"]
            pdf_links.append(full_url)
    
    #response = requests.get(link, headers=headers)
    #response.raise_for_status()

    #firecrawl = Firecrawl(KEYS.api_key)
    #doc = firecrawl.scrape(link, formats=["markdown"])
    #print(doc.markdown)
    print(f"\nFound {len(pdf_links)} PDF links")
    savePDFs()
    
def savePDFs():
    with open("pdf_links.json", 'w') as f:
        imp.json.dump(pdf_links, f, indent=2)
    print("PDF links saved")
