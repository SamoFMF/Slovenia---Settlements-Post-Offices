from typing import List
from datastructure import *
from utils import loadFile, saveFile

# List of all settlements
data: List[Entry] = []
for i in [j for j in range(26)] + [172, 256, 285]:
    x = chr(i+97)
    if x in {"q", "x", "y", "w"}:
        continue
    T = loadFile(f"data/naselja_{x}.pkl.gz")
    data += T.data

#######################
# Update missing data #
#######################
# Besnica
d = data[118]
d.link = "Besnica, Ljubljana"
d.coordinates = ((14, 38, 55.37), (46, 2, 15.73))
d.population = 239
d.statRegion = "Osrednjeslovenska regija"
d.region = "Dolenjska"

# Ceršak
d = data[500]
d.population = 1764 # Celota (sredisce manj)

# Donačka gora
d = data[818]
d.population = 185 # Idk zakaj ni delalo
d.statRegion = "Savinjska regija"
d.region = "Štajerska"

# Dren
d = data[874]
d.link = "Dren, Kostel"
d.population = 21
d.coordinates = ((14, 53, 49.12), (45, 29, 46.77))
d.statRegion = "Jugovzhodna Slovenija"
d.region = "Dolenjska"

# Drenje
d = data[876]
d.link = "Drenje, Dolenjske Toplice"
d.population = 59
d.coordinates = ((15, 0, 29.12), (45, 47, 1.92))
d.statRegion = "Jugovzhodna Slovenija"
d.region = "Dolenjska"

# Gunclje
d = data[1387]
d.population = 1000 # (ocena)
d.statRegion = "Osrednjeslovenska regija"
d.region = "Dolenjska"

# Hudi Graben
d = data[1508]
d.population = 42
d.statRegion = "Gorenjska regija"
d.region = "Gorenjska"

# Jablaniški Potok
d = data[1578] # S tem je ful problemov usposobit wikipedijo, da najde pravi rezultat
d.population = 7
d.coordinates = ((14,54,11.54), (46,3,1.24))
d.statRegion = "Osrednjeslovenska regija"
d.region = "Dolenjska"

# Kapla na Kozjaku - razdeljena na Spodnja Kapla in Zgornja Kapla, ki jih imamo v seznamu
del data[1788]

# Lendavske Gorice
d = data[2235]
d.population = 663
d.coordinates = ((16,27,34.02), (46,34,0.33))
d.statRegion = "Pomurska regija"
d.region = "Prekmurje"

# Ljubljana
d = data[2324]
d.population = 286745 # metropolitansko obmocje = 537712
d.coordinates = ((14,30,0.0), (46,3,0.0)) # Napaka pri parsanju
d.region = "Dolenjska"

# Logarska Dolina
d = data[2357]
d.population = 113
d.statRegion = "Savinjska regija"
d.region = "Štajerska"

# Luža
d = data[2454]
d.link = "Luža, Trebnje"
d.population = 66
d.coordinates = ((14,57,22.68), (45,54,13.04))
d.statRegion = "Jugovzhodna Slovenija"
d.region = "Dolenjska"

# Mala sela, Črnomelj
d = data[2504]
d.population = 17
d.coordinates = ((15,18,17.06), (45,30,58.67))
d.statRegion = "Jugovzhodna Slovenija"
d.region = "Dolenjska"

# Miklavž na Dravskem polju
d = data[2696]
d.population = 4363
d.coordinates = ((15,41,57.6), (46,30,20.69))
d.statRegion = "Podravska regija"
d.region = "Štajerska"

# Novi Svet
d = data[2888]
d.population = 112
d.coordinates = ((14,8,34.76), (45,54,25.2))
d.statRegion = "Osrednjeslovenska regija"
d.region = "Notranjska"

# Plešivec
d = data[3192]
d.link = "Plešivec, Velenje"
d.population = 406
d.coordinates = ((15,6,19.79), (46,24,35.53))
d.statRegion = "Savinjska regija"
d.region = "Štajerska"

# Presika
d = data[3589]
d.link = "Presika, Ljutomer"
d.population = 131
d.coordinates = ((16,14,26.98), (46,29,34.0))
d.statRegion = "Pomurska regija"
d.region = "Štajerska"

# Preska, Medove
del data[3590] # V 20. stoletju prikljucena mestu Medvode

# Robanov Kot
d = data[3897]
d.population = 138
d.coordinates = ((14,42,36.52), (46,23,50.68))
d.statRegion = "Savinjska regija"
d.region = "Štajerska"

