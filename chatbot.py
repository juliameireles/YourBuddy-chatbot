import streamlit as st
import google.generativeai as genai
import random
import os

# Substitua pela sua chave de API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

modelo = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")



sugestoes_gerais = [
     "Se puder, tome um banho quente com calma, prestando atenção na água tocando seu corpo.",
    "Coloque uma música leve, deite em um lugar confortável e apenas respire por alguns minutos.",
    "Escreva em um caderno como você está se sentindo — sem censura, só coloque pra fora.",
    "Deite por 30 minutos, mesmo que não consiga dormir. Permita que seu corpo descanse.",
    "Acenda uma vela ou incenso suave e fique em silêncio por alguns instantes, com os olhos fechados.",
    "Beba algo quente, como um chá, e aproveite o momento presente sem pressa.",
    "Faça alongamentos lentos, respeitando seus limites, prestando atenção em como seu corpo responde.",
    "Assista um filme ou série leve, que te traga conforto — não precisa ser produtiva agora.",
    "Desligue o celular por um tempo e se desconecte do excesso de estímulos. Seu mundo interior também merece atenção.",
    "Abra a janela, respire o ar de fora, sinta a temperatura no seu rosto. Você está aqui, e está tudo bem.",
]



# Sugestões específicas para lugares caóticos
sugestoes_caoticas = [
   "Relaxe a mandíbula, os ombros e as mãos. Você pode fazer isso agora mesmo, onde estiver.",
    "Foque por 5 segundos em um objeto ao seu redor. Traga sua atenção pra ele e permita que sua mente respire.",
    "Repita mentalmente: 'Eu posso passar por isso. Minha calma está comigo.'",
    "Feche os olhos por 3 a 5 segundos (se for seguro). Mesmo no barulho, sua respiração pode ser seu refúgio.",
    "Se possível, coloque um fone e ouça um som que te acalme — mesmo que seja só por 1 minuto.",
    "Enquanto estiver parada, firme os pés no chão e sinta o apoio da terra sob você. Você está segura.",
    "Solte o ar devagar pela boca como se estivesse suspirando. Esse gesto simples pode aliviar tensões escondidas.",
    "Massageie levemente sua palma com o polegar. Esse toque sutil pode trazer conforto, mesmo em silêncio.",
    "Mentalize um lugar calmo que você ama. Mesmo em meio ao caos, você pode se visitar internamente.",
    "Incline levemente a cabeça para o lado, alongando o pescoço, e respire fundo. Pequenos gestos também cuidam de você."
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