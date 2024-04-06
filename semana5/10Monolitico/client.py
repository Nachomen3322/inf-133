import requests
url = "http://localhost:8000"
# GET /posts
response = requests.get(f"{url}/posts")
print(response.text)

print("POST---")
# POST /post
data = {
    "title": "Mi experiencia como dev",
    "content": "[De 5 estrellas 4 estrellas, porque no puedo dormir]"
}
headers = {'Content-type': 'application/json'}
response = requests.post(f"{url}/posts", json=data, headers=headers)
print(response.json())

response = requests.get(f"{url}/posts")
print(response.text)

print("PUT---")
# PUT /post/3
edit = {
    "title": "Mi primera publicacion editada",
    "content": "En progreso"
}
headers = {'Content-type': 'application/json'}
response = requests.put(f"{url}/posts/1", json=edit, headers=headers)
print(response.text)

response = requests.get(f"{url}/posts")
print(response.text)

print("DELETE---")
# DELETE /post/1
response = requests.delete(f"{url}/posts/1")
print(response.text)

response = requests.get(f"{url}/posts")
print(response.text)


