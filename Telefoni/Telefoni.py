from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store_tel.db')


def populate_list(): #za uzimanje podataka
    proizvodjac_list.delete(0, END) #da se ne bi vise puta ucitalo ono sto smo pozvali
    for row in db.fetch():
        proizvodjac_list.insert(END, row) #dodavanje novih na kraj liste


def add_item():
    if proizvodjac_text.get() == '' or model_text.get() == '' or specifikacije_text.get() == '' or cijena_text.get() == '':
        messagebox.showerror('Greška', 'Molimo Vas popunite sva polja.')
        return
    db.insert(proizvodjac_text.get(), model_text.get(), #dodavanje u bazu podataka
              specifikacije_text.get(), cijena_text.get())
    proizvodjac_list.delete(0, END)
    proizvodjac_list.insert(END, (proizvodjac_text.get(), model_text.get(), #dodavanje u listu
                            specifikacije_text.get(), cijena_text.get()))
    clear_text()
    populate_list()


def select_item(event): # da bismo uklonili nesto, moramo da znamo sta selektujemo
    try:
        global selected_item
        index = proizvodjac_list.curselection()[0]
        selected_item = proizvodjac_list.get(index)
            #ovo iznad samo da uzmemo podatke modela koji smo selektovali
        proizvodjac_entry.delete(0, END)
        proizvodjac_entry.insert(END, selected_item[1])
        model_entry.delete(0, END)
        model_entry.insert(END, selected_item[2])
        specifikacije_entry.delete(0, END)
        specifikacije_entry.insert(END, selected_item[3])
        cijena_entry.delete(0, END)
        cijena_entry.insert(END, selected_item[4])
            #ovo iznad kad selektujemo nesto da nam se pokaze u input polja da bismo mogli i da izmijenimo
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], proizvodjac_text.get(), model_text.get(),
              specifikacije_text.get(), cijena_text.get())
    populate_list()


def clear_text(): #brise ono smo smo unijeli u input kad god kliknemo na neko dugme
    proizvodjac_entry.delete(0, END)
    model_entry.delete(0, END)
    specifikacije_entry.delete(0, END)
    cijena_entry.delete(0, END)


# Create window object
app = Tk()


# Proizvođač
proizvodjac_text = StringVar()
proizvodjac_label = Label(app, text='Proizvođač', font=('bold', 14), pady=10, padx=5)
proizvodjac_label.grid(row=0, column=0, sticky=W) # svaki label i input predstavljaju matrice KxI
proizvodjac_entry = Entry(app, textvariable=proizvodjac_text) #input
proizvodjac_entry.grid(row=0, column=1)
# Model
model_text = StringVar()
model_label = Label(app, text='Model', font=('bold', 14))
model_label.grid(row=0, column=2, sticky=W)
model_entry = Entry(app, textvariable=model_text)
model_entry.grid(row=0, column=3)
# Spec
specifikacije_text = StringVar()
specifikacije_label = Label(app, text='Specifikacije', font=('bold', 14), padx=5)
specifikacije_label.grid(row=1, column=0, sticky=W)
specifikacije_entry = Entry(app, textvariable=specifikacije_text)
specifikacije_entry.grid(row=1, column=1)
# Cijena
cijena_text = StringVar()
cijena_label = Label(app, text='Cijena', font=('bold', 14))
cijena_label.grid(row=1, column=2, sticky=W)
cijena_entry = Entry(app, textvariable=cijena_text)
cijena_entry.grid(row=1, column=3)
# proizvodjac List (Listbox)
proizvodjac_list = Listbox(app, height=8, width=50, border=0)
proizvodjac_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
proizvodjac_list.configure(yscrollcommand=scrollbar.set) #postavimo scroll pored liste dolje
scrollbar.configure(command=proizvodjac_list.yview) #skrola po y osi
# Bind select
proizvodjac_list.bind('<<ListboxSelect>>', select_item) #ovo treba za select_item(event)

# Buttons
add_btn = Button(app, text='Dodaj', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Ukloni', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Izmijeni', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Ocisti polja', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('Telefoni')
app.geometry('500x350')
app.configure(bg='#455e87')

# Populate data
populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' proizvodjac_manager.py
# '''
