import imports as imp
import PDF_extraction as pe

pdf_links = []

def getTable():

    with open("pdf_links.json", 'r') as f:
        pdf_links = imp.json.load(f)

    for pdf in pdf_links:
        url = pdf
        all_tables = imp.pd.read_html(url)
        print(f"Found {len(all_tables)} tables")

        version_tables = imp.pd.read_html(url, match='G A:B')
        for i, table in enumerate(version_tables):
            print(f"\nTable {i}:")
            print(table.head(4))
        break