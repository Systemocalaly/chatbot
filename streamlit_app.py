import streamlit as st
import openai

st.set_page_config(page_title="Asystent Macieja", page_icon="🤖")

st.title("🤖 Asystent AI dla Macieja")
st.markdown("Zadaj pytanie, a agent odpowie jak Twój osobisty doradca biznesowy.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "Jesteś profesjonalnym doradcą AI Macieja. Mów konkretnie, zwięźle i z biznesowym nastawieniem."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Zadaj pytanie...")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("Myślę..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
    reply = response.choices[0].message.content
    st.chat_message("assistant").write(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})