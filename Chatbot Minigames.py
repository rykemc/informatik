


print("Chatbot: Guten Tag, willst du meine Zahl erraten oder einen Witz hören?")
print("Schreibe dazu entweder 'Zahl' oder 'Witz'.")
while True:
    eingabe=input("Du: ")
    if eingabe=="Zahl":
        import random
        print("Chatbot: Ich denke mir eine Zahl von 1 bis 100. Rate sie!")
        geheim=random.randint(1,100)
        while True:
            versuch=int(input("Dein Tipp: "))
            if versuch==geheim:
                print("Chatbot:Glückwunsch, du hast die Zahl erraten!")
                break
            elif versuch==0:
              print("Schreibe 'Zahl' um eine Zahl zwischen 1 und 100 zu erraten, oder 'Witz' um einen Witz zu hören.")
              break
            else:
                print("Chatbot: Falsch, versuch es nochmal!")
    elif eingabe=="Witz":
        import random
        witze=[
            "Warum können Skelette so schlecht lügen? - Weil man durch sie hindurchsieht!",
            "Was macht ein Pirat am Computer? - Er drückt die Enter-Taste!",
            "Was ist orange und läuft durch den Wald? - Eine Wanderine!",
            "Warum ging der Pilz auf die Party? - Weil er ein Champignon war!",
            "Warum dürfen Geister keine Lügen erzählen? - Weil sie durchschaut werden!",
            "Was macht ein Keks unter einem Baum? - Krümel!",
            "Warum können Elefanten nicht fliegen? - Weil sie zu schwer für den Flugzeug sind!",
            "Was ist grün und klopft an die Tür? - Ein Klopfsalat!",
            "Warum können Bienen so gut rechnen? - Weil sie den Honig aufsummieren!",
            "Was macht ein Mathematiker im Garten? - Wurzeln ziehen!",
            "Warum war der Computer kalt? - Weil er Windows offen hatte!",
            "Was ist der Lieblingstanz von Elektrikern? - Der Stromboli!",
            "Warum können Katzen so gut singen? - Weil sie Miau-sik lieben!",
            "Was macht ein Pirat am Computer? - Er drückt die Enter-Taste!",
            "Warum ging der Pilz auf die Party? - Weil er ein Champignon war!",
            "Was ist rot und steht im Wald? - Ein Kirsch!",
            "Warum können Fische so schlecht Mathe? - Weil sie immer in den Netzen hängen!",
            "Was macht ein Schaf auf dem Tennisplatz? - Es spielt Wolle!",
            "Warum sind Spaghetti so geheimnisvoll? - Weil sie immer im Verborgenen kochen!",
            "Was ist gelb und kann nicht schwimmen? - Ein Bagger!",
            "Warum können Kühe nicht tanzen? - Weil sie immer aus der Reihe muhen!",
            "Was macht ein U-Boot im Wald? - Bäume tauchen!",
            "Warum sind Geister schlechte Lügner? - Weil man durch sie hindurchsieht!",
            "Was ist braun und läuft durch den Wald? - Ein Keks!",
            "Warum können Vögel so gut rechnen? - Weil sie Pi-pi-pi machen!",
            "Was macht ein Hund am Computer? - Er klickt auf den Knochen!",
            "Warum sind Mathematiker schlechte Gärtner? - Weil sie nur Wurzeln ziehen!",
            "Was ist blau und liegt im Wald? - Eine Blaubeere!",
            "Warum können Frösche so gut hüpfen? - Weil sie immer einen Sprung voraus sind!",
            "Was macht ein Elefant im Kühlschrank? - Platz!",
            "Warum sind Bananen nie einsam? - Weil sie immer in einer Schale sind!",
            "Was ist grün und läuft durch den Wald? - Ein Jäger!",
            "Warum können Mäuse so gut tanzen? - Weil sie immer auf dem Käse stehen!",
            "Was macht ein Fisch im Weltall? - Sternflossen!",
            "Warum sind Computer schlecht im Schwimmen? - Weil sie immer abstürzen!",
            "Was ist orange und läuft durch den Wald? - Eine Wanderine!",
            "Warum können Pilze so gut feiern? - Weil sie immer einen Champignon haben!",
            "Was macht ein Vogel im Fitnessstudio? - Flügeltraining!",
            "Warum sind Bücher so schlau? - Weil sie viele Seiten haben!",
            "Was ist schwarz-weiß und hüpft durch den Dschungel? - Ein Springuin!",
            "Warum können Enten so gut schwimmen? - Weil sie immer eine Ente haben!",
            "Was macht ein Löwe im Büro? - Brüllen!",
            "Warum sind Giraffen so groß? - Damit sie den Überblick behalten!",
            "Was ist rot und läuft durch den Wald? - Eine Tomate!",
            "Warum können Affen so gut klettern? - Weil sie immer einen Ast haben!",
            "Was macht ein Frosch auf der Straße? - Quak!",
            "Warum sind Schildkröten so langsam? - Weil sie ihr Haus immer dabei haben!",
            "Was ist gelb und steht im Wald? - Eine Banane!",
            "Warum können Ameisen so gut arbeiten? - Weil sie immer im Team sind!",
            "Was macht ein Pferd im Kino? - Popcorn essen!",
            "Warum sind Zebras gestreift? - Damit sie nicht übersehen werden!",
            "Was ist grün und fliegt durch die Luft? - Eine Fliege!",
            "Warum können Schafe so gut schlafen? - Weil sie immer zählen!",
            "Was macht ein Hase im Supermarkt? - Möhren kaufen!",
            "Warum sind Pinguine so elegant? - Weil sie immer im Frack sind!",
            "Was ist braun und sitzt auf dem Baum? - Ein Affe!",
            "Warum können Eichhörnchen so gut klettern? - Weil sie immer eine Nuss haben!",
            "Was macht ein Bär im Winter? - Schlafen!",
            "Warum sind Löwen so mutig? - Weil sie immer brüllen!",
            "Was ist blau und schwimmt im Meer? - Ein Blauwal!",
            "Warum können Delfine so gut springen? - Weil sie immer einen Sprung machen!",
            "Was macht ein Fuchs im Wald? - Schleichen!",
            "Warum sind Eulen so klug? - Weil sie immer nachdenken!",
            "Was ist rot und fliegt durch die Luft? - Ein Fliegender Teppich!",
            "Warum können Kängurus so gut hüpfen? - Weil sie immer einen Beutel haben!",
            "Was macht ein Schmetterling im Garten? - Blumen besuchen!",
            "Warum sind Bienen so fleißig? - Weil sie immer arbeiten!",
            "Was ist gelb und läuft durch den Wald? - Eine Zitrone!",
            "Warum können Hühner so gut gackern? - Weil sie immer ein Ei legen!",
            "Was macht ein Schwein im Schlamm? - Suhlen!",
            "Warum sind Kühe so ruhig? - Weil sie immer wiederkäuen!",
            "Was ist grün und sitzt auf dem Fensterbrett? - Eine Fensterbank!",
            "Warum können Schlangen so gut kriechen? - Weil sie keine Beine haben!",
            "Was macht ein Adler in den Bergen? - Fliegen!",
            "Warum sind Mäuse so flink? - Weil sie immer rennen!",
            "Was ist braun und läuft durch die Wüste? - Ein Kamel!",
            "Warum können Kamele so gut Wasser speichern? - Weil sie immer einen Höcker haben!",
            "Was macht ein Papagei im Dschungel? - Sprechen!",
            "Warum sind Tiger so stark? - Weil sie immer jagen!",
            "Was ist rot und steht auf dem Feld? - Ein Traktor!",
            "Warum können Schafe so gut zählen? - Weil sie immer Wolle haben!",
            "Was macht ein Wolf im Wald? - Heulen!",
            "Warum sind Füchse so schlau? - Weil sie immer nachdenken!",
            "Was ist gelb und fliegt durch die Luft? - Eine Fliege!",
            "Warum können Enten so gut schwimmen? - Weil sie immer eine Ente haben!",
            "Was macht ein Huhn im Stall? - Gackern!",
            "Warum sind Pferde so schnell? - Weil sie immer galoppieren!",
            "Was ist grün und läuft durch den Garten? - Ein Gartenschlauch!",
            "Warum können Frösche so gut hüpfen? - Weil sie immer einen Sprung machen!",
            "Was macht ein Schaf auf der Wiese? - Grasen!",
            "Warum sind Bären so stark? - Weil sie immer Honig essen!",
            "Was ist blau und fliegt durch die Luft? - Ein Blauflieger!",
            "Warum können Hunde so gut bellen? - Weil sie immer einen Knochen haben!",
            "Was macht ein Kater im Haus? - Schlafen!",
            "Warum sind Katzen so neugierig? - Weil sie immer schnüffeln!",
            "Was ist rot und läuft durch die Stadt? - Eine Ampel!",
            "Warum können Affen so gut klettern? - Weil sie immer einen Ast haben!",
            "Was macht ein Frosch im Teich? - Quaken!",
            "Warum sind Schildkröten so langsam? - Weil sie ihr Haus immer dabei haben!",
        ]
        print("Chatbot:", random.choice(witze))
        print(" ")
        print("Schreibe 'Zahl' um eine Zahl zwischen 1 und 100 zu erraten, oder 'Witz' um einen weiteren Witz zu hören.")
    else:
        break
