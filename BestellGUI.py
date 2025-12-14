'''
Einfache Bestell GUI

ToDo:
- Suchleiste
- Warenkorb
- Preise anzeigen
- Bessere Anordnung der Buttons (Grid evtl.)
- Bessere Optik (Farben, Bilder)
- Produkte: Burger; Wraps; 
'''
# Imports
import tkinter as tk
import requests

# Simple in-memory cart: maps item text -> count
cart = {}

def add_to_cart(item_text):
    """Increment count for item_text in the cart."""
    cart[item_text] = cart.get(item_text, 0) + 1
    print(f"Added to cart: {item_text} (total {cart[item_text]})")

def make_cmd(original_fn, item_text):
    """Return a command wrapper that adds item_text to cart then calls original_fn."""
    def _cmd():
        add_to_cart(item_text)
        try:
            original_fn()
        except Exception:
            pass
    return _cmd
# Ausgaben/Defines/Cmds
def bestellung_sushi1():    # Maki Gurke
    print("Nr78")
def bestellung_sushi2():   # Maki Lachs
    print("Nr79")
def bestellung_sushi3():   # Maki Thunfisch
    print("Nr80")
def bestellung_sushi4():   # Nigiri Lachs
    print("Nr81")
def bestellung_sushi5():   # Nigiri Thunfisch
    print("Nr82")
def bestellung_sushi6():   # Sashimi Lachs
    print("Nr83")
def bestellung_sushi7():   # Sashimi Thunfisch
    print("Nr84")
def bestellung_sushi8():   # California Roll
    print("Nr85")
def bestellung_sushi9():   # Tempura Roll
    print("Nr86")
def bestellung_sushi10():  # Dragon Roll
    print("Nr87")
def bestellung_sushi11():  # Inside Out Roll
    print("Nr88")
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
def bestellung_kuchen1():    # Käsekuchen
    print("Nr67")
def bestellung_kuchen2():    # Schokoladenkuchen
    print("Nr68")
def bestellung_kuchen3():    # Apfelkuchen
    print("Nr69")
def bestellung_kuchen4():    # Obsttorte
    print("Nr70")
def bestellung_kuchen5():    # Mohnkuchen
    print("Nr71")
def bestellung_kuchen6():    # Nusskuchen
    print("Nr72")
def bestellung_kuchen7():    # Bienenstich
    print("Nr73")
def bestellung_kuchen8():    # Rüblikuchen
    print("Nr74")
def bestellung_kuchen9():    # Donauwelle
    print("Nr75")
def bestellung_kuchen10():   # Schwarzwälder Kirschtorte
    print("Nr76")
def bestellung_dessert1():   # Tiramisu
    print("Nr32")
def bestellung_dessert2():   # Panna Cotta
    print("Nr33")
def bestellung_dessert3():   # Gelato
    print("Nr34")
def bestellung_desser4():   # Salat
    print("Nr35")
def bestellung_eis1():       # Vanille Eis
    print("Nr36")
def bestellung_eis2():       # Schoko Eis
    print("Nr37")
def bestellung_eis3():       # Stracciatella Eis
    print("Nr38")
def bestellung_eis4():       # Erdbeer Eis
    print("Nr39")
def bestellung_eis5():       # Zitrone Eis
    print("Nr40")
def bestellung_eis6():       # Haselnuss Eis
    print("Nr41")
def bestellung_eis7():       # Karamell Eis
    print("Nr42")
def bestellung_eis8():       # Pistazien Eis
    print("Nr43")
def bestellung_eis9():       # Mango Eis
    print("Nr44")
def bestellung_eis10():      # Kokos Eis
    print("Nr45")
def bestellung_eis11():      # Joghurt Eis
    print("Nr46")
def bestellung_eis12():      # Pistanzien Eis
    print("Nr47")
def bestellung_eis13():      # Blaubeer Eis
    print("Nr48")
def bestellung_eis14():      # Kaffee Eis
    print("Nr49")
def bestellung_eis15():      # Minz Eis
    print("Nr50")
def bestellung_eis16():      # Brownie Eis
    print("Nr51")
def bestellung_eis17():      # Cookie Dough Eis
    print("Nr52")
def bestellung_eis18():      # Butterkeks Eis
    print("Nr53")
def bestellung_eis19():      # Zimt Eis
    print("Nr54")
def bestellung_eis20():      # Honig Eis
    print("Nr55")
def bestellung_pasta1():    # Pasta Carbonara
    print("Nr56")
