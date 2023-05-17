import time
import re

def animate_bonequinho(steps):
    for i in range(steps):
        print(" "*(i+1) + "( o.o )")
        print(" "*(i+1) + "=\\_t_/=")
        print(" "*(i+1) + "  ! !")
        time.sleep(0.5)
        print("\033[F\033[F\033[F")
        print(" "*(i+1) + "( o.o )")
        print(" "*(i+1) + "=\\_t_/=")
        print(" "*(i+1) + "  ! !")
        time.sleep(0.5)
        print("\033[F\033[F\033[F")

def create_password():
    # Lista de palavras para gerar sugestões de senha
    words = ["Python", "Segurança", "Proteção", "Privacidade", "Cibersegurança", "Senha", "Hacker", "Firewall", "Antivírus"]

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

def play_game(password):
    animate_bonequinho(len(password))
    lives = len(password)//2 + 1 # Define a quantidade de corações com base no tamanho da senha
    print("Você tem {} vidas para criar a senha".format(lives))
    rules = 0
    for i, char in enumerate(password):
        print("Senha atual: " + "*"*(i) + char + "*"*(len(password)-i-1))
        while True:
            attempt = input("Digite a letra da posição {}: ".format(i+1))
            if attempt == char:
                print("Acertou!")
                rules += 1
                lives += 1 # Ganha uma vida a cada letra correta
                break
            else:
                print("Errou! Tente novamente.")
                lives -= 1 # Perde uma vida a cada letra incorreta
                if lives == 0:
                    print("Você perdeu todas as vidas. Tente novamente.")
                    return False

