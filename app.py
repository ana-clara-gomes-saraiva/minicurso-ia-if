import streamlit as st

st.set_page_config(page_title="Calculadora de Notas", page_icon="🌸")

# CSS (mantive o seu)
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
st.markdown('<div class="texto">Preencha as notas por categoria</div>', unsafe_allow_html=True)

st.subheader("📚 Notas por avaliação")

# Caderno
st.markdown("### 📒 Caderno")
c1 = st.number_input("Nota 1", 0.0, 10.0, step=0.1, key="c1")
c2 = st.number_input("Nota 2", 0.0, 10.0, step=0.1, key="c2")
media_caderno = (c1 + c2) / 2

# Trabalhos
st.markdown("### 📝 Trabalhos")
t1 = st.number_input("Nota 1 ", 0.0, 10.0, step=0.1, key="t1")
t2 = st.number_input("Nota 2 ", 0.0, 10.0, step=0.1, key="t2")
media_trabalhos = (t1 + t2) / 2

# Prova
st.markdown("### 📊 Prova")
p1 = st.number_input("Prova 1", 0.0, 10.0, step=0.1)
p2 = st.number_input("Prova 2", 0.0, 10.0, step=0.1)
media_prova = (p1 + p2) / 2

# Atitudinal
st.markdown("### 🌟 Atitudinal")
atitudinal = st.number_input("Nota Atitudinal", 0.0, 10.0, step=0.1)

# Botão
if st.button("Calcular Média 💖"):

    # Média final ponderada
    media_final = (
        media_caderno * 0.2 +
        media_trabalhos * 0.2 +
        media_prova * 0.5 +
        atitudinal * 0.1
    )

    # Status
    if media_final >= 7:
        status = "Aprovado 😄"
        cor = "#4CAF50"
    elif media_final >= 5:
        status = "Recuperação 😐"
        cor = "#FFC107"
    else:
        status = "Reprovado 😢"
        cor = "#F44336"

    # Mostrar médias por categoria
    st.write("### 📊 Detalhamento")
    st.write(f"Caderno: {media_caderno:.2f}")
    st.write(f"Trabalhos: {media_trabalhos:.2f}")
    st.write(f"Prova: {media_prova:.2f}")
    st.write(f"Atitudinal: {atitudinal:.2f}")

    # Card final
    st.markdown(f"""
    <div class="card" style="background-color:{cor};">
        🎀 Média Final: {media_final:.2f} <br><br>
        {status}
    </div>
    """, unsafe_allow_html=True)
