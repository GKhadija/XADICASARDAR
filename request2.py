import requests

count = 100
spanish_users = []

url = "https://www.youtube.com"  # Servis URL-ni buraya qoyun

for i in range(count):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP xətalarını yoxlamaq

        data = response.json()

        # İstifadəçinin ölkəsinin İspaniya olub olmadığını yoxlayın
        if data.get('country') == 'Spain':
            name = data.get('name', 'Unknown')
            spanish_users.append(name)

    except requests.RequestException as e:
        print(f"Request {i+1} failed: {e}")

# İspaniyalı istifadəçiləri və onların sayını çap edin
print(f"Number of Spanish users: {len(spanish_users)}")
print("Names of Spanish users:")
for name in spanish_users:
    print(name)
