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
sl.info("Zona Polare")
if sl.button("clima"):
    sl.write("inverni lunghi e freddi ")
    sl.write("estati brevi e fresche")
if sl.button("Bioma"):
    sl.title("Taiga")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/500px-Fall_on_the_Yukon_Flats_NWR.jpg")
    sl.write("Flora: foreste di conifere")
    sl.write("Fauna: continentale")
    sl.title("Tundra")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Icebreaker_in_greenland_2.JPG/500px-Icebreaker_in_greenland_2.JPG")
    sl.write("flora:muschi e licheni")
    sl.write("fauna:renne,alci,gufi,volpi,orsi")