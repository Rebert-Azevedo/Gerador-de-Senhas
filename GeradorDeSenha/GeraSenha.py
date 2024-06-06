import random
import string

def gerar_senha(tamanho_senha, usar_minusculas=True, usar_maiusculas=True, usar_numeros=True, usar_simbolos=True):
 
  """
  Gera uma senha aleatória com base nos parâmetros especificados.

  Args:
    tamanho_senha: Tamanho da senha a ser gerada.
    usar_minusculas: Se True, inclui letras minúsculas na senha.
    usar_maiusculas: Se True, inclui letras maiúsculas na senha.
    usar_numeros: Se True, inclui números na senha.
    usar_simbolos: Se True, inclui símbolos na senha.

  Returns:
    Uma string contendo a senha gerada.
  """

  caracteres = ""

  if usar_minusculas:
    caracteres += string.ascii_lowercase
  if usar_maiusculas:
    caracteres += string.ascii_uppercase
  if usar_numeros:
    caracteres += string.digits
  if usar_simbolos:
    caracteres += string.punctuation

  senha = "".join(random.choice(caracteres) for _ in range(tamanho_senha))
  return senha

def main():
  """
  Função principal do script.
  """

  numero_senhas = int(input("Digite o número de senhas que deseja gerar: "))
  tamanho_senha = int(input("Digite o tamanho das senhas: "))

  print("\nSenhas geradas:")
  for _ in range(numero_senhas):
    senha = gerar_senha(tamanho_senha)
    f = open('passwords.txt', "a")
    f.write(senha + "\n")
    f.close()

if __name__ == "__main__":
  main()