# Snežnik
d = data[4223] # V data je gora ne naselje
d.link = "Snežnik, Ilirska Bistrica"
d.population = 19
d.coordinates = ((14,26,48.46), (45,35,20.96))
d.statRegion = "Primorsko-notranjska regija"
d.region = "Notranjska"

# Staro selo
d = data[4478]
d.population = 168
d.coordinates = ((13,31,51.4), (46,14,45.35))
d.statRegion = "Goriška regija"
d.region = "Primorska"

# Suhi Potok
d = data[4608] # Napačne koordinate itd. (verjetno kaže nek potok)
d.population = 0
d.coordinates = ((14,57,42.9), (45,35,16.69))
d.statRegion = "Jugovzhodna Slovenija"
d.region = "Dolenjska"

# Uršla Gora
d = data[4882] # Najde goro zraven naselja
d.population = 25
d.coordinates = ((14,57,4.16), (46,29,57.3))
d.statRegion = "Koroška regija"
d.region = "Koroška"

# Ustje
d = data[4884]
d.link = "Ustje, Ajdovščina"
d.population = 344
d.coordinates = ((13,53,42.3), (45,52,12.84))
d.statRegion = "Goriška regija"
d.region = "Primorska"

##############
# FIX ERRORS #
##############
# There were some errors in the data
# Klinja vas
data[1831].coordinates = ((14,51,0.0), (45,39,0.0))

# Trzin
data[4842].coordinates = ((14,34,0.0), (46,8,0.0))

##########################
# Fix municipality names #
##########################
mestne = {"Murska Sobota", "Maribor", "Ptuj", "Slovenj Gradec", "Celje", "Velenje", "Novo mesto", "Ljubljana", "Kranj", "Nova Gorica", "Koper"}
for t in data:
    if "občina" not in t.municipality.lower():
        if t.municipality in mestne:
            t.municipality = f"Mestna občina {t.municipality}"
        else:
            t.municipality = f"Občina {t.municipality}"

data[498].municipality = "Občina Šmartno pri Litiji"
data[498].municipalityTitle = "Občina Šmartno pri Litiji"
data[5701].municipality = "Občina Šmartno pri Litiji"
data[5701].municipalityTitle = "Občina Šmartno pri Litiji"

##################################
# Update wrong stat. region data #
##################################
# Brestovica pri Komnu
d = data[303]
d.statRegion = "Obalno-kraška regija"

# Hrastnik, Moravče
d = data[1449]
d.statRegion = "Osrednjeslovenska regija"

# Malovše
d = data[2601]
d.statRegion = "Goriška Slovenija"

# Padna
d = data[3041]
d.statRegion = "Obalno-kraška regija"

# Parecag
d = data[3063]
d.statRegion = "Obalno-kraška regija"

# Zgornje Loke
d = data[5523]
d.statRegion = "Osrednjeslovenska regija"

# Cesta, Ajdovščina
d = data[501]
d.statRegion = "Goriška regija"

# Gabrovlje
d = data[986]
d.statRegion = "Savinjska regija"

# Hrib, Preddvor
d = data[1480]
d.statRegion = "Gorenjska regija"

# Markišavci
d = data[2617]
d.statRegion = "Pomurska regija"

# Markovščina
d = data[2622]
d.statRegion = "Obalno-kraška regija"

# Murski Vrh
d = data[2801]
d.statRegion = "Pomurska regija"

# Podgora, Šmartno ob Paki
d = data[3245]
d.statRegion = "Savinjska regija"

# Polene
d = data[3402]
d.statRegion = "Savinjska regija"

# Serjuče
d = data[4114]
d.statRegion = "Osrednjeslovenska regija"

# Spodnji Log, Kočevje
d = data[4367]
d.statRegion = "Jugovzhodna Slovenija"

# Troblje
d = data[4823]
d.statRegion = "Koroška regija"

# Popravki imen regij
for t in data:
    if t.statRegion == "Obalno - kraška regija":
        t.statRegion = "Obalno-kraška regija"
    elif t.statRegion == "Goriška":
        t.statRegion = "Goriška regija"
    elif t.statRegion == "Gorenjska":
        t.statRegion = "Gorenjska regija"
    elif t.statRegion == "Osrednjeslovenska":
        t.statRegion = "Osrednjeslovenska regija"
    elif t.statRegion == "Goriška Slovenija":
        t.statRegion = "Goriška regija"

