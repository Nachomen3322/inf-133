import requests

url = "http://localhost:5000/"

response = requests.get(url=url)

print(response.text)


nombre = requests.get(url=url + "saludar?nombres=Messi")
print(nombre.text)

suma = requests.get(url=url + "suma?num1=5&num2=3")
print(suma.text)


palindromo = requests.get(url=url + "palindromo?cadena=reconocer")
print(palindromo.text)

contar = requests.get(url=url + "contar?cadena=exepciones&vocal=e")
print(contar.text)
