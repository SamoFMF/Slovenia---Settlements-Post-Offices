import wikipedia

language = "sl"

wikipedia.set_lang(language)

def getCoords(strcoord):
    deg, strcoord = strcoord.split(chr(176))
    if chr(8242) in strcoord:
        val = strcoord.split(chr(8242))
        if val[1] == "":
            minute = val[0]
            sec = "0.0"
        else:
            minute, sec = val
    else:
        minute = "0"
        sec = strcoord[:-1]
    deg = int(deg)
    minute = int(minute)
    sec = float(sec)
    return deg, minute, sec

class Entry:
    def __init__(self, name, title, municipality, municipalityTitle, idx):
        self.town = name
        self.link = title
        self.municipality = municipality
        self.municipalityTitle = municipalityTitle

        self.idx = idx # Position in data

        self.population = None
        self.coordinates = None
        self.statRegion = None
        self.region = None
    
    def __repr__(self) -> str:
        return f"{{ {self.link} -- {self.municipality} -- {self.population} }}"
    
    def getPopulation(self):
        html = wikipedia.page(self.link).html()
        start = html.find("Prebivalstvo")
        if start == -1:
            print(f"Error at {self.link}")
            return
        start = html.find("Skupno", start)
        start = html.find("<td>", start)
        start += 4

        i = 0
        while html[start+i] != "<":
            i += 1
        
        self.population = int(html[start:start+i].replace(".", ""))
    
    def updateData(self):
        try:
            html = wikipedia.page(self.link).html()
        except:
            return

        # Get coordinates
        # Get latitude
        i = html.find('class="latitude"')
        if i < 0:
            # we didn't get the correct html
            return
        else:
            i += 17
        j = html.find("</span>", i) - 2
        latitude = getCoords(html[i:j])

        # Get longitude
        i = html.find("longitude", j) + 11
        j = html.find("</span", i) - 2
        longitude = getCoords(html[i:j])

        self.coordinates = (longitude, latitude)
        
        # Get statistical region
        i = html.find("Statistična regija</a>", j)
        i = html.find("title=", i) + 7
        j = html.find(">", i) - 1
        self.statRegion = html[i:j]

        # Get region
        i = html.find("Tradicionalna pokrajina</a>", j)
        i = html.find("title=", i) + 7
        j = html.find(">", i) - 1
        self.region = html[i:j]

        # Get population
        i = html.find("Prebivalstvo", j)
        i = html.find("Skupno", i)
        i = html.find("<td>", i) + 4
        j = html.find("</td>", i)
        try:
            self.population = int(html[i:j].replace(".", ""))
        except:
            pass

class Table:
    def __init__(self, html):
        self.html = html.replace("\n", "")
        self.data = []

        self.start = -1
        self.end = 0
        self.getEndpoints()
    
    def getEndpoints(self):
        start = self.html.find("<table", self.end)
        if start == -1:
            self.start = -1
            self.end = -1
            return
        end = self.html.find("</table", start)
        # Skip "<table class="wikitable">, sometimes "wikitable sortable"
        while self.html[start] != ">":
            start += 1
        start += 1

        # Skip "<tbody>" and "</tbody>"
        start += 7
        end -= 8

        self.start = self.html.find("</tr>", start) + 5 # Skip first line
        self.end = end
    
    def readEntry(self):
        i = self.start

        # <td>
        i += 4

        if self.html[i] == "<":
            # <a href="..." title="...">
            while self.html[i:i+5] != "title":
                i += 1
            i += 7

            j = 0
            while self.html[i+j] != '"':
                j += 1
            
            title = self.html[i:i+j]
            i += j + 2

            j = 0
            while self.html[i+j] != "<":
                j += 1
            name = self.html[i:i+j]
            i += j

            # </a>
            i += 4

            # </td>
            i += 5
        else:
            while self.html[i:i+5] != "</td>":
                i += 1
            i += 5 # "</td>"
            self.start = i
            return None
        
        self.start = i
    
        return title, name
    
    def readLine(self):
        i = self.start
        
        # <tr>
        i += 4

        title, name = self.readEntry()
        val = self.readEntry()
        if val is None:
            self.readEntry()
            mtitle, municipality = self.readEntry()
        else:
            mtitle, municipality = val

        while self.html[i:i+5] != "</tr>":
            i += 1
        i += 5

        self.start = i

        return Entry(name, title, municipality, mtitle, len(self.data))
    
    def extractData(self):
        while self.start != -1:
            while self.start < self.end:
                self.data.append(self.readLine())
            self.getEndpoints()