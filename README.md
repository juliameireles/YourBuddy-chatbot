# 🧘 YourBuddy - Chatbot Terapêutico com IA 🌿

**YourBuddy** é um chatbot terapêutico feito com **Python**, **Streamlit** e **Gemini AI (Google)**.  
Ele oferece um espaço de escuta acolhedor para quem está passando por estresse, ansiedade ou momentos difíceis, e ainda sugere dicas suaves de autocuidado com base no que você escreve 💛

---

## ✨ Funcionalidades

- 💬 Responde com empatia e acolhimento usando IA (Gemini)
- 🌱 Sugere práticas de autocuidado personalizadas
- 🌪️ Identifica situações caóticas (ex: ônibus, barulho, trabalho)
- 🧘‍♀️ Interface simples e leve feita com Streamlit

---

## 💻 Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/juliameireles/YourBuddy-chatbot.git
cd YourBuddy-chatbot
```

### 2. (Opcional) Crie e ative um ambiente virtual

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Adicione sua chave da API do Gemini

No arquivo `chatbot.py`, substitua:

```python
genai.configure(api_key="SUA_CHAVE_AQUI")
```

pela sua chave real (obtenha em [ai.google.dev](https://ai.google.dev)).

---

### 5. Rode o app

```bash
streamlit run chatbot.py
```

---

## 📦 Dependências

- `streamlit`
- `google-generativeai`
- `random` (nativo do Python)

---

## 🌈 Exemplo de uso

```text
Você: estou me sentindo ansiosa e com medo do futuro

YourBuddy: É natural se sentir assim às vezes. Respire fundo e lembre-se que você está fazendo o melhor que pode 💛

Dica de autocuidado:
Feche os olhos por 5 segundos e foque apenas no som da sua respiração, mesmo com o barulho ao redor.
```

---

## 🧡 Sobre

Este projeto foi criado por [Seu Nome] com carinho, com o objetivo de oferecer conforto e apoio em momentos difíceis. 


**Não substitui acompanhamento terapêutico profissional.**
