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
        break
        

def getMatchScore(url):
    version_tables = imp.pd.read_html(url, match='G A:B')
    results = version_tables[1]["G A:B"]
    total = results.dropna().iloc[-1]  
    print(total)