from transformers import pipeline

ia = pipeline(
    'text-generation', 
    model = 'Qwen/Qwen2.5-1.5b-Instruct'
    )

prompt = """ 
Digamos que você é um professsor de programação.

Responda a pergunta: A quanto tempo e como surgiu o Java?

Resposta:
"""

resposta = ia(
    prompt, max_new_tokens = 500, 
    temperature = 0.3
    )

print(resposta[0]['generated_text'])