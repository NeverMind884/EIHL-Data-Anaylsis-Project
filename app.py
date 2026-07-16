import ttkbootstrap as ttk
from appState import AppState
from Database import team_queries as tq

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

        pages = {
            "home": Home,
            "search results": SearchResults,
        }

        for name, Page in pages.items():
            page = Page(parent=self, app=self)

            self.pages[name] = page
            page.grid(row=0, column=0, sticky="nsew")


    def show_page(self, name):

        self.pages[name].tkraise()

    def perform_search(self, query):
        self.state.search_query = query
        self.state.search_results = tq.searchTeamName(query)
        self.show_page("search results")    