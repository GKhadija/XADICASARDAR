import requests
import time

count = 100
success_request = 0
fail_request = 0
slow_request = 0

url = "https://www.youtube.com"  # Servis URL-ni buraya qoyun

for i in range(count):
    start_time = time.time()  # Sorğunun başlama vaxtı
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP xətalarını yoxlamaq

        elapsed_time = time.time() - start_time  # Sorğunun icra müddəti
        if response.status_code == 200 and elapsed_time < 1:
            success_request += 1
        elif response.status_code == 200:
            slow_request += 1
        else:
            fail_request += 1

        # Hər sorğunun nəticəsini çap edin (əlavə olaraq)
        print(f"Request {i+1}: Status Code: {response.status_code}, Time: {elapsed_time:.4f} seconds")

    except requests.RequestException as e:
        fail_request += 1
        elapsed_time = time.time() - start_time
        print(f"Request {i+1}: Failed, Time: {elapsed_time:.4f} seconds")

print(f"Success: {success_request}")
print(f"Failed: {fail_request}")
print(f"Slow Requests (>1s): {slow_request}")