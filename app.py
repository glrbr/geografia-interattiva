import streamlit as sl
#Titolo della pagina
sl.title("Geografia interattiva")
#Sottotitolo della pagina
sl.write("Ecco il mio progetto di esame")
#Collegamento con immagine
sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Map_of_the_world_with_countries_and_dependencies.svg/1024px-Map_of_the_world_with_countries_and_dependencies.svg.png")

#sezione zone climatiche
sl.subheader("zone climatiche del mondo")

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
    # Crea due colonne affiancate per questa zona
    fl_zts1, fl_zts2 = sl.columns(2)
    with fl_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Echinocactus_grusonii_%28aka%29.jpg/960px-Echinocactus_grusonii_%28aka%29.jpg", caption="Echinocactus Grusonii", width=200)
    with fl_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Centaurea_horrida_con_Astragalus_terracianoi.jpg", caption="Centaurea Horrida", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_zts1, an_zts2, an_zts3 = sl.columns(3)
    with an_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Camelus_dromedarius_in_Nuweiba.jpg/640px-Camelus_dromedarius_in_Nuweiba.jpg", caption="Dromedario",width=200)
    with an_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Pharaoh_Eagle-owl.jpg/640px-Pharaoh_Eagle-owl.jpg", caption="Gufo reale del deserto", width=200)
    with an_zts3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/2009-03-07Vulpes_zerda028.jpg/640px-2009-03-07Vulpes_zerda028.jpg", caption="Fennec", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_zts4, an_zts5, an_zts6 = sl.columns(3)
    with an_zts4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Common_yellow_scorpion_-_Buthus_occitanus.jpg/640px-Common_yellow_scorpion_-_Buthus_occitanus.jpg", caption="Scorpione giallo", width=200)
    with an_zts5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Hornviper_Cerastes_cerastes.jpg/640px-Hornviper_Cerastes_cerastes.jpg", caption="Vipera cornuta", width=200)
    with an_zts6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Rhombomys_opimus_1.jpg/640px-Rhombomys_opimus_1.jpg", caption="Gerbillo", width=200)

# Bottone 2:fascia polare
if sl.button("Zona Polare"):
    sl.info("Clima")
    sl.write("temperature piu' basse della terra")
    sl.write("6 mesi di buio 6 mesi di luce")
    sl.info("Bioma")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg/1024px-Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg")
    sl.write("Aree deserte")
    sl.write("fauna: pinguni,foche e albatro reale")
    # Crea due colonne affiancate per questa zona
    fl_zts1, fl_zts2 = sl.columns(2)
    with fl_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Echinocactus_grusonii_%28aka%29.jpg/960px-Echinocactus_grusonii_%28aka%29.jpg", caption="Echinocactus Grusonii", width=200)
    with fl_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Centaurea_horrida_con_Astragalus_terracianoi.jpg", caption="Centaurea Horrida", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_zts1, an_zts2, an_zts3 = sl.columns(3)
    with an_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Camelus_dromedarius_in_Nuweiba.jpg/640px-Camelus_dromedarius_in_Nuweiba.jpg", caption="Dromedario",width=200)
    with an_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Pharaoh_Eagle-owl.jpg/640px-Pharaoh_Eagle-owl.jpg", caption="Gufo reale del deserto", width=200)
    with an_zts3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/2009-03-07Vulpes_zerda028.jpg/640px-2009-03-07Vulpes_zerda028.jpg", caption="Fennec", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_zts4, an_zts5, an_zts6 = sl.columns(3)
    with an_zts4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Common_yellow_scorpion_-_Buthus_occitanus.jpg/640px-Common_yellow_scorpion_-_Buthus_occitanus.jpg", caption="Scorpione giallo", width=200)
    with an_zts5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Hornviper_Cerastes_cerastes.jpg/640px-Hornviper_Cerastes_cerastes.jpg", caption="Vipera cornuta", width=200)
    with an_zts6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Rhombomys_opimus_1.jpg/640px-Rhombomys_opimus_1.jpg", caption="Gerbillo", width=200)

