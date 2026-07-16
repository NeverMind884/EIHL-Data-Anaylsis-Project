import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SearchResults(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)  # Header
        self.rowconfigure(1, weight=0)  # Separator
        self.rowconfigure(2, weight=1)  # Content

        self.results = self.app.state.search_results

        self.create_header()
        self.create_content()

    def create_header(self):

        self.header = ttk.Frame(self)
        self.header.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 0))

        for i in range(3):
            self.header.columnconfigure(i, weight=1)

        def callback():
            print("Click!")

        self.stats_button = ttk.Button(
            self.header,
            text="Stats",
            bootstyle="primary-outline",
            command=callback
        )

        self.my_reports_button = ttk.Button(
            self.header,
            text="All saved reports",
            bootstyle="primary-outline",
            command=callback
        )

        self.stats_button.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.my_reports_button.grid(row=0, column=1, padx=10, pady=(0, 10), sticky="ew")

        # Underline
        ttk.Separator(self, orient=HORIZONTAL).grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 10)
        )

    def create_content(self):

        self.content_area = ttk.Frame(self)
        self.content_area.grid(row=2, column=0, sticky="nsew", padx=10, pady=(50, 10))

        self.content_area.columnconfigure(0, weight=1)
        self.content_area.rowconfigure(0, weight=1)

        self.result_frame = ttk.Labelframe(
            self.content_area,
            text= "Actions",
            padding=10,
            bootstyle="primary"
        )

        self.result_frame.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.result_frame.columnconfigure((0, 1, 2), weight=1)


        self.name_label = ttk.Label(
            self.result_frame,
            text=self.results
        )

        self.view_button = ttk.Button(
            self.result_frame,
            text="View",
            bootstyle="primary-outline"
        )

        self.reports_button = ttk.Button(
            self.result_frame,
            text="Saved Reports",
            bootstyle="primary-outline"
        )

        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.view_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.reports_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")
