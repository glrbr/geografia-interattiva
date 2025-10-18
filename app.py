import streamlit as sl
#Titolo della pagina
sl.title("Geografia interattiva")
#Sottotitolo della pagina
sl.write("Ecco il mio progetto di esame")
#Collegamento con immagine
sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Map_of_the_world_with_countries_and_dependencies.svg/1024px-Map_of_the_world_with_countries_and_dependencies.svg.png")
#sezione animali
sl.subheader("Animali del mondo")
#creiamo un bottone
# --- Sezione animali dell'Africa ---
sl.subheader("🦁 Animali dell'Africa")

# Bottone 1: Elefante
if sl.button("🐘 Elefante"):
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/500px-African_Bush_Elephant.jpg")
    sl.write("*Elefante Africano*")
    sl.write("Vive nelle savane e foreste. È il più grande animale terrestre!")
    sl.info("📍 Continente: Africa")

# Bottone 2: Leone
if sl.button("🦁 Leone"):
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/500px-Lion_waiting_in_Namibia.jpg")
    sl.write("*Leone*")
    sl.write("Il re della savana! Vive in gruppi chiamati branchi.")
    sl.info("📍 Continente: Africa")

# Bottone 3: Giraffa
if sl.button("🦒 Giraffa"):
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Giraffe_standing.jpg/400px-Giraffe_standing.jpg")
    sl.write("*Giraffa*")
    sl.write("L'animale più alto del mondo! Il suo collo può essere lungo 2 metri.")
    sl.info("📍 Continente: Africa")

