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

# TAIGA
    sl.title("Taiga")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/500px-Fall_on_the_Yukon_Flats_NWR.jpg")
    sl.write("Flora: foreste di conifere")
    sl.write("Fauna: continentale")
# Crea due colonne affiancate per questa zona
    fl_ta1, fl_ta2 = sl.columns(2)
    with fl_ta1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Santuario_della_Verna%2C_abete_bianco.jpg/640px-Santuario_della_Verna%2C_abete_bianco.jpg", caption="Abeti", width=200)
    with fl_ta2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Vaade_Suure_Munam%C3%A4e_vaatetornist_2013_02.jpg/640px-Vaade_Suure_Munam%C3%A4e_vaatetornist_2013_02.jpg", caption="Pini", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_ta1, an_ta2, an_ta3 = sl.columns(3)
    with an_ta1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Wild_Grizzly_Bear.jpg/640px-Wild_Grizzly_Bear.jpg", caption="Orso",width=200)
    with an_ta2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Canis_Lupus_Signatus_%282%29.JPG/640px-Canis_Lupus_Signatus_%282%29.JPG", caption="Lupo", width=200)
    with an_ta3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Lince_ib%C3%A9rico_%28Lynx_pardinus%29%2C_Almuradiel%2C_Ciudad_Real%2C_Espa%C3%B1a%2C_2021-12-19%2C_DD_07.jpg/640px-Lince_ib%C3%A9rico_%28Lynx_pardinus%29%2C_Almuradiel%2C_Ciudad_Real%2C_Espa%C3%B1a%2C_2021-12-19%2C_DD_07.jpg", caption="Lince", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_ta4, an_ta5, an_ta6 = sl.columns(3)
    with an_ta4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/European_otter_02.jpg/640px-European_otter_02.jpg", caption="Lontra", width=200)
    with an_ta5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Mustela_erminea_3.jpg/640px-Mustela_erminea_3.jpg", caption="Ermellino", width=200)
    with an_ta6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Martes_martes_crop_cropped.jpg/640px-Martes_martes_crop_cropped.jpg", caption="Martora", width=200)

# TUNDRA
    sl.title("Tundra")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Icebreaker_in_greenland_2.JPG/500px-Icebreaker_in_greenland_2.JPG")
    sl.write("flora:muschi e licheni")
    sl.write("fauna:renne,alci,gufi,volpi,orsi")
    # Crea due colonne affiancate per questa zona
        # Crea due colonne affiancate per questa zona
    fl_tu1, fl_tu2 = sl.columns(2)
    with fl_tu1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Coscinodon_lawianus_%28J.H._Willis%29_Ochyra%2C_2004_%28described_as_Grimmia_lawiana_J.H._Willis%2C_1966%29._Habit_dry.jpeg/640px-Coscinodon_lawianus_%28J.H._Willis%29_Ochyra%2C_2004_%28described_as_Grimmia_lawiana_J.H._Willis%2C_1966%29._Habit_dry.jpeg", caption="Muschi", width=200)
    with fl_tu2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Licheni_Stanca_Pirinei.JPG/640px-Licheni_Stanca_Pirinei.JPG", caption="Licheni", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_tu1, an_tu2, an_tu3 = sl.columns(3)
    with an_tu1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Carib%C3%BA_%28Rangifer_tarandus%29%2C_Parque_nacional_y_reserva_Denali%2C_Alaska%2C_Estados_Unidos%2C_2017-08-30%2C_DD_40.jpg/640px-Carib%C3%BA_%28Rangifer_tarandus%29%2C_Parque_nacional_y_reserva_Denali%2C_Alaska%2C_Estados_Unidos%2C_2017-08-30%2C_DD_40.jpg", caption="Renne",width=200)
    with an_tu2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/Alces_alces_Wildpark_Alte_Fasanerie_Klein-Auheim_Juni_2012.JPG/640px-Alces_alces_Wildpark_Alte_Fasanerie_Klein-Auheim_Juni_2012.JPG", caption="Alci", width=200)
    with an_tu3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Bubo_scandiacus_Delta_3.jpg/640px-Bubo_scandiacus_Delta_3.jpg", caption="Gufo delle nevi", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_tu4, an_tu5, an_tu6 = sl.columns(3)
    with an_tu4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Terianniaq-Qaqortaq-arctic-fox.jpg/640px-Terianniaq-Qaqortaq-arctic-fox.jpg", caption="Volpe polare", width=200)
    with an_tu5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Steinhuhn.jpg/640px-Steinhuhn.jpg", caption="Pernice", width=200)
    with an_tu6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Sea_lion_sunbathing.jpg/640px-Sea_lion_sunbathing.jpg", caption="Leoni marini", width=200)

