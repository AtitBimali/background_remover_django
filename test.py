import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('atit.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'nMwNpgr7xLeEtQMqb8cLd3at'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)


import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    data={
        'image_url': 'https://www.remove.bg/example.jpg',
        'size': 'auto'
    },
    headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)