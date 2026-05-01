def reverse_dictionary(en_ru_file, ru_en_file):
    ru_dict = {}
    with open(en_ru_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Убираем лишние тире/пробелы
            if ' - ' in line:
                eng, rus_part = line.split(' - ', 1)
            elif ' -- ' in line:
                eng, rus_part = line.split(' -- ', 1)
            else:
                continue

            # У каждого английского слова может быть несколько русских
            for rus in rus_part.split(', '):
                rus = rus.strip()
                if rus not in ru_dict:
                    ru_dict[rus] = []
                ru_dict[rus].append(eng)

    # Запись результата
    with open(ru_en_file, 'w', encoding='utf-8') as f:
        for rus in sorted(ru_dict.keys()):  # сортировка по алфавиту
            eng_variants = ', '.join(sorted(ru_dict[rus]))
            f.write(f"{rus} -- {eng_variants}\n")

    print(f"Готово! Словарь сохранён в {ru_en_file}")

reverse_dictionary("en-ru.txt", "ru-en.txt")