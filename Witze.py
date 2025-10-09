import random
witze=[
    "Warum können skelette so schlecht lügen? - Weil man durch sie hindurchsieht!",
    "Was macht ein Pirat am Computer? - Er drückt die Enter-Taste!",
    "Was ist orange und läuft durch den Wald? - Eine Wanderine!",
    "Warum ging der Pilz auf die Party? - Weil er ein Champignon war!",
]
print("Chatbot gestartet. Tippe 'Witz' oder 'tschüss'.")
while True:
    eingabe=input("Du:")
    if eingabe=="tschüss":
        print("Chatbot: Tschüss, bis bald!")
        break
    elif eingabe=="Witz":
