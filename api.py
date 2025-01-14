import openai, consts
from datetime import datetime


def openai_call(prompt, temperature=0.4, max_tokens=200, role="assistant"):
    messages = [
        {
            "role": "system",
            "content": f"You are BabyAGI-asi, an Autonomous and Self-Improving LLM-based agent. There are no users, just BabyAGI. Strictly follow your objective. Today's date: {datetime.now().strftime('%d/%m/%Y')}. Knowledge cut-off: set/2021."
            if role == "assistant"
            else "You are BabyAGI-asi, you must strictly follow the user's intructions",
        },
        {"role": role, "content": prompt},
    ]
    # print(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo" if not consts.USE_GPT4 else "gpt-4",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
    )
    text = response.choices[0].message.content.strip()
    return text