# Bottone 2:fascia polare
if sl.button("Zona Polare"):
    sl.info("Clima")
    sl.write("temperature piu' basse della terra")
    sl.write("6 mesi di buio 6 mesi di luce")
    sl.info("Bioma")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg/1024px-Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg")
    sl.write("Aree deserte")
    sl.write("fauna: pinguni,foche e albatro reale")

    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_zp1, an_zp2 = sl.columns(2)
    with an_zp1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/00_2103_Pinguin_-_Petermann_Island_%28Antarktische_Halbinsel%29.jpg/640px-00_2103_Pinguin_-_Petermann_Island_%28Antarktische_Halbinsel%29.jpg", caption="Pinguino Reale",width=200)
    with an_zp2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Ursus_maritimus_in_Alaska.jpg/640px-Ursus_maritimus_in_Alaska.jpg", caption="Orso polare", width=200)
        # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_zp3, an_zp4 = sl.columns(2)
    with an_zp3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Anim0365_-_Flickr_-_NOAA_Photo_Library.jpg/640px-Anim0365_-_Flickr_-_NOAA_Photo_Library.jpg", caption="Foca", width=200)
    with an_zp4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/1/1f/Northern_Royal_Albatross_Taiaroa_Head_Nov_2008_2.jpg", caption="Albatro reale", width=200)

# COMPLETATA
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
    # Crea due colonne affiancate per questa zona
    fl_gi1, fl_gi2 = sl.columns(2)
    with fl_gi1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Avicennia_marina_%28Forssk.%29_Vierh._%2852264901119%29.jpg/640px-Avicennia_marina_%28Forssk.%29_Vierh._%2852264901119%29.jpg", caption="Mangrovie", width=200)
    with fl_gi2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Palm_trees%2Cits_leaves_and_fruits_06.jpg/640px-Palm_trees%2Cits_leaves_and_fruits_06.jpg", caption="Palme", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_gi1, an_gi2, an_gi3 = sl.columns(3)
    with an_gi1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Bengal_tiger_in_Sanjay_Dubri_Tiger_Reserve_December_2024_by_Tisha_Mukherjee_10.jpg/640px-Bengal_tiger_in_Sanjay_Dubri_Tiger_Reserve_December_2024_by_Tisha_Mukherjee_10.jpg", caption="Tigre",width=200)
    with an_gi2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Chapultepec_Zoo_-_Jaguar_%2802%29.jpg/640px-Chapultepec_Zoo_-_Jaguar_%2802%29.jpg", caption="Giaguaro", width=200)
    with an_gi3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Mountain_gorilla_%28Gorilla_beringei_beringei%29_2-year-old_2.jpg/640px-Mountain_gorilla_%28Gorilla_beringei_beringei%29_2-year-old_2.jpg", caption="Gorilla", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_gi4, an_gi5, an_gi6 = sl.columns(3)
    with an_gi4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Crocodylus_acutus_jalisco_mexico.jpg/640px-Crocodylus_acutus_jalisco_mexico.jpg", caption="Coccodrillo", width=200)
    with an_gi5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Canario_silvestre%2C_Serinus_canaria%28%E2%99%82%29_%289109542249%29.jpg/640px-Canario_silvestre%2C_Serinus_canaria%28%E2%99%82%29_%289109542249%29.jpg", caption="Canarino", width=200)
    with an_gi6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Lesser_violetear_%28Colibri_cyanotus_cyanotus%29_in_flight_Cundinamarca.jpg/640px-Lesser_violetear_%28Colibri_cyanotus_cyanotus%29_in_flight_Cundinamarca.jpg", caption="Colibri", width=200)

