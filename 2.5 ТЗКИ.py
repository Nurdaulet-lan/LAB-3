def encrypt(text, key):
    n = len(key)
    # Разбиваем текст на группы по n символов
    groups = [text[i:i + n] for i in range(0, len(text), n)]
    encrypted_groups = []

    for group in groups:
        # Дополняем пробелами, если группа меньше n
        group = group.ljust(n)
        encrypted_group = [''] * n
        for i in range(n):
            encrypted_group[key[i] - 1] = group[i]  # Перестановка
        encrypted_groups.append(''.join(encrypted_group))

    return ''.join(encrypted_groups)

def decrypt(encrypted_text, key):
    n = len(key)
    groups = [encrypted_text[i:i + n] for i in range(0, len(encrypted_text), n)]
    decrypted_groups = []

    # Обратная перестановка
    reverse_key = sorted(range(len(key)), key=lambda k: key[k])

    for group in groups:
        group = group.ljust(n)  # Дополняем пробелами
        decrypted_group = [''] * n
        for i in range(n):
            decrypted_group[reverse_key[i]] = group[i]  # Восстанавливаем порядок
        decrypted_groups.append(''.join(decrypted_group))

    return ''.join(decrypted_groups).strip()  # Убираем пробелы в конце

def main():
    # Запрос ключа у пользователя
    key = list(map(int, input("Введите порядок перестановки (например, 2 1 3 4): ").split()))
    
    while True:
        choice = input("Введите 'ш' для шифрования, 'д' для дешифрования или 'в' для выхода: ").strip().lower()

        if choice == 'ш':
            text = input("Введите текст для шифрования: ").replace(" ", "")
            encrypted_text = encrypt(text, key)
            print("Зашифрованный текст:", encrypted_text)

        elif choice == 'д':
            encrypted_text = input("Введите текст для дешифрования: ")
            decrypted_text = decrypt(encrypted_text, key)
            print("Расшифрованный текст:", decrypted_text)

        elif choice == 'в':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()
