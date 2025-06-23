import ollama

models = ollama.list()

model_name = 'deepseek-r1:8b'

if model_name not in models:
    print(f"The model that is used in this code {model_name} is NOT on your device")
    raise RuntimeError(f"Model \"{model_name}\" not found. Halting execution.")


response = ollama.chat(
    model='deepseek-r1:8b',
    messages=[
        {
            "role": "system",
            "content": (
                "You are a bilingual editor. Your task is to improve sloppy English translations "
                "by comparing them with the original Chinese text. Make the English natural, fluent, "
                "and faithful to the meaning in Chinese."
            )
        },
        {
            "role": "user",
            "content": (
                "Original Chinese: 他昨天去了市场。\n"
                "Machine Translated English: He go to market yesterday."
            )
        }
    ]
)

print(response['message']['content'])
