import random
import re
import time


def create_password():
    # Lista de palavras para gerar sugestões de senha
    words = ["Python", "Segurança", "Proteção", "Privacidade", "Cibersegurança",
             "Senha", "Hacker", "Firewall", "Antivírus"]

    # Gera sugestão de senha aleatória
    suggestion = random.choice(words) + str(random.randint(1, 100)) + random.choice("!@#$%^&*()_+-={};:'\"|,.<>/?~`")

    # Imprime sugestão de senha
    print("Sugestão de senha: " + suggestion)

    # Pede ao usuário para criar uma senha
    password = input("Crie uma senha forte: ")

    # Verifica se a senha atende aos requisitos
    if len(password) < 8:
        print("Sua senha deve ter pelo menos 8 caracteres.")
        return False
    elif not re.search("[a-z]", password):
        print("Sua senha deve conter pelo menos uma letra minúscula.")
        return False
    elif not re.search("[A-Z]", password):
        print("Sua senha deve conter pelo menos uma letra maiúscula.")
        return False
    elif not re.search("[0-9]", password):
        print("Sua senha deve conter pelo menos um número.")
        return False
    elif not re.search("[!@#$%^&*()_+-={};:'\"|,.<>/?~`]", password):
        print("Sua senha deve conter pelo menos um caractere especial.")
        return False
    else:
        print("Senha criada com sucesso!")
        return True


def animate_password_strength(password):
    password_strength = 0
    lives = len(password) // 2
    for char in password:
        if char.isalpha():
            password_strength += 1
            lives += 1
        elif char.isdigit():
            password_strength += 2
            lives += 1
        else:
            password_strength += 3
            lives += 2
        print("Senha: " + "*" * password_strength)
        time.sleep(1)
    print("\nVidas: " + "❤️" * lives)


# Função principal do programa
def main():
    print("Bem-vindo ao criador de senhas!")
    while True:
        if create_password():
            print("\nSenha criada com sucesso!\n")
            password = input("Digite a senha que você criou: ")
            print("\nAnalisando a senha...\n")
            animate_password_strength(password)
            print("\nParabéns! Você criou uma senha forte e segura.\n")
        else:
            print("\nTente novamente.\n")


if __name__ == "__main__":
    main()
