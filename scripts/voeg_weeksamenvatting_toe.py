from datetime import datetime

# Bepaal datum
vandaag = datetime.utcnow()
datum_str = vandaag.strftime("%Y-%m-%d")
titel_datum = vandaag.strftime("%A %d %B %Y")

# Dummy content – dit kun je later vervangen door dynamische invoer
wat_goed = "Je reflecteerde dagelijks, startte het schilderproject, genoot van sociale momenten en zette een handleiding op."
wat_moeilijk = "Volle dagen, technische uitdagingen, sociale spanning."
wat_meenemen = "Één ding tegelijk, rust is herstel, en nietsdoen mag."

# Laad huidige RSS-feed
with open("weeksamenvatting.rss", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Zoek de plek om het nieuwe item in te voegen (voor </channel>)
insert_index = next(i for i, line in enumerate(lines) if "</channel>" in line)

# Bouw nieuw RSS-item
nieuw_item = f"""  <item>
    <title>Weeksamenvatting – {titel_datum}</title>
    <link>https://marc7481.github.io/rss-weeksamenvatting/{datum_str}</link>
    <description>Wat ging goed deze week: {wat_goed}

Wat vroeg energie: {wat_moeilijk}

Wat neem je mee: {wat_meenemen}</description>
    <pubDate>{vandaag.strftime("%a, %d %b %Y %H:%M:%S +0000")}</pubDate>
    <guid>https://marc7481.github.io/rss-weeksamenvatting/{datum_str}</guid>
  </item>
"""

# Voeg item toe op juiste plek
lines.insert(insert_index, nieuw_item + "\n")

# Sla bijgewerkte RSS-feed op
with open("weeksamenvatting.rss", "w", encoding="utf-8") as f:
    f.writelines(lines)

# Genereer eenvoudige HTML-pagina
html_content = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Weeksamenvatting – {titel_datum}</title>
</head>
<body>
    <h1>Weeksamenvatting – {titel_datum}</h1>
    <p><strong>Wat ging goed:</strong> {wat_goed}</p>
    <p><strong>Wat vroeg energie:</strong> {wat_moeilijk}</p>
    <p><strong>Wat neem je mee:</strong> {wat_meenemen}</p>
</body>
</html>
"""

# Opslaan als HTML-bestand
with open(f"{datum_str}.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Weeksamenvatting toegevoegd.")