def bestellung_pasta2():    # Pasta Bolognese
    print("Nr57")
def bestellung_pasta3():    # Pasta Alfredo
    print("Nr58")
def bestellung_pasta4():    # Pasta Pesto
    print("Nr59")
def bestellung_pasta5():    # Pasta Arrabbiata
    print("Nr60")
def bestellung_vorspeise1():  # Bruschetta
    print("Nr61")
def bestellung_vorspeise2():  # Caprese
    print("Nr62")
def bestellung_vorspeise3():  # Antipasti
    print("Nr63")
def bestellung_vorspeise4():  # Suppe
    print("Nr64")
def bestellung_vorspeise5():  # Frühlingsrollen
    print("Nr65")
def bestellung_vorspeise6():  # Sommerrollen
    print("Nr66")
def warenkorb_öffnen():
    warenkorb_fenster = tk.Toplevel(fenster)
    warenkorb_fenster.title("Warenkorb")
    warenkorb_fenster.geometry("320x400")

    frame = tk.Frame(warenkorb_fenster)
    frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    def refresh_list():
        listbox.delete(0, tk.END)
        if not cart:
            listbox.insert(tk.END, "Warenkorb ist leer.")
        else:
            for item, count in cart.items():
                listbox.insert(tk.END, f"{item}  x{count}")

    def send_order():
        try:
            response = requests.post("http://localhost:5000/api/users", json=cart)
            response.raise_for_status() 
            print("Order sent successfully!")
        except requests.exceptions.RequestException as e:
            print(f"Error sending order: {e}")

    # initial populate
    refresh_list()

    btn_frame = tk.Frame(warenkorb_fenster)
    btn_frame.pack(fill=tk.X, padx=8, pady=6)
    refresh_btn = tk.Button(btn_frame, text="Aktualisieren", command=refresh_list)
    refresh_btn.pack(side=tk.LEFT)
    order_btn = tk.Button(btn_frame, text="Bestellen", command=send_order)
    order_btn.pack(side=tk.LEFT, padx=5)
    close_btn = tk.Button(btn_frame, text="Schließen", command=warenkorb_fenster.destroy)
    close_btn.pack(side=tk.RIGHT)
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
# Mouse wheel support (cross-platform)
def _on_mousewheel(event):
    # Linux: event.num == 4 (up), 5 (down)
    if hasattr(event, 'num') and event.num in (4, 5):
        if event.num == 4:
            my_canvas.yview_scroll(-1, "units")
        else:
            my_canvas.yview_scroll(1, "units")
        return

    # Windows and macOS: event.delta is provided
    if hasattr(event, 'delta'):
        delta = event.delta
        # If the delta is large (wheel), convert to steps of 120 per notch
        if abs(delta) >= 120:
            steps = int(abs(delta) / 120)
        else:
            # Small deltas come from trackpad (macOS). Treat them as single-step scrolls.
            steps = 1

        # Determine direction: positive delta means scroll up (typically)
        direction = -1 if delta > 0 else 1
        my_canvas.yview_scroll(direction * steps, "units")
        return

    # Fallback: do nothing
    return

