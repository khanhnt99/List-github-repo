import requests
username = input("Enter the github username:")
res = requests.get('https://api.github.com/users/'+username+'/repos')
json = res.json()
for i in range(0, len(json)):
    print("Project Number: ", i+1)
    print("Project Name: ", json[i]['name'])
