import imports as imp
import KEYS
import game_extraction as ge
import PDF_extraction as pe
import read_tables as rt

imp.session.headers.update({"User-Agent": "Mozilla/5.0"})

#ge.getGames()
#pe.getPDFs()
rt.getTable()
#LIST OF MATCH LINKS FOUND -- WHAT TO DO WITH PDFS NEXT, DOWNLOAD, SCAN, READ?
#ALSO UI
