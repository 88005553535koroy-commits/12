import json
def add_product(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Добавление нового продукта:")
    name = input("Название: ")
    price = int(input("Цена: "))
    weight = int(input("Вес: "))
    available = input("В наличии? (да/нет): ").lower() == 'да'

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }

    data['products'].append(new_product)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Готово! Обновлённый список:")
    for p in data['products']:
        print(f"{p['name']} — {p['price']} руб. ({'есть' if p['available'] else 'нет'})")