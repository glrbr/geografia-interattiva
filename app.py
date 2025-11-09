import streamlit as st

# Configurazione pagina
st.set_page_config(page_title="Geografia Interattiva", page_icon="🌍", layout="wide")

# Carica CSS
def load_css():
    with open("styles/style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Inizializza session_state
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'
if 'zona_scelta' not in st.session_state:
    st.session_state.zona_scelta = None

# ========== HOMEPAGE ==========
if st.session_state.pagina == 'home':
    # Titolo solo con emoji
    st.markdown("<h1 style='text-align: center;'>🌍</h1>", unsafe_allow_html=True)
    
    # Mappa del mondo
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Map_of_the_world_with_countries_and_dependencies.svg/1024px-Map_of_the_world_with_countries_and_dependencies.svg.png")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 5 bottoni zone climatiche con IMMAGINI CLICCABILI
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<p style='text-align: center; font-size: 40px;'>❄️ 🔵</p>", unsafe_allow_html=True)
        if st.button("➡️ ❄️ 🔵", key="polare", use_container_width=True, width = "stretch", help="Zona Polare"):
            st.session_state.zona_scelta = 'polare'
            st.session_state.pagina = 'lezione'
            st.rerun()
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg/1024px-Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg")
    
    with col2:
        st.markdown("<p style='text-align: center; font-size: 40px;'>🌲 🟢</p>", unsafe_allow_html=True)
        if st.button("➡️ 🌲 🟢", key="subpolare", use_container_width=True, help="Zona Subpolare"):
            st.session_state.zona_scelta = 'subpolare'
            st.session_state.pagina = 'lezione'
            st.rerun()
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/640px-Fall_on_the_Yukon_Flats_NWR.jpg", 
                 use_container_width=True)
    
    with col3:
        st.markdown("<p style='text-align: center; font-size: 40px;'>🦁 🟡</p>", unsafe_allow_html=True)
        if st.button("➡️ 🦁 🟡", key="savana", use_container_width=True, help="Savana"):
            st.session_state.zona_scelta = 'savana'
            st.session_state.pagina = 'lezione'
            st.rerun()
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Savana_Bekol.jpg/640px-Savana_Bekol.jpg", 
                 use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col4, col5, col6 = st.columns([1, 1, 1])
    
    with col4:
        st.markdown("<p style='text-align: center; font-size: 40px;'>🌵 🟤</p>", unsafe_allow_html=True)
        if st.button("➡️ 🌵 🟤", key="deserto", use_container_width=True, help="Deserto"):
            st.session_state.zona_scelta = 'deserto'
            st.session_state.pagina = 'lezione'
            st.rerun()
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg/640px-Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg", 
                 use_container_width=True)
    
    with col5:
        st.markdown("<p style='text-align: center; font-size: 40px;'>🦜 🟢</p>", unsafe_allow_html=True)
        if st.button("➡️ 🦜 🟢", key="equatoriale", use_container_width=True, help="Foresta Equatoriale"):
            st.session_state.zona_scelta = 'equatoriale'
            st.session_state.pagina = 'lezione'
            st.rerun()
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Shaheed_Island%2C_Andamans%2C_Tropical_forest.jpg/640px-Shaheed_Island%2C_Andamans%2C_Tropical_forest.jpg", 
                 use_container_width=True)

