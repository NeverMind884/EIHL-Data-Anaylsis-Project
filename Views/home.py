import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Home(ttk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        self.create_header()
        self.create_content()


    def create_header(self):

        self.header = ttk.Frame(self)
        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=15,
            pady=(15, 0)
        )

        for i in range(3):
            self.header.columnconfigure(i, weight=1)


        self.stats_button = ttk.Button(
            self.header,
            text="Stats",
            bootstyle="primary-outline",
            command=lambda: self.controller.show_page("stats")
        )


        self.reports_button = ttk.Button(
            self.header,
            text="Reports",
            bootstyle="primary-outline",
            command=lambda: self.controller.show_page("reports")
        )


        self.search_entry = ttk.Entry(
            self.header,
            bootstyle="primary"
        )

        self.search_entry.insert(0, "Search...")


        self.search_entry.bind(
            "<FocusIn>",
            self.clear_search
        )

        self.search_entry.bind(
            "<FocusOut>",
            self.restore_search
        )

        self.search_entry.bind(
            "<Return>",
            self.search
        )


        self.stats_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=(0,10),
            sticky="ew"
        )

        self.reports_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=(0,10),
            sticky="ew"
        )

        self.search_entry.grid(
            row=0,
            column=2,
            padx=10,
            pady=(0,10),
            sticky="ew"
        )


        ttk.Separator(
            self,
            orient=HORIZONTAL
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0,10)
        )


    def clear_search(self, event):

        if self.search_entry.get() == "Search...":
            self.search_entry.delete(0, END)


    def restore_search(self, event):

        if self.search_entry.get() == "":
            self.search_entry.insert(0, "Search...")


    def search(self, event):

        search_text = self.search_entry.get().strip()

        if search_text and search_text != "Search...":
            self.run_search(search_text)


    def run_search(self, query):

        # Save the search value
        self.controller.state.search_query = query

        # Move to results page
        self.controller.show_page("query_results")


    def create_content(self):

        self.content_area = ttk.Frame(self)

        self.content_area.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=10,
            pady=(0,10)
        )


        self.card = ttk.Labelframe(
            self.content_area,
            text="Welcome",
            padding=20,
            width=860,
            height=190,
            bootstyle="primary"
        )

        self.card.grid(
            row=0,
            column=0
        )

        self.card.grid_propagate(False)


        ttk.Label(
            self.card,
            text="This application is my independent data analysis project for the Elite Ice Hockey League (EIHL). It compiles data and generates reports to provide insight into individual matches and each team's performance and progress throughout the season.",
            wraplength=600
        ).pack()