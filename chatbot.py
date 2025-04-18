import streamlit as st
import google.generativeai as genai
import random
import os

# Substitua pela sua chave de API Gemini
genai.configure(api_key=os.getenv("SUA_GEMINI_API_KEY"))

modelo = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")



sugestoes_gerais = [
    "Feche os olhos por 5 segundos e foque apenas no som da sua respiração, mesmo com o barulho ao redor.",
    "Tente relaxar a mandíbula, os ombros e as mãos — tensionamos isso sem perceber.",
    "Lembre-se: o que está ao seu redor é temporário. Respire fundo e repita mentalmente: 'Eu estou segura agora.'",
    "Desvie sua atenção do caos ao redor e foque em algo pequeno e fixo — como um objeto no bolso ou uma cor no ambiente.",
    "Coloque uma música ou som calmo com fone de ouvido, se possível, mesmo que seja por 1 minuto.",
    "Faça 3 respirações lentas e conscientes.",
    "Toque seu pulso ou aperte levemente sua mão. Isso pode ajudar a ancorar você no presente.",
    "Feche os olhos por alguns segundos e pense em um lugar onde você se sente segura — visualize esse lugar.",
    "Mentalize uma frase curta como 'Eu vou passar por isso', ou 'O barulho está fora, minha calma está dentro'.",
    "Se puder, tire um tempinho para ir ao banheiro ou tomar uma água — são pequenas pausas que renovam.",
]



# Sugestões específicas para lugares caóticos
sugestoes_caoticas = [
    "Relaxe a mandíbula, os ombros e as mãos. Você pode fazer isso agora mesmo, onde estiver.",
    "Foque por 5 segundos em um objeto ao seu redor. Traga sua mente para o presente.",
    "Repita mentalmente: 'Eu posso passar por isso. Minha calma está comigo.'",
    "Feche os olhos por 5 segundos, mesmo com barulho. Só foque no som da sua respiração.",
    "Se possível, coloque um fone e ouça um som que te traga paz — mesmo que seja só por 1 minuto.",
]


# Detecta se a situação descrita é caótica
def detectar_situacao(mensagem):
    mensagem = mensagem.lower()
    palavras_caoticas = ["ônibus", "trabalho", "barulho", "gente", "festa", "ruído", "fila", "metrô", "lugar cheio", "aperto", "não posso sair"]

    for palavra in palavras_caoticas:
        if palavra in mensagem:
            return "caotico"
    return "geral"


# Interface com Streamlit
st.set_page_config(page_title="YourBuddy 🌿", layout="centered")
st.title("🧘 YourBuddy - Desabafe sem julgamentos 🌿")
st.markdown("Sinta-se à vontade para desabafar. O YourBuddy vai te ouvir com carinho e cuidado 💛")

mensagem = st.text_area("Como você está se sentindo agora?", height=150)


if st.button("Enviar"):
    with st.spinner("YourBuddy está refletindo com carinho..."):
        prompt = f"""
        Você é um chatbot terapêutico, acolhedor e empático.
        A pessoa desabafou o seguinte: "{mensagem}"

        Responda com acolhimento, com até 4 frases. 
        Use uma linguagem leve e reconfortante, como um terapeuta gentil, sem dar diagnósticos clínicos.
        """
        resposta = modelo.generate_content(prompt)

        st.success("💬 Resposta do YourBuddy:")
        st.markdown(f"> {resposta.text.strip()}")

        tipo = detectar_situacao(mensagem)
        sugestao = random.choice(sugestoes_caoticas if tipo == "caotico" else sugestoes_gerais)
        st.markdown("🌿 **Dica de autocuidado:**")
        st.info(sugestao)