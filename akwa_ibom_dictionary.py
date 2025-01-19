from tkinter import Tk, Entry, Button, Label, StringVar, Toplevel

window = Tk()
window.geometry("600x250")
window.title("EFIIK Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

efik_dict = {
    "Good Morning" : "Amesiere",
    "Come and eat" : "Di dia nkpo",
    "welcome" : "Amedio",
    "close the door" : "Bet usong",
    "write it " : "Wet nkpo",
    "open your eye" : "Tat enyin",
    "Close your mouth" : "Kop inua",
    "Thank you" : "Sosongo",
    "Come and sleep" : "Di ke dede",
    "Wash your hand" : "Yet ubok",
    "Ten" : "Doup",
    "What is it?" : "Nsidoro",
    "How many book" : "Nwed ifang",
    "Who are you" : "Afo do anie",
    "Give me water" : "Kod mmori nsok",
    "Help me" : "Di nyariga",
    "God is good" : "Abasi afom",
    "Is beautiful" : "Ayaya",
    "Wake up" : "Demere",
    "Sweep" : "Kwok isong"
}
def search(word):
    if word in efik_dict:
        result.set(efik_dict[word])
        print(efik_dict[word])
    else:
        result.set("Not Found")
        print("Not Found")

search_btn = Button(window, text="search", command=lambda: search(entry_text.get()))
search_btn.pack()

window.mainloop()