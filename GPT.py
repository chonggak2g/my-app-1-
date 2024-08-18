import requests
import streamlit as st
from streamlit_chat import message
import openai
import os

# OpenAI API 키 설정
openai.api_key = os.environ.get('OPENAI_API_KEY')  # 환경 변수에서 API 키 가져오기

# 시스템 지침 정의
system_instruction1 = '''고경력 베테랑 교감으로서 학교 생활 전반에 걸쳐 관리자로서의 경험과 지식이 풍부한 사람이야.
- 신규 발령 받은 교감에게 여러 가지 도움이 되는 조언을 해줄 수 있는 친절하고 상냥한 교감.'''

# 세션 스테이트 초기화
if 'messages' not in st.session_state:
    st.session_state['messages'] = [{
        "role": "assistant",
        "content": '안녕하세요! 신규 발령을 축하합니다! 어떤 고민이나 질문이 있으신가요?'
    }]

if 'stop' not in st.session_state:
    st.session_state['stop'] = False

def chat(text):
    messages = [{"role": "system", "content": system_instruction1}]
    messages.extend(st.session_state['messages'])
    user_turn = {"role": "user", "content": text}
    messages.append(user_turn)
    st.session_state['messages'].append(user_turn)

    # OpenAI API 호출
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages
    )

    assistant_messages = response['choices'][0]['message']['content']
    assistant_turn = {"role": "assistant", "content": assistant_messages}
    st.session_state['messages'].append(assistant_turn)

    return assistant_messages

# Streamlit 앱 타이틀
st.title('교감 상담 챗봇')

if not st.session_state['stop']:
    row1 = st.container()
    row2 = st.container()
    row3 = st.container()

    with row2:
        with st.form('form', clear_on_submit=True):
            input_text = st.text_input('당신의 질문 또는 고민을 입력하세요:')
            submitted = st.form_submit_button('전송')
            if submitted and input_text:
                chat(input_text)

    with row1:
        for i, msg_obj in enumerate(st.session_state['messages']):
            msg = msg_obj['content']
            is_user = (i % 2 == 1)  # 질문/응답 구분
            message(msg, is_user=is_user, key=i)

    with row3:
        if st.button('조언 받기'):
            recommendation = chat("위의 대화를 기반으로 신규 교감에게 도움이 되는 조언을 제시해줘.")
            st.success(recommendation)
            del st.session_state['messages']  # 메시지 초기화