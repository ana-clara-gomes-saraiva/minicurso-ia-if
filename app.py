import streamlit as st

st.set_page_config(page_title="Calculadora de Notas", page_icon="🌸")

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

.stApp {
    background-color: #fff0f5;
    background-image: radial-gradient(#ffc0cb 1px, transparent 1px);
    background-size: 20px 20px;
}

.titulo {
    font-family: 'Pacifico', cursive;
    font-size: 42px;
    text-align: center;
    color: #d63384;
}

.texto {
    font-family: 'Quicksand', sans-serif;
    text-align: center;
    font-size: 18px;
    color: #555;
}

.card {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 22px;
    font-weight: bold;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<div class="titulo">🌸 Calculadora de Notas do IF 🎀</div>', unsafe_allow_html=True)
st.markdown('<div class="texto">Preencha todas as categorias</div>', unsafe_allow_html=True)

# Inputs organizados
st.subheader("📚 Notas")

col1, col2 = st.columns(2)

with col1:
    caderno = st.number_input("📒 Caderno", 0.0, 10.0, step=0.1)
    trabalhos = st.number_input("📝 Trabalhos", 0.0, 10.0, step=0.1)

with col2:
    prova = st.number_input("📊 Prova", 0.0, 10.0, step=0.1)
    atitudinal = st.number_input("🌟 Atitudinal", 0.0, 10.0, step=0.1)

# Botão
if st.button("Calcular Média 💖"):

    # Pesos (você pode ajustar)
    media = (
        caderno * 0.2 +
        trabalhos * 0.2 +
        prova * 0.5 +
        atitudinal * 0.1
    )

    # Definição visual
    if media >= 7:
        status = "Aprovado 😄"
        cor = "#4CAF50"
    elif media >= 5:
        status = "Recuperação 😐"
        cor = "#FFC107"
    else:
        status = "Reprovado 😢"
        cor = "#F44336"

    # Card resultado
    st.markdown(f"""
    <div class="card" style="background-color:{cor};">
        🎀 Média Final: {media:.2f} <br><br>
        {status}
    </div>
    """, unsafe_allow_html=True)
