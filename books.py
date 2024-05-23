import yaml

# books.yaml faylını oxuyun
with open('books.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 1000-dən çox səhifəsi olan kitabları tapın və çap edin
for book in data['books']:
    if book['pages'] > 1000:
        print(f"{book['name']} {book['library']}")
