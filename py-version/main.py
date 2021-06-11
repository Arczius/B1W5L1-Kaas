row = "---------------"
naam = "het is "

print("welkom bij de kaas zoekmachine")
print("antwoord hier met ja of nee")
print(row)
print("is de kaas geel?")
ycheese = input("-")
if ycheese.lower() == "ja":
    print("zitten er gaten in?")
    gcheese = input("-")
    if gcheese.lower() == "ja":
        print("is de kaas belachelijk duur?")
        bdcheese = input("-")
        if bdcheese.lower() == "ja":
            print(row)
            print(naam + "Emmenthaler")

        elif bdcheese.lower() == "nee":
            print(row)
            print(naam + "Leerdammer")

    elif gcheese.lower() == "nee":
        print("is de kaas hard als steen?")
        hcheese = input("-")
        if hcheese.lower() == "ja":
            print(row)
            print(naam + "Pamigiano Reggiano")

        elif hcheese.lower() == "nee":
            print(row)
            print(naam + "Goudse kaas")

elif ycheese.lower() == "nee":
    print("heeft de kaas blauwe schimmels?")
    scheese = input("-")
    if scheese.lower() == "ja":
        print("heeft de kaas een korst?")
        kcheese = input("-")
        if kcheese.lower() == "ja":
            print(row)
            print(naam + "Bleu de Rochbaron")

        elif kcheese.lower() == "nee":
            print(row)
            print(naam + "Foume d'Ambert")

    elif scheese.lower() == "nee":
        print("heeft de kaas een korst?")
        kcheese = input("-")
        if kcheese.lower() == "ja":
            print(row)
            print(naam + "Camembert")

        elif kcheese.lower() == "ja":
            print(row)
            print(naam + "Mozzarella")
