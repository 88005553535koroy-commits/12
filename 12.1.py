import json
def show_products(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()
show_products("products.json")