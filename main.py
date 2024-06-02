import re

# Dicionário com as perguntas e respostas
faq = {
    "qual é o seu nome?": "Meu nome é João.",
    "qual é a sua idade?": "Eu tenho 30 anos.",
    "qual é o seu endereço?": "Meu endereço é Rua ABC, 123, Cidade X, Estado Y, CEP 12345-678.",
    "qual é o seu telefone?": "Meu telefone é (11) 98765-4321.",
    "qual é o seu email?": "Meu email é joao@exemplo.com.",
    "qual é o seu cpf?": "Meu CPF é 123.456.789-00.",
    "qual é a sua profissão?": "Eu sou desenvolvedor de software."
}

# Função para responder às perguntas do usuário
def responder_pergunta(pergunta):
    # Converte a pergunta em minúsculas para facilitar a comparação
    pergunta_lower = pergunta.lower()

    # Verifica se a pergunta está no dicionário de perguntas e respostas
    if pergunta_lower in faq:
        return faq[pergunta_lower]
    else:
        # Se a pergunta não estiver no dicionário, tenta encontrar a resposta usando regex
        for key in faq:
            if re.search(key, pergunta_lower):
                return faq[key]
        return "Desculpe, não entendi a sua pergunta."

# Loop principal do chatbot
while True:
    pergunta = input("Você: ")
    resposta = responder_pergunta(pergunta)
    print("Chatbot: " + resposta)