# Bind mouse wheel events to the canvas for all platforms
my_canvas.bind_all("<MouseWheel>", _on_mousewheel)   # Windows and macOS
my_canvas.bind_all("<Button-4>", _on_mousewheel)     # Linux scroll up
my_canvas.bind_all("<Button-5>", _on_mousewheel)     # Linux scroll down
# Texte / Labels
label1 = tk.Label(second_frame, text="Klicke auf die Buttons zur Bestellung", fg="black", font=("Arial", 22, "bold"))
label2 = tk.Label(second_frame, text="Pizzen", font=("", 16))
label3 = tk.Label(second_frame, text="")
label4 = tk.Label(second_frame, text="Getränke", font=("", 16))
label5 = tk.Label(second_frame, text="Desserts", font=("", 16))
label6 = tk.Label(second_frame, text="Eissorten", font=("", 16))
label7 = tk.Label(second_frame, text="Nudelgerichte", font=("", 16))
label8 = tk.Label(second_frame, text="Vorspeisen", font=("", 16))
label9 = tk.Label(second_frame, text="Kuchen", font=("", 16))
label10 = tk.Label(second_frame, text="Sushi", font=("", 16))
# Bestell Buttons
button1 = tk.Button(second_frame, text="Wasser", command=make_cmd(bestellung_getränk1, "Wasser"))
button2 = tk.Button(second_frame, text="Pizza Mageritha", command=make_cmd(bestellung_pizza1, "Pizza Mageritha"))
button3 = tk.Button(second_frame, text="Pizza Salami", command=make_cmd(bestellung_pizza2, "Pizza Salami"))
button4 = tk.Button(second_frame, text="Rucola Pizza", command=make_cmd(bestellung_pizza3, "Rucola Pizza"))
button5 = tk.Button(second_frame, text="Pizza Speciale", command=make_cmd(bestellung_pizza4, "Pizza Speciale"))
button6 = tk.Button(second_frame, text="Pizza Hawai", command=make_cmd(bestellung_pizza5, "Pizza Hawai"))
button7 = tk.Button(second_frame, text="Sprite", command=make_cmd(bestellung_getränk2, "Sprite"))
button8 = tk.Button(second_frame, text="Cola", command=make_cmd(bestellung_getränk3, "Cola"))
button9 = tk.Button(second_frame, text="Fanta", command=make_cmd(bestellung_getränk4, "Fanta"))
button10 = tk.Button(second_frame, text="Eistee", command=make_cmd(bestellung_getränk5, "Eistee"))
button11 = tk.Button(second_frame, text="Apfelsaft", command=make_cmd(bestellung_getränk6, "Apfelsaft"))
button12 = tk.Button(second_frame, text="Mineralwasser", command=make_cmd(bestellung_getränk7, "Mineralwasser"))
button13 = tk.Button(second_frame, text="Orangensaft", command=make_cmd(bestellung_getränk8, "Orangensaft"))
button14 = tk.Button(second_frame, text="Kleiner Kaffee", command=make_cmd(bestellung_getränk9, "Kleiner Kaffee"))
button15 = tk.Button(second_frame, text="Großer Kaffee", command=make_cmd(bestellung_getränk10, "Großer Kaffee"))
button16 = tk.Button(second_frame, text="Tee", command=make_cmd(bestellung_getränk11, "Tee"))
button17 = tk.Button(second_frame, text="Pizza mit Pilzen", command=make_cmd(bestellung_pizza6, "Pizza mit Pilzen"))
button18 = tk.Button(second_frame, text="Pizza mit Schinken", command=make_cmd(bestellung_pizza7, "Pizza mit Schinken"))
button19 = tk.Button(second_frame, text="Pizza Vegetarisch", command=make_cmd(bestellung_pizza8, "Pizza Vegetarisch"))
button20 = tk.Button(second_frame, text="Pizza Funghi", command=make_cmd(bestellung_pizza9, "Pizza Funghi"))
button21 = tk.Button(second_frame, text="Pizza Quattro Stagioni", command=make_cmd(bestellung_pizza10, "Pizza Quattro Stagioni"))
button22 = tk.Button(second_frame, text="Pizza Diavolo", command=make_cmd(bestellung_pizza11, "Pizza Diavolo"))
button23 = tk.Button(second_frame, text="Pizza Prosciutto", command=make_cmd(bestellung_pizza12, "Pizza Prosciutto"))
button24 = tk.Button(second_frame, text="Pizza Tonno", command=make_cmd(bestellung_pizza13, "Pizza Tonno"))
button25 = tk.Button(second_frame, text="Pizza Calzone", command=make_cmd(bestellung_pizza14, "Pizza Calzone"))
button26 = tk.Button(second_frame, text="Pizza Capricciosa", command=make_cmd(bestellung_pizza15, "Pizza Capricciosa"))
button27 = tk.Button(second_frame, text="Pizza Napoli", command=make_cmd(bestellung_pizza16, "Pizza Napoli"))
button28 = tk.Button(second_frame, text="Pizza Romana", command=make_cmd(bestellung_pizza17, "Pizza Romana"))
button29 = tk.Button(second_frame, text="Pizza Siciliana", command=make_cmd(bestellung_pizza18, "Pizza Siciliana"))
button30 = tk.Button(second_frame, text="Pizza Vegetariana", command=make_cmd(bestellung_pizza19, "Pizza Vegetariana"))
button31 = tk.Button(second_frame, text="Pizza Zucchini", command=make_cmd(bestellung_pizza20, "Pizza Zucchini"))
button32 = tk.Button(second_frame, text="Tiramisu", command=make_cmd(bestellung_dessert1, "Tiramisu"))
button33 = tk.Button(second_frame, text="Panna Cotta", command=make_cmd(bestellung_dessert2, "Panna Cotta"))
button34 = tk.Button(second_frame, text="Gelato", command=make_cmd(bestellung_dessert3, "Gelato"))
button35 = tk.Button(second_frame, text="Salat", command=make_cmd(bestellung_desser4, "Salat"))
button36 = tk.Button(second_frame, text="Vanille Eis", command=make_cmd(bestellung_eis1, "Vanille Eis"))
button37 = tk.Button(second_frame, text="Schoko Eis", command=make_cmd(bestellung_eis2, "Schoko Eis"))
button38 = tk.Button(second_frame, text="Stracciatella Eis", command=make_cmd(bestellung_eis3, "Stracciatella Eis"))
button39 = tk.Button(second_frame, text="Erdbeer Eis", command=make_cmd(bestellung_eis4, "Erdbeer Eis"))
button40 = tk.Button(second_frame, text="Zitrone Eis", command=make_cmd(bestellung_eis5, "Zitrone Eis"))
button41 = tk.Button(second_frame, text="Haselnuss Eis", command=make_cmd(bestellung_eis6, "Haselnuss Eis"))
button42 = tk.Button(second_frame, text="Karamell Eis", command=make_cmd(bestellung_eis7, "Karamell Eis"))
button43 = tk.Button(second_frame, text="Pistazien Eis", command=make_cmd(bestellung_eis8, "Pistazien Eis"))
button44 = tk.Button(second_frame, text="Mango Eis", command=make_cmd(bestellung_eis9, "Mango Eis"))
button45 = tk.Button(second_frame, text="Kokos Eis", command=make_cmd(bestellung_eis10, "Kokos Eis"))
button46 = tk.Button(second_frame, text="Joghurt Eis", command=make_cmd(bestellung_eis11, "Joghurt Eis"))
button47 = tk.Button(second_frame, text="Pistanzien Eis", command=make_cmd(bestellung_eis12, "Pistanzien Eis"))
button48 = tk.Button(second_frame, text="Blaubeer Eis", command=make_cmd(bestellung_eis13, "Blaubeer Eis"))
button49 = tk.Button(second_frame, text="Kaffee Eis", command=make_cmd(bestellung_eis14, "Kaffee Eis"))
button50 = tk.Button(second_frame, text="Minz Eis", command=make_cmd(bestellung_eis15, "Minz Eis"))
button51 = tk.Button(second_frame, text="Brownie Eis", command=make_cmd(bestellung_eis16, "Brownie Eis"))
button52 = tk.Button(second_frame, text="Cookie Dough Eis", command=make_cmd(bestellung_eis17, "Cookie Dough Eis"))
button53 = tk.Button(second_frame, text="Butterkeks Eis", command=make_cmd(bestellung_eis18, "Butterkeks Eis"))
button54 = tk.Button(second_frame, text="Zimt Eis", command=make_cmd(bestellung_eis19, "Zimt Eis"))
button55 = tk.Button(second_frame, text="Honig Eis", command=make_cmd(bestellung_eis20, "Honig Eis"))
button56 = tk.Button(second_frame, text="Pasta Carbonara", command=make_cmd(bestellung_pasta1, "Pasta Carbonara"))
button57 = tk.Button(second_frame, text="Pasta Bolognese", command=make_cmd(bestellung_pasta2, "Pasta Bolognese"))
button58 = tk.Button(second_frame, text="Pasta Alfredo", command=make_cmd(bestellung_pasta3, "Pasta Alfredo"))
button59 = tk.Button(second_frame, text="Pasta Pesto", command=make_cmd(bestellung_pasta4, "Pasta Pesto"))
button60 = tk.Button(second_frame, text="Pasta Arrabbiata", command=make_cmd(bestellung_pasta5, "Pasta Arrabbiata"))
button61 = tk.Button(second_frame, text="Bruschetta", command=make_cmd(bestellung_vorspeise1, "Bruschetta"))
button62 = tk.Button(second_frame, text="Caprese", command=make_cmd(bestellung_vorspeise2, "Caprese"))
button63 = tk.Button(second_frame, text="Antipasti", command=make_cmd(bestellung_vorspeise3, "Antipasti"))
button64 = tk.Button(second_frame, text="Suppe", command=make_cmd(bestellung_vorspeise4, "Suppe"))
button65 = tk.Button(second_frame, text="Frühlingsrollen", command=make_cmd(bestellung_vorspeise5, "Frühlingsrollen"))
button66 = tk.Button(second_frame, text="Sommerrollen", command=make_cmd(bestellung_vorspeise6, "Sommerrollen"))
button67 = tk.Button(second_frame, text="Käsekuchen", command=make_cmd(bestellung_kuchen1, "Käsekuchen"))
button68 = tk.Button(second_frame, text="Schokoladenkuchen", command=make_cmd(bestellung_kuchen2, "Schokoladenkuchen"))
button69 = tk.Button(second_frame, text="Apfelkuchen", command=make_cmd(bestellung_kuchen3, "Apfelkuchen"))
button70 = tk.Button(second_frame, text="Obsttorte", command=make_cmd(bestellung_kuchen4, "Obsttorte"))
button71 = tk.Button(second_frame, text="Mohnkuchen", command=make_cmd(bestellung_kuchen5, "Mohnkuchen"))
button72 = tk.Button(second_frame, text="Nusskuchen", command=make_cmd(bestellung_kuchen6, "Nusskuchen"))
button73 = tk.Button(second_frame, text="Bienenstich", command=make_cmd(bestellung_kuchen7, "Bienenstich"))
button74 = tk.Button(second_frame, text="Rüblikuchen", command=make_cmd(bestellung_kuchen8, "Rüblikuchen"))
button75 = tk.Button(second_frame, text="Donauwelle", command=make_cmd(bestellung_kuchen9, "Donauwelle"))
button76 = tk.Button(second_frame, text="Schwarzwälder Kirschtorte", command=make_cmd(bestellung_kuchen10, "Schwarzwälder Kirschtorte"))
button77 = tk.Button(second_frame, text="Maki Gurke", command=make_cmd(bestellung_sushi1, "Maki Gurke"))
button78 = tk.Button(second_frame, text="Maki Lachs", command=make_cmd(bestellung_sushi2, "Maki Lachs"))
button79 = tk.Button(second_frame, text="Maki Thunfisch", command=make_cmd(bestellung_sushi3, "Maki Thunfisch"))
button80 = tk.Button(second_frame, text="Nigiri Lachs", command=make_cmd(bestellung_sushi4, "Nigiri Lachs"))
button81 = tk.Button(second_frame, text="Nigiri Thunfisch", command=make_cmd(bestellung_sushi5, "Nigiri Thunfisch"))
button82 = tk.Button(second_frame, text="Sashimi Lachs", command=make_cmd(bestellung_sushi6, "Sashimi Lachs"))
button83 = tk.Button(second_frame, text="Sashimi Thunfisch", command=make_cmd(bestellung_sushi7, "Sashimi Thunfisch"))
button84 = tk.Button(second_frame, text="California Roll", command=make_cmd(bestellung_sushi8, "California Roll"))
button85 = tk.Button(second_frame, text="Tempura Roll", command=make_cmd(bestellung_sushi9, "Tempura Roll"))
button86 = tk.Button(second_frame, text="Dragon Roll", command=make_cmd(bestellung_sushi10, "Dragon Roll"))
button87 = tk.Button(second_frame, text="Inside Out Roll", command=make_cmd(bestellung_sushi11, "Inside Out Roll"))
# Warenkorb Button
Tbutton1 = tk.Button(text="Warenkorb öffnen", command=warenkorb_öffnen)
# Anordnung
label1.pack()
Tbutton1.pack(side=tk.RIGHT)
label3.pack()
label8.pack()
button61.pack()
button62.pack()
button63.pack()
button64.pack()
button65.pack()
button66.pack()
label7.pack()
button56.pack()
button57.pack()
button58.pack()
button59.pack()
button60.pack()
label10.pack()
button77.pack()
button78.pack()
button79.pack()
button80.pack()
button81.pack()
button82.pack()
button83.pack()
button84.pack()
button85.pack()
button86.pack()
button87.pack()
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
label5.pack()
button32.pack()
button33.pack()
button34.pack()
button35.pack()
label9.pack()
button67.pack()
button68.pack()
button69.pack()
button70.pack()
button71.pack()
button72.pack()
button73.pack()
button74.pack()
button75.pack()
button76.pack()
label6.pack()
button36.pack()
button37.pack()
button38.pack()
button39.pack()
button40.pack()
button41.pack()
button42.pack()
button43.pack()
button44.pack()
button45.pack()
button46.pack()
button47.pack()
button48.pack()
button49.pack()
button50.pack()
button51.pack()
button52.pack()
button53.pack()
button54.pack()
button55.pack()
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
