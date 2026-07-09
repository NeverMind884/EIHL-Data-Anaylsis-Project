import tkinter as tk


class MyApp(tk.Frame):

    def __init__(self, root):

        self.colour1 = '#2d5796'
        self.colour2 = '#c82a40'
        self.colour3 = '#9d9b98'
        self.colour4 = '#000000'
        self.colour5 = '#FFFFFF'

        super().__init__(root, bg=self.colour3)

        self.pack(fill=tk.BOTH, expand=True)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)

        self.create_header()
        self.create_content()

    def create_header(self):

        self.header = tk.Frame(
            self,
            bg=self.colour1,
            height=60
        )

        self.header.grid(row=0, column=0, sticky="nsew")
        self.header.grid_propagate(False)

        for i in range(3):
            self.header.columnconfigure(i, weight=1)

        def callback():
            print("click!")

        self.stats_button = tk.Button(self.header, text="Stats", command=callback)
        self.reports_button = tk.Button(self.header, text="Reports", command=callback)
        self.search_button = tk.Button(self.header, text="Search", command=callback)

        self.stats_button.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        self.reports_button.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.search_button.grid(row=0, column=2, sticky="ew", padx=10, pady=10)

    def create_content(self):

        self.content_area = tk.Frame(self, bg=self.colour3)
        self.content_area.grid(row=1, column=0, sticky="nsew")

        self.content_area.columnconfigure(0, weight=1)
        self.content_area.rowconfigure(0, weight=1)
        self.content_area.rowconfigure(1, weight=0)
        self.content_area.rowconfigure(2, weight=1)

        self.card_border = tk.Frame(self.content_area, bg=self.colour2)
        self.card_border.grid(row=1, column=0)

        self.card = tk.Frame(
            self.card_border,
            bg=self.colour5,
            width=480,
            height=290
        )

        self.card.pack(padx=3, pady=3)
        self.card.pack_propagate(False)


# ---- APP START ----

root = tk.Tk()
root.geometry("960x540")
root.resizable(False, False)
root.title("EIHL Stats Tool")

MyApp(root)

root.mainloop()