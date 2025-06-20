from openai import OpenAI



if __name__ == '__main__':
    # 调用远程模型 key
    API_KEY = "b7cd18fd95214219beeb7a9478bf01f6.6Lz9lnGlgMQfB8OK"
    # 路径
    ASE_URL="https://open.bigmodel.cn/api/paas/v4"

    # 初始化chat
    client = OpenAI(
        api_key=API_KEY,
        base_url=ASE_URL
    )

    # 开始调用模型接口进行对话
    response = client.chat.completions.create(
        model="glm-4-flash-250414",
        messages=[
            {"role": "user", "content": "天空的颜色与什么相关"}
        ],
        temperature=0.3
    )
    print(response.choices[0].message.content)


