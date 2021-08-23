# Scrap post offices from Wikipedia
import wikipedia
from utils import saveFile

language = "sl"
wikipedia.set_lang(language)

def getData(html):
    data = []
    start = html.find("<ul>")
    while start > 0:
        i = html.find("title=", start)
        end = html.find("</ul>", i)
        while i > 0 and i < end:
            i += 7
            j = html.find('"', i)
            title = html[i:j]

            i = j + 2
            j = html.find("</a>", i)
            town = html[i:j]

            i = html.find("-", j) + 1
            j = html.find('<', i)
            num = int(html[i:j])

            data.append((town, title, num))
            i = html.find("title=", j)
        start = html.find("<ul>", end)
    return data

h = wikipedia.page("Seznam poštnih številk v Sloveniji").html()
d = getData(h)

# Uncomment to save
# saveFile("data/poste.pkl.gz", d)