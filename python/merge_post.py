# Merge post offices with settlements
from typing import List
from datastructure import Entry
from utils import loadFile, saveFile

poste = [i for i in loadFile("data/poste.pkl.gz") if i[0].lower() != "mostec"] # Mostec in Dobova sta enaka?
data: List[Entry] = loadFile("data/naselja.pkl.gz")
centers = []

for d in data:
    d.idx = None

# Bohinjsko jezero - vbistvu v kraju Ribčev Laz
data[3871].idx = 4265
# centers.append(3871)

# Brusnice - leži v Velike Brusnice
data[4953].idx = 8321
# centers.append(4953)

# Črni Vrh
data[5706].idx = 5274
# centers.append(5706)

# Dobrovo v Brdih
data[647].idx = 5212
# centers.append(647)

# Gozd - Martuljek
data[1262].idx = 4282
# centers.append(1262)

# Grobelno
data[1372].idx = 3231
# centers.append(1372)

# Hajdina - naj bo v Zgornji Hajdini
data[5472].idx = 2288
# centers.append(5472)

# Hoče - naj bo Spodnje Hoče
data[4316].idx = 2311
# centers.append(4316)

# Jakobski Dol - vzemimo Spodnji Jakobski Dol
data[4361].idx = 2222

# Jarenina - izberemo Jareninski Vrh, ker je nekje na sredini Jarenine
data[1614].idx = 2221

# Košana - Doljna Košana
data[783].idx = 6256

# Loški Potok - vbistvu Hrib - Loški Potok
data[1485].idx = 1318

# Lukovica - Lukovica pri Domžalah
data[2447].idx = 1225

# Petrovci - wiki da link do HR, pravilno Gornji Petrovci
data[1244].idx = 9203

# Prevorje - vbistvu Lopaca
data[2405].idx = 3262

# Rateče - Planica - je kar Rateče
data[3783].idx = 4283

# Sečovlje/Sicciole - kar Sečovlje
data[4010].idx = 6333

# Sorica - wiki pravi, da Sponja Sorica
data[4295].idx = 4229

# Struge - vbistvu Pri Cerkvi - Struge
data[3616].idx = 1313

# Sv. Ana v Slovenskih goricah - Sveta Ana v Slovenskih goricah
data[4625].idx = 2233

# Sv. Duh na Ostrem Vrhu - Sveti Duh na Ostrem Vrhu
data[4643].idx = 2353

# Sv. Jurij ob Ščavnici - Sveti Jurij ob Ščavnici
data[4652].idx = 9244

# Sv. Trojica v Slovenskih goricah - Sveta Trojica v Slovenskih goricah
data[4631].idx = 2235

# Šentrupert pri Laškem - Šentrupert, Laško
data[5774].idx = 3271

# Škofije - naj bodo Sponje Škofije (več prebivalcev)
data[4345].idx = 6281

# Trnovo pri Gorici - Trnovo, Nova Gorica
data[4819].idx = 5252

# Videm - Dobrepolje - Videm, Dobrepolje
data[5044].idx = 1312

# Voličina - naj bo Spodnja Voličina (več prebivalcev)
data[4300].idx = 2232

towns = dict()
links = dict()

for i,d in enumerate(data):
    towns[d.town.lower()] = i
    links[d.link.lower()] = i

print(sum(1 for p in poste if p[0].lower() in towns or p[0].lower() in links or p[1].lower() in towns or p[1].lower() in links))
print(len(poste))

def addCenter(x, d, p):
    i = d[x]
    # centers.append(i)
    data[i].idx = p

for i,p in enumerate(poste):
    if p[0].lower() == "Ljubljana p.p.":
        continue
    if p[0].lower() in towns:
        addCenter(p[0].lower(), towns, p[2])
    elif p[0].lower() in links:
        addCenter(p[0].lower(), links, p[2])
    elif p[1].lower() in towns:
        addCenter(p[1].lower(), towns, p[2])
    elif p[1].lower() in links:
        addCenter(p[1].lower(), links, p[2])
    else:
        # print(i, p)
        pass

for i,d in enumerate(data):
    if d.idx is not None:
        centers.append(i)

print(len(centers))

post_data = (data, centers)

# Uncomment to save
# saveFile("data/naselja_poste.pkl.gz", post_data)