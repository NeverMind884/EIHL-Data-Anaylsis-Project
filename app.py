import ttkbootstrap as ttk
from appState import AppState
from Database import team_queries as tq
from Database import league_queries as lq
from Database import match_queries as mq
from datetime import datetime

class MyApp(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.state = AppState()

        self.pages = {}

        self.create_pages() 
        self.show_page("home")


    def create_pages(self):

        from Views.home import Home
        from Views.query_results import SearchResults
        from Views.view_team_stats import TeamStats

        pages = {
            "home": Home,
            "search results": SearchResults,
            "view team stats": TeamStats
        }

        for name, Page in pages.items():
            page = Page(parent=self, app=self)

            self.pages[name] = page
            page.grid(row=0, column=0, sticky="nsew")


    def show_page(self, name):
        page = self.pages[name]

        if hasattr(page, "refresh"):
            page.refresh()

        page.tkraise()

    def perform_search(self, query):
        self.state.search_query = query
        self.state.search_results = tq.searchTeamName(query)
        #print(self.state.search_results) #Debug
        self.show_page("search results")

    def load_team_stats(self,team_name):
        self.state.current_league = lq.getcurrLeague()

        self.state.num_league_matches = tq.teamMatchesInLeagueCount(
            self.state.current_league,
            team_name
        )
        print(str(self.state.num_league_matches))

        self.state.home_wins = mq.homeWinCount(
            self.state.current_league,
            team_name
        )
        print(str(self.state.home_wins))

        self.state.away_wins = mq.awayWinCount(
            self.state.current_league,
            team_name
        )
        print(str(self.state.away_wins))
        
        self.show_page("view team stats")

        #if end year is this year and match happened before may th and after august the prior year
        #2025 after august - 2026 may, if curr date before 2026 sep then 2025/26 league