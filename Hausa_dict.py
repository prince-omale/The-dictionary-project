from tkinter import Tk, Entry, Button, Label, StringVar

window = Tk()
window.geometry("600x250")
window.title("Hausa Dictionary")

entry_text = Entry(window)
entry_text.pack()

result = StringVar()
result_label = Label(window, textvariable=result)
result_label.pack()

hausa_dict = {
   "Aboki": "Friend",
   "Gida" :"House",
   "Makaranta" : "School",
   "Tafiya" :  "Journey",
   "Kasuwa" : "Market",
   "Barka" : "Greeting (used in 'Barka da safe' - Good morning)",
   "Ruwa" : "Water",
   "Hanya" :"Road",
   "Doki" : "Horse",
   "Hausa" : "A Nigerian ethnic group or their language",
   "Kofi" : "Coffee",
   "Littafi" : "Book",
   "Tushen" : "Root",
   "Wata" : "Moon",
   "Gizo" : "Spider",
   "Zuciya" : "Heart",
   "Kare" : "Dog",
   "Iri" :"Seed",
   "Gwamnati" : "Government",
   "Farma": "Farm",
   "Rana" : "Sun or Day",
   "Dare" :"Night",
   "Sana'a" : "Craft or trade",
   "Farko" : "First",
   "Raina" : "My life",
   "Bari" : "Leave or quit",
   "Lafiya" : "Health or Well-being"
}

def search(word):
    if word in hausa_dict:
        result.set(hausa_dict[word])
        print(hausa_dict[word])
    else:
        result.set("Not found")
        print("Not found")

search_btn = Button(window, text="search", command=lambda: search(entry_text.get()))
search_btn.pack()


window.mainloop()