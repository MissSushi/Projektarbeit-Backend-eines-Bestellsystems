#
#import os
import random


# def clear():
#     os.system('cls')
#     print("\n"*30)

#Preis wird definiert.
def get_price() -> float:
    return float(f'{random.randint(19, 99)}.{random.choice(("99", "49", "95", "98"))}')

#Sortiment wird definiert. Für jede größe in jeder Farbe, random Menge, preis funktion wird hier aufgerufen
#
def sortiment():
    farbe = ("Blau", "Rot", "Schwarz")
    größen = (36, 38, 40, 42)
    produktnummer = 1001
    for f in farbe:
        for g in größen:
            damen_blusen[f"{produktnummer}"] = {"Artikelnummer": produktnummer, "Beschreibung": f"Bluse, {f}",
                                                "Preis": get_price(), "Menge": random.randint(1, 6),
                                                "Größe": g, "Warenkorb": 0}
            artikelnummern.append(produktnummer)
            produktnummer += 1
    produktnummer = 2001
    for f in farbe:
        for g in größen:
            herren_hemden[f"{produktnummer}"] = {"Artikelnummer": produktnummer, "Beschreibung": f"Hemd, {f}",
                                                 "Preis": get_price(), "Menge": random.randint(1, 8),
                                                 "Größe": g, "Warenkorb": 0}
            artikelnummern.append(produktnummer)
            produktnummer += 1
    produktnummer = 3001
    for f in farbe:
        for g in größen:
            damen_jeans[f"{produktnummer}"] = {"Artikelnummer": produktnummer, "Beschreibung": f"Jeans, {f}",
                                               "Preis": get_price(), "Menge": random.randint(1, 6),
                                               "Größe": g, "Warenkorb": 0}
            artikelnummern.append(produktnummer)
            produktnummer += 1
    produktnummer = 4001
    for f in farbe:
        for g in größen:
            herren_jeans[f"{produktnummer}"] = {"Artikelnummer": produktnummer, "Beschreibung": f"Jeans, {f}",
                                                "Preis": get_price(), "Menge": random.randint(1, 6),
                                                "Größe": g, "Warenkorb": 0}
            artikelnummern.append(produktnummer)
            produktnummer += 1

#um Artikel im Warenkorb hinzuzufügen. Kat sind die Nummern aus der Navigation
#wir prüfen ob kategorie mit user input einstimmt. Der schlüssel von nen Dict ist string, deswegen str konvertierung
def artikel_hinzufügen(artikel: int, menge: int, kat: int):
    # print("Hat geklappt")
    if kat == 5:
        warenkorb_liste.append(herren_jeans[str(artikel)])
        sortiment_ändern(herren_jeans[str(artikel)], menge)
    elif kat == 4:
        warenkorb_liste.append(damen_jeans[str(artikel)])
        sortiment_ändern(damen_jeans[str(artikel)], menge)
    elif kat == 3:
        warenkorb_liste.append(herren_hemden[str(artikel)])
        sortiment_ändern(herren_hemden[str(artikel)], menge)
    elif kat == 2:
        warenkorb_liste.append(damen_blusen[str(artikel)])
        sortiment_ändern(damen_blusen[str(artikel)], menge)
    im_warenkorb.append(artikel)

#Menge vom Sortiment wird geändert nachdem es zum Warenkorb hinzugefügt wurde
def sortiment_ändern(artikel, menge):
    artikel['Menge'] -= menge
    artikel['Warenkorb'] += menge

#Fehlende Menge aus dem Warenkorb wird dem Artikel hinzugefügt, Warenkorb auf 0 gesetzt und dann wird der Korb geleert
def warenkorb_leeren():
    for x in warenkorb_liste:
        x['Menge'] += x['Warenkorb']
        x['Warenkorb'] = 0

    warenkorb_liste.clear()
    warenkorb()

