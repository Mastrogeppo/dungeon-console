import streamlit as st

# 1. Recupero del Caster dal Battlefield
caster = st.session_state.get("caster", "Nessun Caster Selezionato")

# 2. Stile Dark & Gold per questa pagina
st.markdown(f"""
    <style>
    .stApp {{ background-color: #0e0e10; }}
    h1 {{ color: #d4af37; border-bottom: 2px solid #d4af37; }}
    .caster-box {{ 
        padding: 20px; 
        border: 2px solid #d4af37; 
        border-radius: 10px; 
        text-align: center;
        margin-bottom: 20px;
    }}
    </style>
    <div class="caster-box">
        <h2 style="color: #d4af37; margin: 0;">Console di Controllo</h2>
        <h1 style="color: #00ff00; margin: 5px;">{caster}</h1>
    </div>
""", unsafe_allow_html=True)

# 3. Gestione Round e Skill
col1, col2 = st.columns(2)

with col1:
    st.subheader("⚔️ Azioni Rapide")
    if st.button("Lancia Iniziativa"):
        st.success(f"{caster} è pronto al combattimento!")
    
    if st.button("Fine Turno"):
        st.info("Turno passato al prossimo combattente.")

with col2:
    st.subheader("📜 Skill Attive")
    # Esempio di skill (queste dovrebbero venire dal tuo database o session_state)
    skill_nome = "Scudo Arcano"
    round_rimanenti = st.number_input("Round rimanenti", value=3, min_value=0)
    
    if round_rimanenti == 0:
        st.markdown("<p style='color:red; font-weight:bold; animation: blinker 1s linear infinite;'>⚠️ SKILL SCADUTA!</p>", unsafe_allow_html=True)

# 4. Navigazione per tornare indietro
if st.button("⬅️ Torna al Battlefield"):
    st.switch_page("main.py")
