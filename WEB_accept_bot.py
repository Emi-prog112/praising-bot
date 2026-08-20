import streamlit as st
from openai import OpenAI

# ページのタイトルを設定
st.title("💖 やさしい肯定チャットボット")
st.write("あなたの愚痴や不安を何でも聞いて、全力で肯定して癒やしてくれるボットです。")

import os
# 環境変数から読み込む設定
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# ボットの役割（システムプロンプト）
system_prompt = "あなたは世界一優しいメンタルケアの専門家です。ユーザーのどんな発言も徹底的に肯定し、自己肯定感を高める温かい言葉で返答してください。"

# チャットの履歴を保存する箱をブラウザ上に用意する（これがないと画面を更新した時に会話が消えちゃいます）
if "messages" not in st.session_state:
    st.session_state.messages = []

# 過去のチャット履歴を画面に表示する
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーが画面下の入力欄に文字を打って送信したときの処理
if user_input := st.chat_input("今の気持ちや愚痴を話してね..."):
    
    # 1. ユーザーの発言を履歴に追加して画面に表示
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 2. AIからの返信を取得
    # これまでの会話の文脈をすべてAIに渡すようにしています
    messages_for_api = [{"role": "system", "content": system_prompt}]
    for m in st.session_state.messages:
        messages_for_api.append({"role": m["role"], "content": m["content"]})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages_for_api
    )
    
    bot_response = response.choices[0].message.content

    # 3. AIの返信を履歴に追加して画面に表示
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)