#Wenn im Warenkorb mehr als 0 Elemente drin sind, für jedes Element im Warenkorb wird das geprinted, für jedes Element im Warenkorb 
#Preis * Elemente im Warenkorb summiert. Gesamtsumme wird geprinted, AUswahl variable wird erstellt und überprüft
#wenn auswahl == 1 ist, dann bestellung bestätigt und Warenkorb wird wieder auf 0 gesetzt
def bezahlung():
    preis = 0
    if len(warenkorb_liste) > 0:
        for x in warenkorb_liste:
            print(f"Artikelnummer: {x['Artikelnummer']} Beschreibung: {x['Beschreibung']}, Menge: {x['Warenkorb']},"
                  f" Größe: {x['Größe']}, Preis: {x['Preis']}€")
            preis += x['Preis']*x['Warenkorb']

        print(f"\nGesamtpreis: {round(preis, 2)}€")
    auswahl = navigation('bestellung')
    if auswahl == 1:
        print("Bestellung bestätigt!")
        for x in warenkorb_liste:
            x['Warenkorb'] = 0
        warenkorb_liste.clear()
        main()
        return
    elif auswahl == 0:
        warenkorb()
        return
    else:
        print("Ungültige Eingabe\n\n")
        bezahlung()
        return


def warenkorb():
    print("Warenkorb: \n")
    preis = 0
    if len(warenkorb_liste) > 0:
        for x in warenkorb_liste:
            print(f"Artikelnummer: {x['Artikelnummer']} Beschreibung: {x['Beschreibung']}, Menge: {x['Warenkorb']},"
                  f" Größe: {x['Größe']}, Preis: {x['Preis']}€")
            preis += x['Preis']*x['Warenkorb']

        print(f"\nGesamtpreis: {round(preis, 2)}€")

    else:
        print("Warenkorb leer")
    navigation('warenkorb')

#wenn man sich im Warenkorb aufhält, mach das, wenn man sich im Sortiment aufhält, mach das usw
def navigation(param) -> int:  # TODO param
    if param == "warenkorb":
        print("Navigation: '0' für Beenden. '1' für Sortiment. '4' um zu bestellen. '5' um den Warenkorb zu leeren.")
        while True:
            try:
                auswahl = int(input())
            except ValueError:
                print("Ungültige Eingabe.")
                continue
            else:
                if auswahl in (0, 1, 4, 5):
                    if auswahl == 0:
                        exit()
                    elif auswahl == 1:
                        show_sortiment()
                    elif auswahl == 4:
                        bezahlung()
                    elif auswahl == 5:
                        warenkorb_leeren()
                else:
                    print("Ungültige Eingabe")
                    continue
    if param == "sortiment":
        print("Navigation: '0' für Beenden. '1' für Warenkorb. '2' - Damen Blusen, '3' - Herren Hemden,"
              " '4' - Damen Jeans, '5' - Herren Jeans.")
        while True:
            try:
                auswahl = int(input())
            except ValueError:
                print("Ungültige Eingabe.")
                continue
            else:
                if auswahl == 0:
                    exit()
                elif auswahl == 1:
                    warenkorb()
                elif auswahl in (2, 3, 4, 5):
                    return auswahl
                else:
                    print("Ungültige Eingabe")
                    continue
    if param == "bestellung":
        print("Navigation: '0' zum abbrechen. '1' zum bestätigen.")
        while True:
            try:
                auswahl = int(input())
            except ValueError:
                print("Ungültige Eingabe.")
                continue
            else:
                if auswahl in (0, 1):
                    return auswahl
                else:
                    print("Ungültige Eingabe")
                    continue
    if param == "start":
        print("Navigation: '0' für Beenden. '1' für Sortiment. '2' für Warenkorb.")
        while True:
            try:
                auswahl = int(input())
            except ValueError:
                print("Ungültige Eingabe.")
                continue
            else:
                if auswahl in (0, 1, 2):
                    if auswahl == 0:
                        exit()
                    elif auswahl == 1:
                        show_sortiment()
                    elif auswahl == 2:
                        warenkorb()
                else:
                    print("Ungültige Eingabe")
                    continue


