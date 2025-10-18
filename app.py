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
if sl.button("Animali dell'Africa"):
    #Questo codice viene eseguito solo quando clicco il bottone
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/500px-African_Bush_Elephant.jpg")
    sl.write("Elefante africano")
    sl.write("vive nelle savane")

#Messaggio di successo
sl.success("La mia prima app funziona!")
