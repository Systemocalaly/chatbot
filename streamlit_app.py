import streamlit as st
import openai

st.set_page_config(
        page_title="Asystent Macieja", 
        page_icon="🤖", 
        layout="centered")

st.title("🤖 Asystent AI dla Macieja")
st.markdown("Zadaj pytanie, a agent odpowie jak Twój osobisty doradca biznesowy.")

# ⇣ klucz z secrets.toml
openai_api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI(api_key=openai_api_key)

# inicjalizacja historii czatu
if "messages" not in st.session_state:
    st.session_state.messages = [
            {
                        "role": "system",
                                    "content": (
                                                    "Jesteś profesjonalnym doradcą AI Macieja. "
                                                                    "Odpowiadasz konkretnie, rzeczowo, w języku polskim."
                                                                                )
                                                                                        }
                                                                                            ]

                                                                                            # wyświetl dotychczasową historię
for m in st.session_state.messages:
                                                                                                with st.chat_message(m["role"]):
                                                                                                        st.write(m["content"])

                                                                                                        # pole wejściowe
                                                                                                        prompt = st.chat_input("Zadaj pytanie…")

                                                                                                        if prompt:
                                                                                                            # dodaj pytanie użytkownika do historii
                                                                                                                st.session_state.messages.append({"role": "user", "content": prompt})
                                                                                                                with st.chat_message("user"):
                                                                                                                    st.write(prompt)

                                                                                                                                # wysyłka do OpenAI
with st.spinner("Myślę…"):
                                                                                                                                            reply = client.chat.completions.create(
                                                                                                                                                        model="gpt-3.5-turbo",
                                                                                                                                                                    messages=st.session_state.messages
                                                                                                                                                                            ).choices[0].message.content

                                                                                                                                                                                # pokaż i zapisz odpowiedź
st.session_state.messages.append({"role": "assistant", "content": reply})
with st.chat_message("assistant"):
                                                                                                                                                                                                st.write(reply)
                                                                                                                                                                                                # 4️⃣ 📝  ZAPISZ HISTORIĘ  
st.session_state.chat_log =st.session_state.messages