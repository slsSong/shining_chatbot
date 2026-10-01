# import streamlit as st
# # st.title("Shining_Chatbot")
# # st.write("챗봇을 준비하고 있습니다.")

# # 페이지만 만들고 -> 깃허브에 올려봅시다
# # 10분 정도 드릴테니


# # 입력창과 응답 화면 테스트
# user_input = st.chat_input("메시지를 입력하세요.")

import os
import streamlit as st
from langchain.chat_models import init_chat_model

# st.title("Shining Chatbot")

# st.title("😎 나의 첫번째 챗봇")
# st.write("streamlt으로 만든 챗봇 페이지 입니다.")

st.set_page_config(page_title="산업재해 데이터 인사이트",
                   layout="wide"
                   )
st.title("산업재해 데이터 인사이트")
st.caption("산업재해 데이터 현황을 살펴보고, 근거자료 기반 질의응답으로 확장하는 프로젝트")


# api_key = st.secrets["OPENAI_API_KEY"]

model = init_chat_model(
    model="gpt-6-luna",
    reasoning_effort="none",
    api_key=st.secrets["OPENAI_API_KEY"]
)


# model = ChatOpenAI(model="gpt-6-luna")
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
user_input = st.chat_input("메시지를 입력하세요.")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    answer = model.invoke(user_input).content
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
