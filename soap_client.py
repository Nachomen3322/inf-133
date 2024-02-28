from zeep import Client

client = Client("http://localhost:8000")
result = client.service.Saludar(nombre="Ignacio")
a, b = map(int, input("Ingrese 2 datos de la siguiente manera, ejemplo: 1, 2: ").split(","))
resultSuma = client.service.SumaDosNumeros(a, b)
resultPalindromo = client.service.CadenaPalindromo(input("Ingrese una cadena: "));
print(result)
print(resultSuma)
print(resultPalindromo)