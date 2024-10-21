def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsiusToKelvin(celsius):
    return celsius + 273.15

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheitToKelvin(fahrenheit):
    celsius = fahrenheitToCelsius(fahrenheit)
    return celsiusToKelvin(celsius)

def kelvinToCelsius(kelvin):
    return kelvin - 273.15

def kelvinToFahrenheit(kelvin):
    celsius = kelvinToCelsius(kelvin)
    return celsiusToFahrenheit(celsius)

def converter():
    while True:
        print("\nO que quer converter?:")
        print("1. Celsius para Fahrenheit")
        print("2. Celsius para Kelvin")
        print("3. Fahrenheit para Celsius")
        print("4. Fahrenheit para Kelvin")
        print("5. Kelvin para Celsius")
        print("6. Kelvin para Fahrenheit")
        print("7. Sair do programa")
        
        escolha = input("Digite o número da sua escolha: ")
        
        if escolha == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C é igual a {celsiusToFahrenheit(celsius)}°F")
        
        elif escolha == '2':
            celsius = float(input("Digite a temperatura em Celsius: "))
            print(f"{celsius}°C é igual a {celsiusToKelvin(celsius)}K")
        
        elif escolha == '3':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{fahrenheit}°F é igual a {fahrenheitToCelsius(fahrenheit)}°C")
        
        elif escolha == '4':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{fahrenheit}°F é igual a {fahrenheitToKelvin(fahrenheit)}K")
        
        elif escolha == '5':
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin}K é igual a {kelvinToCelsius(kelvin)}°C")
        
        elif escolha == '6':
            kelvin = float(input("Digite a temperatura em Kelvin: "))
            print(f"{kelvin}K é igual a {kelvinToFahrenheit(kelvin)}°F")
        
        elif escolha == '7':
            print("Saindo do programa...")
            break
        
        else:
            print("Escolha inválida. Por favor, selecione um número de 1 a 7.")

# Chama a função do conversor
if __name__ == "__main__":
    converter()