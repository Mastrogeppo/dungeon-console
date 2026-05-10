import streamlit as st

# 1. Configurazione Iniziale
st.set_page_config(page_title="Dungeon Console", layout="wide", initial_sidebar_state="collapsed")

# Inizializzazione Session State
if 'caster' not in st.session_state:
    st.session_state.caster = "Nessuno"
if 'targets' not in st.session_state:
    st.session_state.targets = []

# 2. CSS Custom: Look Dark & Gold + Targeting Wizard
st.markdown("""
<style>
    .stApp { background-color: #0e0e10; color: #d4af37; }
    
    /* Colonne con bordi colorati */
    [data-testid="column"]:nth-child(1) { border-left: 3px solid #228b22; padding-left: 20px; }
    [data-testid="column"]:nth-child(2) { border-left: 3px solid #d4af37; padding-left: 20px; }
    [data-testid="column"]:nth-child(3) { border-left: 3px solid #8b0000; padding-left: 20px; }

    /* Stile Label Checkbox */
    label[data-testid="stWidgetLabel"] p {
        font-size: 1.1rem !important;
        font-weight: 500;
    }

    /* Targeting Wizard: Checkbox dorate e segno verde */
    input[type="checkbox"] {
        accent-color: #00ff00;
        transform: scale(1.2);
    }
    
    /* Classi colori nomi */
    .nome-pg { color: #00ff00; font-weight: bold; text-shadow: 1px 1px 2px black; }
    .nome-png { color: #d4af37; font-weight: bold; text-shadow: 1px 1px 2px black; }
    .nome-nemico { color: #ff4b4b; font-weight: bold; text-shadow: 1px 1px 2px black; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ DUNGEON BATTLEFIELD")

# 3. Funzioni di Supporto
def update_target(name, key):
    """Aggiunge o rimuove il target dalla lista globale in base allo stato del checkbox"""
    if st.session_state[key]:
        if name not in st.session_state.targets:
            st.session_state.targets.append(name)
    else:
        if name in st.session_state.targets:
            st.session_state.targets.remove(name)

def reset_all():
    """Pulisce tutti i target resettando i checkbox tramite session_state"""
    for key in st.session_state.keys():
        if key.startswith("check_"):
            st.session_state[key] = False
    st.session_state.targets = []

# 4. Layout a 3 Colonne
col_pg, col_png, col_enemy = st.columns(3)

with col_pg:
    st.markdown("<h3 class='nome-pg'>PERSONAGGI (PG)</h3>", unsafe_allow_html=True)
    pg_list = ["Guerriero", "Mago", "Ladro"]
    for pg in pg_list:
        key = f"check_{pg}"
        st.checkbox(pg, key=key, on_change=update_target, args=(pg, key))
        
        if st.button(f"🎮 Gestisci {pg}", use_container_width=True):
            st.session_state.caster = pg
            st.switch_page("1_Console.py") # Assicurati che il path sia corretto

with col_png:
    st.markdown("<h3 class='nome-png'>ALLEATI (PNG)</h3>", unsafe_allow_html=True)
    png_list = ["Guaritore", "Scorta Reale"]
    for png in png_list:
        key = f"check_{png}"
        st.checkbox(png, key=key, on_change=update_target, args=(png, key))

with col_enemy:
    st.markdown("<h3 class='nome-nemico'>NEMICI</h3>", unsafe_allow_html=True)
    enemy_list = ["Orco A", "Orco B", "Sciamano"]
    for en in enemy_list:
        key = f"check_{en}"
        st.checkbox(en, key=key, on_change=update_target, args=(en, key))

# 5. Barra Inferiore: Wizard Control
st.divider()
c1, c2, c3 = st.columns([2, 1, 1])

with c1:
    st.write(f"**Caster Attuale:** :green[{st.session_state.caster}]")
    t_list = ", ".join(st.session_state.targets) if st.session_state.targets else "Nessuno"
    st.write(f"**Target Selezionati:** :red[{t_list}]")

with c2:
    if st.button("⚪ RESET TARGETS", use_container_width=True):
        reset_all()
        st.rerun()

with c3:
    if st.button("⚔️ VAI ALLA CONSOLE", type="primary", use_container_width=True):
        if st.session_state.caster == "Nessuno":
            st.error("Seleziona un Caster prima!")
        else:
            st.switch_page("pages/1_Console.py")

