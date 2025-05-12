from openai import AsyncOpenAI as asyncAI

token = "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"

client = asyncAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=token,
)


async def generate_text(prompt):
    completion = await client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content
