# Matriz A
A = [[4, 1], [3, 1]]

# Matriz B
B = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
     [18, 19, 20, 21, 22, 23, 24, 25, 26, 1, 2, 3, 4, 5, 6, 7, 8]]

# Frase a ser criptografada
frase = "ESTUDAR PARA TRANSFORMAR O MUNDO"

# Remove espaços em branco e converte a frase para letras maiúsculas
frase = frase.replace(" ", "").upper()

# Verifica se a frase tem o tamanho adequado para a multiplicação
if len(frase) != 2:
    print("A frase deve conter exatamente 2 caracteres.")
    exit()

# Converte a frase em um vetor coluna
frase_vetor = [[ord(frase[0]) - ord('A') + 1], [ord(frase[1]) - ord('A') + 1]]

# Realiza a multiplicação de matriz A com matriz B
resultado = [[0] * len(B[0]) for _ in range(len(A))]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]

# Criptografa a frase multiplicando a matriz resultado pelo vetor coluna da frase
frase_criptografada = [[0] * len(frase_vetor[0]) for _ in range(len(resultado))]
for i in range(len(resultado)):
    for j in range(len(frase_vetor[0])):
        for k in range(len(frase_vetor)):
            frase_criptografada[i][j] += resultado[i][k] * frase_vetor[k][j]

# Imprime a frase criptografada
print("Frase criptografada:")
for i in range(len(frase_criptografada)):
    for j in range(len(frase_criptografada[0])):
        print(chr(frase_criptografada[i][j] - 1 + ord('A')), end="")
print()