# FINITA
    sl.title("savana")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/f/f4/Savana_Bekol.jpg")
    sl.write("flora:erbe e arbusti spinosi")
    sl.write("fauna:grandi mammiferi (come leoni, elefanti, zebre...), struzzi, uccelli serpentari e serpenti")
    # Crea due colonne affiancate per questa zona
    fl_sa1, fl_sa2 = sl.columns(2)
    with fl_sa1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Baobab_and_elephant%2C_Tanzania.jpg/640px-Baobab_and_elephant%2C_Tanzania.jpg", caption="Baobab", width=200)
    with fl_sa2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Acacia_heterophylla_1.JPG/640px-Acacia_heterophylla_1.JPG", caption="Acacia", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_sa1, an_sa2, an_sa3 = sl.columns(3)
    with an_sa1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Lion_%28Panthera_leo%29_male_6y.jpg/640px-Lion_%28Panthera_leo%29_male_6y.jpg", caption="Leone",width=200)
    with an_sa2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Burchell%27s_zebra_%28Equus_quagga_burchellii%29_2.jpg/640px-Burchell%27s_zebra_%28Equus_quagga_burchellii%29_2.jpg", caption="Zebra", width=200)
    with an_sa3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Giraffa_camelopardalis_angolensis.jpg/640px-Giraffa_camelopardalis_angolensis.jpg", caption="Giraffa", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_sa4, an_sa5, an_sa6 = sl.columns(3)
    with an_sa4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Avestruz_de_cuello_azul_%28Struthio_camelus_australis%29%2C_cabo_de_Buena_Esparanza%2C_Sud%C3%A1frica%2C_2018-07-23%2C_DD_87.jpg/640px-Avestruz_de_cuello_azul_%28Struthio_camelus_australis%29%2C_cabo_de_Buena_Esparanza%2C_Sud%C3%A1frica%2C_2018-07-23%2C_DD_87.jpg", caption="Struzzo", width=200)
    with an_sa5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Dendroaspis_polylepis00.jpg/640px-Dendroaspis_polylepis00.jpg", caption="Mamba nero", width=200)
    with an_sa6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Secretary_bird_%28Sagittarius_serpentarius%29%2C_Buffalo_Springs_National_Reserve.jpg/640px-Secretary_bird_%28Sagittarius_serpentarius%29%2C_Buffalo_Springs_National_Reserve.jpg", caption="Serpentari", width=200)

#FINITA
if sl.button("zona tropicale secca"):
    sl.info("Clima")
    sl.write("scarse piogge con le temperature più alte della terra")
    sl.info("Bioma")
    sl.image("https://upload.wikimedia.org/wikipedia/commons/c/cb/Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg")
    sl.write("Flora: piante xerofite")
    # Crea due colonne affiancate per questa zona
    fl_ztu1, fl_ztu2 = sl.columns(2)
    with fl_ztu1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Echinocactus_grusonii_%28aka%29.jpg/960px-Echinocactus_grusonii_%28aka%29.jpg", caption="Cactus (cuscino della suocera)", width=200)
    with fl_ztu2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Centaurea_horrida_con_Astragalus_terracianoi.jpg", caption="Fiordaliso spinoso", width=250)
    sl.write("Fauna:uccelli rapaci, rettili, roditori, insetti, e altri mammiferi")
    # Crea tre colonne affiancate per i primi 3 animali di questa zona
    an_ztu1, an_ztu2, an_ztu3 = sl.columns(3)
    with an_ztu1:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Camelus_dromedarius_in_Nuweiba.jpg/640px-Camelus_dromedarius_in_Nuweiba.jpg", caption="Dromedario",width=200)
    with an_ztu2:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Pharaoh_Eagle-owl.jpg/640px-Pharaoh_Eagle-owl.jpg", caption="Gufo reale del deserto", width=200)
    with an_ztu3:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/2009-03-07Vulpes_zerda028.jpg/640px-2009-03-07Vulpes_zerda028.jpg", caption="Fennec", width=200)
    # Crea tre colonne affiancate per gli ultimi 3 animali di questa zona
    an_ztu4, an_ztu5, an_ztu6 = sl.columns(3)
    with an_ztu4:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Common_yellow_scorpion_-_Buthus_occitanus.jpg/640px-Common_yellow_scorpion_-_Buthus_occitanus.jpg", caption="Scorpione giallo", width=200)
    with an_ztu5:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Hornviper_Cerastes_cerastes.jpg/640px-Hornviper_Cerastes_cerastes.jpg", caption="Vipera cornuta", width=200)
    with an_ztu6:
        sl.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Rhombomys_opimus_1.jpg/640px-Rhombomys_opimus_1.jpg", caption="Gerbillo", width=200)
    

# --- Sezione zona equatorial---
sl.subheader("zona equatoriale")

#FINITA
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
