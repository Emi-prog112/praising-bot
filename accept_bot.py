from openai import OpenAI

import os
# 環境変数から読み込む設定
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# 2. ボットの役割を定義（システムプロンプト）
system_prompt = "あなたは世界一優しいメンタルケアの専門家です。ユーザーのどんな発言も徹底的に肯定し、自己肯定感を高める温かい言葉で返答してください。"

print("ボットが起動しました。何か話しかけてね！")

while True:
    user_input = input("あなた: ")
    if user_input == "終了":
        break
    
    # 3. AIにメッセージを送る
    response = client.chat.completions.create(
        model="gpt-4o", # 最新のモデルがおすすめ
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    
    print(f"ボット: {response.choices[0].message.content}")
