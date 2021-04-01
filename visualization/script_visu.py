import data 
import utils
import visualization.data.data_extractor
import visualization.utils.generator
import visualization.map.marker as marker
import folium
import collections
from os import makedirs
from os.path import isdir
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium import webdriver
browser = webdriver.Firefox()


# continue using the driver as usual.

data = {
    "Berracasa": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json", "intensity", "dateObserved", "location"),
    "Lavérune": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042632_archive.json", "intensity", "dateObserved", "location"),
    "Celleneuve": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json", "intensity", "dateObserved", "location"),
    "Lattes 2": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042634_archive.json", "intensity", "dateObserved", "location"),
    "Lattes 1": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042635_archive.json", "intensity", "dateObserved", "location"),
    "Vieille-Poste": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063161_archive.json", "intensity", "dateObserved", "location"),
    "Gerhardt": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063162_archive.json", "intensity", "dateObserved", "location"),
    "Delmas 1": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_XTH19101158_archive.json", "intensity", "dateObserved", "location"),
    "Delmas 2": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063163_archive.json", "intensity", "dateObserved", "location"),
    "Albert 1er": data.data_extractor.extract_data_from_url("https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063164_archive.json", "intensity", "dateObserved", "location")
}

def data_locations():
    result = {}
    for key in data.keys():
        result[key] = (data[key][0]["location"]["coordinates"][1],
                       data[key][0]["location"]["coordinates"][0])
    return result


def intensity_by_date():
    result = collections.OrderedDict()
    for key in data.keys():
        for entry in data[key]:
            # 2020-12-17 uniquement par les heures et minutes
            dateNumber = entry["dateObserved"].split(
                "/")[0].split("T")[0].replace("-", "")
            # si result ne contient pas la date, alors j'ajoute un nouveau dictionnaire
            # sinon, j'ajoute au dictionnaire de la date, l'intensité pour la key
            if dateNumber in result:
                result[dateNumber][key] = entry["intensity"]
            else:
                result[dateNumber] = {
                    key: entry["intensity"]
                }
    return result

Montpelier = [43.6112, 3.8767]
data_locations = data_locations()

# grouper les données par dates
intensity_date = intensity_by_date()
# pour chaque date, créer une map à partir des données
Maps = []
for date in list(intensity_date.keys()):
    Map = folium.Map(location=Montpelier, zoom_start=12,
                     tiles="CartoDB positron")
    marker.mark_circles_on_map(
        Map, data_locations, intensity_date[date], 0.10, '#81D8D0')
    Maps.append(
        (Map, date+"-map.html")
    )

destination = "output/htmls"
if not isdir(destination):
    makedirs(destination)

# générer une page html pour chaque map
for Map in Maps:
    Map[0].save(destination+"/"+Map[1])
    
# générer des png pour chaque page html
utils.generate_pngs_from_htmls("output/htmls", "output/pngs", 1)

# générer un gif à partir de png
utils.generate_gif_from_pngs("output/pngs", "output/gif/animation.gif", 3)
