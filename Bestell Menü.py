'''
Einfache Bestell GUI
'''
# Imports
import tkinter as tk
# Ausgaben/Defines/Cmds
def bestellung_pizza1():    # Pizza Mageritha
    print("Nr2")
def bestellung_pizza2():    # Pizza mit Salamie
    print("Nr3")
def bestellung_pizza3():    # Pizza mit Rucola
    print("Nr4")
def bestellung_pizza4():    # Pizza Speciale
    print("Nr5")
def bestellung_pizza5():    # Pizza mit Ananas
    print("Nr6")
def bestellung_pizza6():    # Pizza mit Pilzen
    print("Nr17")
def bestellung_pizza7():    # Pizza mit Schinken
    print("Nr18")
def bestellung_pizza8():    # Pizza Vegetarisch
    print("Nr19")
def bestellung_pizza9():    # Pizza Funghi
    print("Nr20")
def bestellung_pizza10():   # Pizza Quattro Stagioni
    print("Nr21")
def bestellung_pizza11():   # Pizza Diavolo
    print("Nr22")
def bestellung_pizza12():   # Pizza Prosciutto
    print("Nr23")
def bestellung_pizza13():   # Pizza Tonno
    print("Nr24")
def bestellung_pizza14():   # Pizza Calzone
    print("Nr25")
def bestellung_pizza15():   # Pizza Capricciosa
    print("Nr26")
def bestellung_pizza16():   # Pizza Napoli
    print("Nr27")
def bestellung_pizza17():   # Pizza Romana
    print("Nr28")
def bestellung_pizza18():   # Pizza Siciliana
    print("Nr29")
def bestellung_pizza19():   # Pizza Vegetariana
    print("Nr30")
def bestellung_pizza20():   # Pizza Zucchini
    print("Nr31")
def bestellung_getränk1():  # Wasser
    print("Nr1")
def bestellung_getränk2():  # Sprite
    print("Nr7")
def bestellung_getränk3():  # Cola
    print("Nr8")
def bestellung_getränk4():  # Fanta
    print("Nr9")
def bestellung_getränk5():  # Eistee
    print("Nr10")
def bestellung_getränk6():  # Apfelsaft
    print("Nr11")
def bestellung_getränk7():  # Mineralwasser
    print("Nr12")
def bestellung_getränk8():  # Orangensaft
    print("Nr13")
def bestellung_getränk9():  # Kleiner Kaffe
    print("Nr14")
def bestellung_getränk10(): # Großer Kaffee
    print("Nr15")
def bestellung_getränk11(): # Tee
    print("Nr16")
# Fenster
fenster = tk.Tk()
fenster.title("Bestellungen")
fenster.geometry("450x600")
# Scrollbar
main_frame = tk.Frame(fenster)
main_frame.pack(fill=tk.BOTH, expand=1)
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
my_scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
second_frame = tk.Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")
# Texte / Labels
label1 = tk.Label(second_frame, text="Klicke auf die Buttons zur Bestellung", fg="black", font=("Arial", 22, "bold"))
label2 = tk.Label(second_frame, text="Pizzen", font=("", 16))
label3 = tk.Label(second_frame, text="")
label4 = tk.Label(second_frame, text="Getränke", font=("", 16))
# Buttons
button1 = tk.Button(second_frame, text="Wasser", command=bestellung_getränk1)
button2 = tk.Button(second_frame, text="Pizza Mageritha", command=bestellung_pizza1)
button3 = tk.Button(second_frame, text="Pizza Salami", command=bestellung_pizza2)
button4 = tk.Button(second_frame, text="Rucola Pizza", command=bestellung_pizza3)
button5 = tk.Button(second_frame, text="Pizza Speciale", command=bestellung_pizza4)
button6 = tk.Button(second_frame, text="Pizza Hawai", command=bestellung_pizza5)
button7 = tk.Button(second_frame, text="Sprite", command=bestellung_getränk2)
button8 = tk.Button(second_frame, text="Cola", command=bestellung_getränk3)
button9 = tk.Button(second_frame, text="Fanta", command=bestellung_getränk4)
button10 = tk.Button(second_frame, text="Eistee", command=bestellung_getränk5)
button11 = tk.Button(second_frame, text="Apfelsaft", command=bestellung_getränk6)
button12 = tk.Button(second_frame, text="Mineralwasser", command=bestellung_getränk7)
button13 = tk.Button(second_frame, text="Orangensaft", command=bestellung_getränk8)
button14 = tk.Button(second_frame, text="Kleiner Kaffee", command=bestellung_getränk9)
button15 = tk.Button(second_frame, text="Großer Kaffee", command=bestellung_getränk10)
button16 = tk.Button(second_frame, text="Tee", command=bestellung_getränk11)
button17 = tk.Button(second_frame, text="Pizza mit Pilzen", command=bestellung_pizza6)
button18 = tk.Button(second_frame, text="Pizza mit Schinken", command=bestellung_pizza7)
button19 = tk.Button(second_frame, text="Pizza Vegetarisch", command=bestellung_pizza8)
button20 = tk.Button(second_frame, text="Pizza Funghi", command=bestellung_pizza9)
button21 = tk.Button(second_frame, text="Pizza Quattro Stagioni", command=bestellung_pizza10)
button22 = tk.Button(second_frame, text="Pizza Diavolo", command=bestellung_pizza11)
button23 = tk.Button(second_frame, text="Pizza Prosciutto", command=bestellung_pizza12)
button24 = tk.Button(second_frame, text="Pizza Tonno", command=bestellung_pizza13)
button25 = tk.Button(second_frame, text="Pizza Calzone", command=bestellung_pizza14)
button26 = tk.Button(second_frame, text="Pizza Capricciosa", command=bestellung_pizza15)
button27 = tk.Button(second_frame, text="Pizza Napoli", command=bestellung_pizza16)
button28 = tk.Button(second_frame, text="Pizza Romana", command=bestellung_pizza17)
button29 = tk.Button(second_frame, text="Pizza Siciliana", command=bestellung_pizza18)
button30 = tk.Button(second_frame, text="Pizza Vegetariana", command=bestellung_pizza19)
button31 = tk.Button(second_frame, text="Pizza Zucchini", command=bestellung_pizza20)
# Anordnung
label1.pack()
label3.pack()
label2.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button17.pack()
button18.pack()
button19.pack()
button20.pack()
button21.pack()
button22.pack()
button23.pack()
button24.pack()
button25.pack()
button26.pack()
button27.pack()
button28.pack()
button29.pack()
button30.pack()
button31.pack()
label4.pack()
button1.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
button13.pack()
button14.pack()
button15.pack()
button16.pack()
#Fenster Code wiederhohlen lassen (alles bis hier)
fenster.mainloop()
