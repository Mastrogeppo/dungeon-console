import streamlit as st

# 1. Configurazione Iniziale
st.set_page_config(page_title="Dungeon Console", layout="wide")

# Inizializzazione Session State per il Caster e i Target
if 'caster' not in st.session_state:
    st.session_state.caster = "Nessuno"
if 'targets' not in st.session_state:
    st.session_state.targets = []

# 2. CSS Custom: Look Dark & Gold + Targeting Wizard
st.markdown("""
<style>
    .stApp { background-color: #0e0e10; color: #d4af37; }
    
    /* Colonne con colori tematici */
    [data-testid="column"]:nth-child(1) { border-left: 2px solid #228b22; padding-left: 15px; }
    [data-testid="column"]:nth-child(2) { border-left: 2px solid #d4af37; padding-left: 15px; }
    [data-testid="column"]:nth-child(3) { border-left: 2px solid #8b0000; padding-left: 15px; }

    /* Targeting Wizard: Checkbox dorate e segno verde */
    input[type="checkbox"] {
        accent-color: #00ff00;
        transform: scale(1.3);
    }
    
    /* Colori nomi */
    .nome-pg { color: #00ff00; font-weight: bold; }
    .nome-png { color: #d4af37; font-weight: bold; }
    .nome-nemico { color: #8b0000; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ DUNGEON BATTLEFIELD")

# 3. Logica Targeting (Opzione NESSUNO)
def reset_targets():
    st.session_state.targets = []

# 4. Layout a 3 Colonne
col_pg, col_png, col_enemy = st.columns(3)

with col_pg:
    st.markdown("<h3 class='nome-pg'>PERSONAGGI (PG)</h3>", unsafe_allow_html=True)
    pg_list = ["Guerriero", "Mago", "Ladro"]
    for pg in pg_list:
        if st.checkbox(pg, key=f"check_{pg}"):
            if pg not in st.session_state.targets: st.session_state.targets.append(pg)
        
        if st.button(f"🎮 Gestisci {pg}"):
            st.session_state.caster = pg
            st.switch_page("pages\1_Console.py")

with col_png:
    st.markdown("<h3 class='nome-png'>ALLEATI (PNG)</h3>", unsafe_allow_html=True)
    png_list = ["Guaritore", "Scorta Reale"]
    for png in png_list:
        st.checkbox(png, key=f"check_{png}")

with col_enemy:
    st.markdown("<h3 class='nome-nemico'>NEMICI</h3>", unsafe_allow_html=True)
    enemy_list = ["Orco A", "Orco B", "Sciamano"]
    for en in enemy_list:
        st.checkbox(en, key=f"check_{en}")

# 5. Barra Inferiore: Wizard Control
st.divider()
c1, c2, c3 = st.columns([2, 1, 1])

with c1:
    st.write(f"**Caster Attuale:** :green[{st.session_state.caster}]")

with c2:
    if st.button("⚪ RESET TARGETS (NESSUNO)"):
        reset_targets()
        st.rerun()

with c3:
    if st.button("⚔️ VAI ALLA CONSOLE"):
        st.switch_page("pages\1_Console.py")
