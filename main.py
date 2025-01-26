import os
from dotenv import load_dotenv
from nltk.chat.util import Chat, reflections

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o nome do banco de dados do arquivo .env
DB_NAME = os.getenv("DB_NAME", "chatbot.db")

# Define os padrões de conversa e respostas
pairs = [
    [
        r'oi|ol[áa]|olha|ei',
        [
            "Oi! Tudo bem? Qual é o seu nome?",
            "Olá! Estou aqui para conversar com você. Qual é o seu nome?",
        ],
    ],
    [
        r'meu nome é ([\w\s]+)',
        [
            "Prazer em te conhecer, %1! Qual é o seu endereço?",
            "Ótimo, %1! Agora, por favor, me diga seu endereço.",
        ],
    ],
    [
        r'meu endereço é ([\w\s,\\-\\.]+)',
        [
            "Entendido, %1! Obrigado pelas informações. Foi um prazer conversar!",
            "Obrigado, %1! Até logo!",
        ],
    ],
    [
        r'adeus|tchau',
        [
            "Tchau! Foi bom conversar com você. Até logo!",
            "Adeus! Volte sempre que precisar.",
        ],
    ],
    [
        r'(.*)',
        [
            "Desculpe, não entendi. Você poderia repetir de outra forma?",
            "Hmm, pode ser mais específico?",
        ],
    ],
]

# Classe do Chatbot
class Chatbot:
    def __init__(self, pairs, reflections):
        self.chat = Chat(pairs, reflections)
        self.user_name = None
        self.user_address = None

    def start_chat(self):
        print("Bem-vindo! Sou um chatbot.")
        
        # Pergunta o nome do usuário
        self.user_name = input("Chatbot: Qual é o seu nome? ").strip()
        print(f"Chatbot: Prazer em te conhecer, {self.user_name}!")

        # Pergunta o endereço do usuário
        self.user_address = input("Chatbot: Qual é o seu endereço? ").strip()
        print(f"Chatbot: Entendido, {self.user_address}! Obrigado pelas informações.")

        # Encerra a conversa
        print("Chatbot: Foi um prazer conversar! Até logo!")

# Inicializa e inicia o chatbot
if __name__ == "__main__":
    chatbot = Chatbot(pairs, reflections)
    chatbot.start_chat()