import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class TeamStats(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app
        self.state = app.state

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        # AppState values
        self.results = self.state.search_results
        self.league_name = self.state.current_league

        self.create_header()
        self.create_content()


    def refresh(self):

        # Reload AppState
        self.results = self.state.search_results
        self.league_name = self.state.current_league


        # Update team name
        self.name_label.config(
            text=self.results
        )


        # Update league name
        self.league_Labelframe.config(
            text="Overall Stats: " + self.league_name
        )


        # Update stats
        self.total_games_Label.config(
            text="Matches Played: " + str(self.state.num_league_matches)
        )

        self.h_wins_Label.config(
            text="Home Wins: " + str(self.state.home_wins)
        )

        self.a_wins_Label.config(
            text="Away Wins: " + str(self.state.away_wins)
        )


    def create_header(self):

        self.header = ttk.Frame(self)

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=15,
            pady=(15, 0)
        )


        self.header.columnconfigure(0, weight=1)
        self.header.columnconfigure(1, weight=1)


        self.name_label = ttk.Label(
            self.header,
            text=self.results,
            font=("Segoe UI", 14, "bold"),
            anchor="center"
        )


        self.home_button = ttk.Button(
            self.header,
            text="Home",
            bootstyle="primary-outline",
            command=lambda: self.app.show_page("home")
        )


        self.name_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="ew"
        )


        self.home_button.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )


        ttk.Separator(
            self,
            orient=HORIZONTAL
        ).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15
        )


    def create_content(self):

        self.content_area = ttk.Frame(self)

        self.content_area.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )


        self.content_area.columnconfigure(0, weight=1)
        self.content_area.rowconfigure(0, weight=1)


        self.league_Labelframe = ttk.Labelframe(
            self.content_area,
            text="Overall Stats: " + str(self.league_name),
            padding=10,
            bootstyle="primary"
        )


        self.league_Labelframe.grid(
            row=0,
            column=0,
            sticky="nsew"
        )


        self.league_Labelframe.columnconfigure(0, weight=3)
        self.league_Labelframe.columnconfigure(1, weight=1)
        self.league_Labelframe.rowconfigure(0, weight=1)



        self.chart_Labelframe = ttk.Labelframe(
            self.league_Labelframe,
            text="Charts",
            padding=10,
            bootstyle="primary"
        )


        self.info_Labelframe = ttk.Labelframe(
            self.league_Labelframe,
            text="Stats Info",
            padding=10,
            bootstyle="primary"
        )


        self.chart_Labelframe.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )


        self.info_Labelframe.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=5,
            pady=5
        )


        # Statistics labels

        self.total_games_Label = ttk.Label(
            self.info_Labelframe,
            text="Matches Played: 0",
            padding=10
        )


        self.h_wins_Label = ttk.Label(
            self.info_Labelframe,
            text="Home Wins: 0",
            padding=10
        )


        self.a_wins_Label = ttk.Label(
            self.info_Labelframe,
            text="Away Wins: 0",
            padding=10
        )


        self.total_games_Label.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.h_wins_Label.grid(
            row=1,
            column=0,
            sticky="w"
        )

        self.a_wins_Label.grid(
            row=2,
            column=0,
            sticky="w"
        )