def show_sortiment():
    # print("Hat geklappt!n Sortiment")
    # clear()

    def item_hinzufügen(kat):
        while True:
            try:
                print("Bitte Artikelnummer eingeben um Artikel zum Warenkorb hinzuzufügen."
                      " '0' um zum Hauptmenü zurückzukehren. '1' um in den Warenkorb zu gelangen.")
                artikel = int(input())
            except ValueError:
                print("Ungültige Eingabe")
                continue
            else:
                if artikel == 0:
                    main()
                    return
                elif artikel == 1:
                    warenkorb()
                    pass
                elif artikel in artikelnummern:
                    try:
                        menge = int(input("Bitte Menge eingeben: "))
                    except ValueError:
                        print("Ungültige Eingabe")
                        continue
                    else:
                        if kat == 5:
                            if menge <= herren_jeans[str(artikel)]['Menge']:
                                artikel_hinzufügen(artikel, menge, kat)
                                show_sortiment()
                            else:
                                print("Ungültige Menge")
                        elif kat == 4:
                            if menge <= damen_jeans[str(artikel)]['Menge']:
                                artikel_hinzufügen(artikel, menge, kat)
                                show_sortiment()
                            else:
                                print("Ungültige Menge")
                        elif kat == 3:
                            if menge <= herren_hemden[str(artikel)]['Menge']:
                                artikel_hinzufügen(artikel, menge, kat)
                                show_sortiment()
                            else:
                                print("Ungültige Menge")
                        elif kat == 2:
                            if menge <= damen_blusen[str(artikel)]['Menge']:
                                artikel_hinzufügen(artikel, menge, kat)
                                show_sortiment()
                            else:
                                print("Ungültige Menge")
                        else:
                            print("Ungültige Eingabe")
                            continue

    auswahl = int(navigation('sortiment'))
    # need exception
    if auswahl == 5:
        print("Herren Jeans:\n")
        for x in herren_jeans.values():
            print(f"Artikelnummer: {x['Artikelnummer']} Beschreibung: {x['Beschreibung']}, Menge: {x['Menge']},"
                  f" Größe: {x['Größe']}, Preis: {x['Preis']}€")
    elif auswahl == 4:
        print("Damen Jeans:\n")
        for x in damen_jeans.values():
            print(f"Artikelnummer: {x['Artikelnummer']} Beschreibung: {x['Beschreibung']}, Menge: {x['Menge']},"
                  f" Größe: {x['Größe']}, Preis: {x['Preis']}€")
    elif auswahl == 3:
        print("Herren Hemden:\n")
        for x in herren_hemden.values():
            print(f"Artikelnummer: {x['Artikelnummer']} Beschreibung: {x['Beschreibung']}, Menge: {x['Menge']},"
                  f" Größe: {x['Größe']}, Preis: {x['Preis']}€")
    elif auswahl == 2:
        print("Damen Blusen:\n")
        for x in damen_blusen.values():
            print(f"Artikelnummer: {x['Artikelnummer']} Beschreibung: {x['Beschreibung']}, Menge: {x['Menge']},"
                  f" Größe: {x['Größe']}, Preis: {x['Preis']}€")

    item_hinzufügen(auswahl)


def main():
    navigation('start')
# signalisiert den Start des Prozesses. Wenn __name__ == __main__ dann hat man das direkt in der Konsole aufgerufen das Programm
# Wenn nicht, dann wird das Programm importiert in einer anderen Python Datei
if __name__ == "__main__":
    damen_blusen = {}
    herren_hemden = {}
    damen_jeans = {}
    herren_jeans = {}

    artikelnummern = []
    warenkorb_liste = []
    im_warenkorb = []
    sortiment()
    main()
