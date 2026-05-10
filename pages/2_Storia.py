import streamlit as st

# 1. Stile Grafico: Pergamena Antica o Dark Blizzard
st.markdown("""
    <style>
    .stApp { background-color: #0e0e10; }
    .story-entry {
        background-color: #1c1c1e;
        border-left: 4px solid #d4af37;
        padding: 15px;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .round-label {
        color: #d4af37;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.8em;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📜 Cronache del Dungeon")

# 2. Inizializzazione Log (se non esiste)
if 'log_storia' not in st.session_state:
    st.session_state.log_storia = [
        {"round": 1, "evento": "Inizio dello scontro nelle Catacombe."},
        {"round": 1, "evento": "Il Guerriero attiva 'Muro di Scudi'."}
    ]

# 3. Area di inserimento note per il DM
with st.expander("✍️ Aggiungi Nota alla Storia"):
    nuova_nota = st.text_area("Cosa è successo?")
    if st.button("Annota nel Diario"):
        if nuova_nota:
            # Aggiunge in cima alla lista (ordine cronologico inverso)
            st.session_state.log_storia.insert(0, {"round": "??", "evento": nuova_nota})
            st.rerun()

# 4. Visualizzazione Log
st.subheader("Eventi Recenti")

for entry in st.session_state.log_storia:
    st.markdown(f"""
        <div class="story-entry">
            <span class="round-label">Round {entry['round']}</span><br>
            <span style="color: #e0e0e0;">{entry['evento']}</span>
        </div>
    """, unsafe_allow_html=True)

# 5. Navigazione
if st.sidebar.button("⬅️ Torna al Battlefield"):
    st.switch_page("main.py")