elif st.session_state.pagina == 'lezione':
# Bottone Home in alto a sinistra
        col_back, col_space = st.columns([1, 5])
        # effetto pulsante back
        if st.button("➡️ 🏠", key="home_button"):
                st.session_state.pagina = 'home'
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # Dati zone climatiche (foto paesaggi)
        zone_dati = {
            'polare': {
                'emoji': '❄️',
                'colore': '🔵',
                'foto': [
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg/640px-Mt_Herschel%2C_Antarctica%2C_Jan_2006.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Icebreaker_in_greenland_2.JPG/640px-Icebreaker_in_greenland_2.JPG",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/00_2103_Pinguin_-_Petermann_Island_%28Antarktische_Halbinsel%29.jpg/640px-00_2103_Pinguin_-_Petermann_Island_%28Antarktische_Halbinsel%29.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Ursus_maritimus_in_Alaska.jpg/640px-Ursus_maritimus_in_Alaska.jpg"
                ]
            },
            'subpolare': {
                'emoji': '🌲',
                'colore': '🟢',
                'foto': [
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Fall_on_the_Yukon_Flats_NWR.jpg/640px-Fall_on_the_Yukon_Flats_NWR.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Wild_Grizzly_Bear.jpg/640px-Wild_Grizzly_Bear.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Canis_Lupus_Signatus_%282%29.JPG/640px-Canis_Lupus_Signatus_%282%29.JPG",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Carib%C3%BA_%28Rangifer_tarandus%29%2C_Parque_nacional_y_reserva_Denali%2C_Alaska%2C_Estados_Unidos%2C_2017-08-30%2C_DD_40.jpg/640px-Carib%C3%BA_%28Rangifer_tarandus%29%2C_Parque_nacional_y_reserva_Denali%2C_Alaska%2C_Estados_Unidos%2C_2017-08-30%2C_DD_40.jpg"
                ]
            },
            'savana': {
                'emoji': '🦁',
                'colore': '🟡',
                'foto': [
                    "https://upload.wikimedia.org/wikipedia/commons/f/f4/Savana_Bekol.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Lion_%28Panthera_leo%29_male_6y.jpg/640px-Lion_%28Panthera_leo%29_male_6y.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Burchell%27s_zebra_%28Equus_quagga_burchellii%29_2.jpg/640px-Burchell%27s_zebra_%28Equus_quagga_burchellii%29_2.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Giraffa_camelopardalis_angolensis.jpg/640px-Giraffa_camelopardalis_angolensis.jpg"
                ]
            },
            'deserto': {
                'emoji': '🌵',
                'colore': '🟤',
                'foto': [
                    "https://upload.wikimedia.org/wikipedia/commons/c/cb/Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Camelus_dromedarius_in_Nuweiba.jpg/640px-Camelus_dromedarius_in_Nuweiba.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/2009-03-07Vulpes_zerda028.jpg/640px-2009-03-07Vulpes_zerda028.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Echinocactus_grusonii_%28aka%29.jpg/640px-Echinocactus_grusonii_%28aka%29.jpg"
                ]
            },
            'equatoriale': {
                'emoji': '🦜',
                'colore': '🟢',
                'foto': [
                    "https://upload.wikimedia.org/wikipedia/commons/a/a5/Shaheed_Island%2C_Andamans%2C_Tropical_forest.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/113_Jaguar_in_Encontro_das_%C3%81guas_State_Park_Photo_by_Giles_Laurent.jpg/640px-113_Jaguar_in_Encontro_das_%C3%81guas_State_Park_Photo_by_Giles_Laurent.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Tucano_em_Campinas.jpg/640px-Tucano_em_Campinas.jpg",
                    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Scarlet_Macaw_at_Kuranda-1_%286285883802%29.jpg/640px-Scarlet_Macaw_at_Kuranda-1_%286285883802%29.jpg"
                ]
            }
        }

        zona = zone_dati[st.session_state.zona_scelta]

        # Mostra emoji e colore zona
        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{zona['emoji']} {zona['colore']}</h1>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Galleria foto in griglia 2x2
        col1, col2 = st.columns(2)

        with col1:
            st.image(zona['foto'][0], use_container_width=True)
            st.image(zona['foto'][2], use_container_width=True)

        with col2:
            st.image(zona['foto'][1], use_container_width=True)
            st.image(zona['foto'][3], use_container_width=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # Bottone TEST grande al centro
        col_space1, col_test, col_space2 = st.columns([1, 2, 1])
        with col_test:
            if st.button("✏️", key="vai_test"):
                st.session_state.pagina = 'test'
                st.rerun()