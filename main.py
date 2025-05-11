import webbrowser
import time

brave_path = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"

webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path))

siteler = [
    "about:blank",
    "https://www.youtube.com",
    "https://www.instagram.com",
    "https://www.udemy.com",
]

for site in siteler:
    webbrowser.get("brave").open_new_tab(site)








