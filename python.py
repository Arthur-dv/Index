def calcular_imc(peso, altura):
    """
    Calcula o IMC (Índice de Massa Corpórea) com base no peso e altura fornecidos.
    Fórmula: IMC = peso / altura^2
    """
    imc = peso / (altura ** 2)
    return imc

def main():
    print("Bem-vindo ao calculador de IMC!")
    peso = float(input("Por favor, digite seu peso em quilogramas (kg): "))
    altura = float(input("Agora, digite sua altura em metros (m): "))
    
    imc = calcular_imc(peso, altura)
    
    print("Seu IMC é: {:.2f}".format(imc))
    if imc < 18.5:
        print("Você está abaixo do peso normal.")
    elif imc < 25:
        print("Seu peso está dentro da faixa considerada saudável.")
    elif imc < 30:
        print("Você está com sobrepeso.")
    else:
        print("Você está obeso.")

if __name__ == "__main__":
    main()
