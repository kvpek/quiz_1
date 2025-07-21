import csv

def wczytaj_pytania():
    with open ("pytania.csv", "r") as plik:
        reader = csv.reader(plik)
        next(reader)
        pytania = []
        for wiersz in reader:
            pytania.append(wiersz)
        return pytania
    
def rozpocznij_quiz(pytania):
    punkty = 0
    
    for p in pytania:
        tekst_pytania = p[0]
        odpowiedzi = {"a": p[1], "b": p[2], "c": p[3]}
        print(tekst_pytania)
        print("a)", odpowiedzi["a"])
        print("b)", odpowiedzi["b"])
        print("c)", odpowiedzi["c"])
        odpowiedz = input("Podaj odpowiedź: ").lower()    
        if odpowiedz == p[4]:
            print("Odpowiedź prawidłowa! Punkt dla ciebie!")
            punkty += 1
            print(f"Twoja liczba punktów to {punkty}/{len(pytania)}.")
        else:
            print("Niestety twoja odpowiedź jest błędna. Nie dostajesz punkta.")       

pytania = wczytaj_pytania()        
rozpocznij_quiz(pytania)