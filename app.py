import streamlit as sl
#Titolo della pagina
sl.title("Geografia interattiva")
#Sottotitolo della pagina
sl.write("Ecco il mio progetto di esame")
#Collegamento con immagine
sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Map_of_the_world_with_countries_and_dependencies.svg/1024px-Map_of_the_world_with_countries_and_dependencies.svg.png")
#sezione animali
sl.subheader("zone climatiche del mondo")
#creiamo un bottone
# --- Sezione zona polare-subpolare---
sl.subheader("zona polare-subpolare")

# Bottone 1:fascia subpolare
if sl.button("Zona Subpolare"):
    sl.info("Clima")
    sl.write("inverni lunghi e freddi ")
    sl.write("estati brevi e fresche")
    sl.info("Bioma")
    sl.title("Taiga")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/500px-Fall_on_the_Yukon_Flats_NWR.jpg")
    sl.write("Flora: foreste di conifere")
    sl.write("Fauna: continentale")
    sl.title("Tundra")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Icebreaker_in_greenland_2.JPG/500px-Icebreaker_in_greenland_2.JPG")
    sl.write("flora:muschi e licheni")
    sl.write("fauna:renne,alci,gufi,volpi,orsi")

# Bottone 2:fascia subpolare
if sl.button("Zona Polare"):
    sl.info("Clima")
    sl.write("temperature piu' basse della terra")
    sl.write("6 mesi di buio 6 mesi di luce")
    sl.info("Bioma")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg/1024px-Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg")
    sl.write("Aree deserte")
    sl.write("fauna: pinguni,foche e albatro reale")

# --- Sezione zona tropicale---
sl.subheader("zona tropicale")

# Bottone 1:fascia subpolare
if sl.button("zona tropicale umida"):
    sl.info("Clima")
    sl.write(" 2 stagioni ")
    sl.write("stagine delle piogge e stagine secca")
    sl.info("Bioma")
    sl.title("giungla")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/500px-Fall_on_the_Yukon_Flats_NWR.jpg")
    sl.write("Flora: foreste tropicale con piante alofire")
    sl.write("Fauna:grandi mammiferi predatori come tigri o giaguari, molte speci di uccelli e rettili")
    sl.title("savana")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Icebreaker_in_greenland_2.JPG/500px-Icebreaker_in_greenland_2.JPG")
    sl.write("flora:erbe e arbusti spinosi")
    sl.write("fauna:grandi mammiferi (come leoni, elefanti, zebre...), struzzi, uccelli serpentari e serpenti")
if sl.button("zona tropicale secca"):
    sl.info("Clima")
    sl.write("scarse piogge con le temperature più alte della terra")
    sl.info("Bioma")
    sl.write("Flora: piante xerofite")
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")

# --- Sezione zona equatorial---
sl.subheader("zona equatoriale")

# Bottone 1:fascia subpolare

sl.info("Clima")
sl.write("da 27° a 29°in tutto l'anno e molte piogge(3500mm l'anno)")
sl.info("Bioma")
sl.title("foresta equatoriale")
sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/500px-Fall_on_the_Yukon_Flats_NWR.jpg")
sl.write("Flora: molte spece di piante di altezze elevate per avere la luce del sole ")
sl.write("Fauna:più do metà delle spece terrestri")
