# validação de senha: Escreva uma função que verifique se uma senha atende a critérios mínimos de segurança,
# como ter um comprimento mínimo, conter letras maiúsculas, minúsculas e números.

import re

print("Cadastre aqui sua senha com os seguintes critérios:")
print("  * Pelo menos 8 dígitos")
print("  * Pelo menos uma letra maiúscula")
print("  * Pelo menos um número")
print("  * Pelo menos um caractere especial (!@#$%¨&*)")

while True:
    senha = input("Digite sua senha")
    # O comando re.search() é uma função da biblioteca re (expressões regulares) em Python que é usada para pesquisar
    # uma string em busca de uma correspondência com um padrão específico.

    if len(senha) < 8:
        print("A senha deve conter no minimo 8 caracteres.")
    elif re.search(r"[A-Z]", senha):
        print("A senha deve ter pelo menos uma letra maiúscula.")
    elif re.search(r"\d", senha):
        print("A senha deve ter pelo menos um número.")
    elif re.search(r"[!@#$%¨&*]", senha):
        print("A senha deve ter pelo menos um caractere especial.")
    else:
        print("Senha valida")
        break
