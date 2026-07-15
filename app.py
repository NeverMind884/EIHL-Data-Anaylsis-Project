import ttkbootstrap as ttk


class MyApp(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

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

            page = Page(
                self,
                self
            )

            self.pages[name] = page

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )


    def show_page(self, name):

        self.pages[name].tkraise()