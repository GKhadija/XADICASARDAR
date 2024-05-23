import requests

# Servisin URL-sini buraya əlavə edin
BASE_URL = "https://petstore.swagger.io/#/user/getUserByName"

# Nəticələrin saxlanması üçün dəyişənlər
successful_responses = 0
not_found_responses = 0

# 0-dan 99-a qədər olan ID-lərlə sorğular göndərmək
for user_id in range(100):
    response = requests.get(f"{BASE_URL}/{user_id}")
    
    if response.status_code == 200:
        print(f"User ID {user_id}: Məlumat tapıldı (200)")
        successful_responses += 1
    elif response.status_code == 404:
        print(f"User ID {user_id}: Məlumat tapılmadı (404)")
        not_found_responses += 1
    else:
        print(f"User ID {user_id}: Gözlənilməz cavab kodu {response.status_code}")

# Yekun nəticələr
print(f"Successful responses (200): {successful_responses}")
print(f"Not found responses (404): {not_found_responses}")
