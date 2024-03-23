print("########## Par ou Impar ##########")
#Função para poder chamar em outros momentos:
def par_impar():
    numero=int(input("Digite um número inteiro>> "))
    return numero
#loop por causa da 3º parte:
while True:
    #Chamando a função para dentro do loop:
    numero_usuario = par_impar()
    #Conta para descobrir se o número é par ou impar
    if numero_usuario % 2 == 0:
        print(f"O número {numero_usuario} é: \nPar")
    else:
        print(f"O número {numero_usuario} é: \nÍmpar")
    #3º parte: Descobrir se a pessoa quer sair do loop:
    retornar_inicio=input("Deseja testar outro número?(s/n) ")
    if retornar_inicio.lower() != "s" and retornar_inicio.lower() != "n":
        print("Digite apenas 's' ou 'n'")
    if retornar_inicio.lower()=="n":
        print("Espero que tenha gostado!")
        break 