# Pravilno razporedimo regije, ki imajo "Primorska" kot statistično regijo
oksr = {"Občina Ankaran", "Občina Hrpelje - Kozina", "Občina Komen", "Občina Piran", "Občina Divača", "Občina Izola", "Mestna občina Koper", "Občina Sežana"}
pnsr = {"Občina Bloke", "Občina Ilirska Bistrica", "Občina Pivka", "Občina Postojna", "Občina Cerknica", "Občina Loška dolina"}
for t in data:
    if t.statRegion == "Primorska":
        if t.municipality in oksr:
            t.statRegion = "Obalno-kraška regija"
        elif t.municipality in pnsr:
            t.statRegion = "Primorsko-notranjska regija"
        else:
            t.statRegion = "Goriška regija"

#######################
# Update region names #
#######################

# Briše, Zagorje ob Savi
data[396].region = "Gorenjska"

# Bučerca
data[426].region = "Štajerska"

# Dole pri Škofljici
data[676].region = "Dolenjska"

# Gabrovka, Litija
data[985].region = "Dolenjska"

# Gornje Ravne
data[1230].region = "Dolenjska"

# Gradišče v Tuhinju
data[1306].region = "Gorenjska"

# Izlake
data[1567].region = "Gorenjska"

# Korte
data[1950].region = "Primorska"

# Kropa
data[2098].region = "Gorenjska"

# Lancovo
data[2167].region = "Gorenjska"

# Mlinše
data[2727].region = "Gorenjska"

# Piran
data[3143].region = "Primorska"

# Polenšak
data[3403].region = "Štajerska"

# Potok v Črni
data[3484].region = "Gorenjska"

# Preserje, Braslovče
data[3586].region = "Štajerska"

# Reber pri Škofljici
data[3841].region = "Dolenjska"

# Selo, Ajdovščina
data[4084].region = "Primorska"

# Silovec
data[4128].region = "Štajerska"

# Slatna
data[4170].region = "Gorenjska"

# Spodnji Hotič
data[4359].region = "Gorenjska"

# Sveti Anton
data[4637].region = "Primorska"

# Trzin
data[4842].region = "Gorenjska"

# Velika Kostrevnica
data[4929].region = "Dolenjska"

# Zagorje ob Savi
data[5331].region = "Gorenjska"

# Črni Potok, Šmartno pri Litiji
data[5701].region = "Dolenjska"

# Šumnik, Litija
data[5906].region = "Gorenjska"

pairs = {'Ankaran': 'Primorska', 'Belčji Vrh': 'Bela krajina', 'Boršt, Metlika': 'Bela krajina', 'Brezovica pri Metliki': 'Bela krajina', 'Cerkvišče': 'Bela krajina', 'Dobliče': 'Bela krajina', 'Dragovanja vas': 'Bela krajina', 'Griblje': 'Bela krajina', 'Grič pri Dobličah': 'Bela krajina', 'Jelševnik': 'Bela krajina', 'Kanižarica': 'Bela krajina', 'Krupa, Semič': 'Bela krajina', 'Malo Lešče': 'Bela krajina', 'Semič': 'Bela krajina', 'Slovenske Konjice': 'Štajerska', 'Velenje': 'Štajerska', 'Čurile': 'Bela krajina', 'Celje': 'Štajerska', 'Kidričevo': 'Štajerska', 'Ruše': 'Štajerska', 'Trbovlje': 'Štajerska'}
for t in data:
    if t.link in pairs:
        t.region = pairs[t.link]

for t in data:
    t.region = t.region.replace(" (pokrajina)", "")
    if t.region in {"Goriška regija", "Goriška", "Tolmin"}:
        t.region = "Primorska"
    elif t.region in {"Bela Krajina", "Ljubljanska pokrajina", "Bela krajina"}:
        t.region = "Dolenjska"
    elif t.region in {"Prlekija", "Spodnja Štajerska", "Posavje"}:
        t.region = "Štajerska"
    elif t.region in {"Kamnik", "Mengeš"}:
        t.region = "Gorenjska"
    elif t.region in {"Pomurje"}:
        t.region = "Prekmurje"

valid = {'Štajerska', 'Primorska', 'Gorenjska', 'Koroška', 'Prekmurje', 'Notranjska', 'Dolenjska'}
nv = [t for t in data if t.region not in valid]


print("Skupno št. prebivalcev:", sum(t.population for t in data if t.population is not None))

statRegije = {t.statRegion for t in data}
regije = {t.region for t in data}
print()
print("Število stat. regij:", len(statRegije))
print("Stat. regije:", statRegije)
print()
print("Število regij:", len(regije))
print("Regije:", regije)
print()

# Uncomment to save data
# saveFile("data/naselja.pkl.gz", data)