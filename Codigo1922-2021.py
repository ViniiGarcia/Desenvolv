print ("Digite seu nome:")
nome = input()

executar = True

while(executar == True):
    print("Digite o ano de Nascimento:")
    try:
        ano = int(input())
        if(ano < 1922) or (ano > 2021):
            print("O ano precisa estar entre 1922 e 2021")
        else:
            idade = 2022 - ano
            print("O Usuario" , nome , "Completou ou Completará" , idade ,
                  "Anos de idade em 2023")
        executar = False
    except:
        print("Digite o ano somente com numeros")