# --- Sezione zona tropicale---
sl.subheader("zona tropicale")
# Bottone 1:fascia subpolare
if sl.button("zona tropicale umida"):
    sl.info("Clima")
    sl.write(" 2 stagioni ")
    sl.write("stagine delle piogge e stagine secca")
    sl.info("Bioma")
    sl.title("giungla")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Tropical_rainforest_2%2C_Koh_Chang%2C_Thailand.jpg/960px-Tropical_rainforest_2%2C_Koh_Chang%2C_Thailand.jpg")
    sl.write("Flora: foreste tropicale con piante alofire")
    sl.write("Fauna:grandi mammiferi predatori come tigri o giaguari, molte speci di uccelli e rettili")
    sl.title("savana")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/f/f4/Savana_Bekol.jpg")
    sl.write("flora:erbe e arbusti spinosi")
    sl.write("fauna:grandi mammiferi (come leoni, elefanti, zebre...), struzzi, uccelli serpentari e serpenti")
    # Crea due colonne affiancate per questa zona
    fl_zts1, fl_zts2 = sl.columns(2)
    with fl_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Echinocactus_grusonii_%28aka%29.jpg/960px-Echinocactus_grusonii_%28aka%29.jpg", caption="Echinocactus Grusonii", width=200)
    with fl_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Centaurea_horrida_con_Astragalus_terracianoi.jpg", caption="Centaurea Horrida", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_zts1, an_zts2, an_zts3 = sl.columns(3)
    with an_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Camelus_dromedarius_in_Nuweiba.jpg/640px-Camelus_dromedarius_in_Nuweiba.jpg", caption="Dromedario",width=200)
    with an_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Pharaoh_Eagle-owl.jpg/640px-Pharaoh_Eagle-owl.jpg", caption="Gufo reale del deserto", width=200)
    with an_zts3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/2009-03-07Vulpes_zerda028.jpg/640px-2009-03-07Vulpes_zerda028.jpg", caption="Fennec", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_zts4, an_zts5, an_zts6 = sl.columns(3)
    with an_zts4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Common_yellow_scorpion_-_Buthus_occitanus.jpg/640px-Common_yellow_scorpion_-_Buthus_occitanus.jpg", caption="Scorpione giallo", width=200)
    with an_zts5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Hornviper_Cerastes_cerastes.jpg/640px-Hornviper_Cerastes_cerastes.jpg", caption="Vipera cornuta", width=200)
    with an_zts6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Rhombomys_opimus_1.jpg/640px-Rhombomys_opimus_1.jpg", caption="Gerbillo", width=200)

if sl.button("zona tropicale secca"):
    sl.info("Clima")
    sl.write("scarse piogge con le temperature più alte della terra")
    sl.info("Bioma")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/c/cb/Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg")
    sl.write("Flora: piante xerofite")
    # Crea due colonne affiancate per questa zona
    fl_zts1, fl_zts2 = sl.columns(2)
    with fl_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Echinocactus_grusonii_%28aka%29.jpg/960px-Echinocactus_grusonii_%28aka%29.jpg", caption="Cactus (cuscino della suocera)", width=200)
    with fl_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Centaurea_horrida_con_Astragalus_terracianoi.jpg", caption="Fiordaliso spinoso", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_zts1, an_zts2, an_zts3 = sl.columns(3)
    with an_zts1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Camelus_dromedarius_in_Nuweiba.jpg/640px-Camelus_dromedarius_in_Nuweiba.jpg", caption="Dromedario",width=200)
    with an_zts2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Pharaoh_Eagle-owl.jpg/640px-Pharaoh_Eagle-owl.jpg", caption="Gufo reale del deserto", width=200)
    with an_zts3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/2009-03-07Vulpes_zerda028.jpg/640px-2009-03-07Vulpes_zerda028.jpg", caption="Fennec", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_zts4, an_zts5, an_zts6 = sl.columns(3)
    with an_zts4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Common_yellow_scorpion_-_Buthus_occitanus.jpg/640px-Common_yellow_scorpion_-_Buthus_occitanus.jpg", caption="Scorpione giallo", width=200)
    with an_zts5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Hornviper_Cerastes_cerastes.jpg/640px-Hornviper_Cerastes_cerastes.jpg", caption="Vipera cornuta", width=200)
    with an_zts6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Rhombomys_opimus_1.jpg/640px-Rhombomys_opimus_1.jpg", caption="Gerbillo", width=200)
    

# --- Sezione zona equatorial---
sl.subheader("zona equatoriale")


if sl.button("foresta equatoriale"):
# Bottone 1:fascia subpolare
    sl.info("Clima")
    sl.write("da 27° a 29°in tutto l'anno e molte piogge(3500mm l'anno)")
    sl.info("Bioma")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/a/a5/Shaheed_Island%2C_Andamans%2C_Tropical_forest.jpg")
    sl.write("Flora: molte spece di piante di altezze elevate per avere la luce del sole ")
    sl.write("Fauna:più di metà delle spece terrestri")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_zfe1, an_zfe2, an_zfe3 = sl.columns(3)
    with an_zfe1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/113_Jaguar_in_Encontro_das_%C3%81guas_State_Park_Photo_by_Giles_Laurent.jpg/640px-113_Jaguar_in_Encontro_das_%C3%81guas_State_Park_Photo_by_Giles_Laurent.jpg", caption="Giaguaro",width=200)
    with an_zfe2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Ecuadorian_mantled_howler_%28Alouatta_palliata_aequatorialis%29_family_group.jpg/640px-Ecuadorian_mantled_howler_%28Alouatta_palliata_aequatorialis%29_family_group.jpg", caption="Scimmia urlatrice", width=200)
    with an_zfe3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Brown-throated_three-toed_sloth_female_face.JPG/640px-Brown-throated_three-toed_sloth_female_face.JPG", caption="Bradipo", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_zfe4, an_zfe5, an_zfe6 = sl.columns(3)
    with an_zfe4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Tucano_em_Campinas.jpg/640px-Tucano_em_Campinas.jpg", caption="Tucano", width=200)
    with an_zfe5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Job%C3%B3ia_comum_%28Boa_constrictor%29.jpg/640px-Job%C3%B3ia_comum_%28Boa_constrictor%29.jpg", caption="Boa", width=200)
    with an_zfe6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Scarlet_Macaw_at_Kuranda-1_%286285883802%29.jpg/640px-Scarlet_Macaw_at_Kuranda-1_%286285883802%29.jpg", caption="L'Ara Macao", width=200)
