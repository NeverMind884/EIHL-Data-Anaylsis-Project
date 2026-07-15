import ttkbootstrap as ttk
from app import MyApp


root = ttk.Window(
    themename="morph"
)

root.geometry("960x540")
root.resizable(False, False)
root.title("EIHL Stats Tool")


app = MyApp(root)

root.mainloop()