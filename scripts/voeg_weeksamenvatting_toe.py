import datetime
from xml.etree import ElementTree as ET

# Laad de RSS-feed
rss_pad = "weeksamenvatting.rss"
tree = ET.parse(rss_pad)
root = tree.getroot()
channel = root.find("channel")

# Genereer de datum voor de nieuwe samenvatting (afgelopen zondag)
vandaag = datetime.date.today()
zondag = vandaag - datetime.timedelta(days=vandaag.weekday() + 1)
datum_str = zondag.strftime("%Y-%m-%d")
titel_datum = zondag.strftime("%A %d %B %Y")

# Maak nieuw item
item = ET.Element("item")
ET.SubElement(item, "title").text = f"Weeksamenvatting – zondag {titel_datum}"
ET.SubElement(item, "link").text = f"https://marc7481.github.io/rss-weeksamenvatting/{datum_str}.html"
ET.SubElement(item, "description").text = "Automatisch gegenereerde samenvatting – nog aan te vullen."
ET.SubElement(item, "pubDate").text = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
ET.SubElement(item, "guid").text = f"https://marc7481.github.io/rss-weeksamenvatting/{datum_str}"

# Voeg item bovenaan toe
channel.insert(2, item)

# Opslaan
tree.write(rss_pad, encoding="utf-8", xml_declaration=True)
