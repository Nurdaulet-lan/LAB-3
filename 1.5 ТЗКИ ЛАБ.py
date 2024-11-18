import random

def generate_magic_square():
    """Генерирует случайный квадрат 4x4, заполненный числами от 1 до 16."""
    numbers = list(range(1, 17))
    random.shuffle(numbers)
    return [numbers[i:i + 4] for i in range(0, 16, 4)]

def create_encrypted_table(magic_square, text):
    """Создает таблицу шифрования на основе магического квадрата и текста."""
    text = text.upper().replace(" ", "")  # Убираем пробелы и приводим к верхнему регистру
    encrypted_table = [["" for _ in range(4)] for _ in range(4)]
    pos_map = {}
    
    # Определяем позиции цифр в магическом квадрате
    for i in range(4):
        for j in range(4):
            pos_map[magic_square[i][j]] = (i, j)
    
    # Распределяем буквы текста по позициям
    for idx, char in enumerate(text):
        if idx >= 16:
            break  # Если текста больше 16 символов, обрезаем
        x, y = pos_map[idx + 1]
        encrypted_table[x][y] = char
    
    return encrypted_table

def extract_encrypted_text(encrypted_table):
    """Извлекает зашифрованный текст из таблицы."""
    encrypted_text = []
    for row in encrypted_table:
        for char in row:
            if char:
                encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt_text(magic_square, encrypted_table):
    """Расшифровывает текст, используя магический квадрат и шифровальную таблицу."""
    decrypted_text = [""] * 16
    pos_map = {}
    
    # Определяем позиции цифр в магическом квадрате
    for i in range(4):
        for j in range(4):
            pos_map[magic_square[i][j]] = (i, j)
    
    # Восстанавливаем исходный текст
    for num in range(1, 17):
        x, y = pos_map[num]
        char = encrypted_table[x][y]
        if char:
            decrypted_text[num - 1] = char
    
    return ''.join(decrypted_text).strip()

# Основной код
original_text = "НУРДАУЛЕТ РЕЕСТР"

# Шаг 1: Генерация магического квадрата
magic_square = generate_magic_square()

# Шаг 2: Создание таблицы шифрования
encrypted_table = create_encrypted_table(magic_square, original_text)

# Шаг 3: Извлечение зашифрованного текста
encrypted_text = extract_encrypted_text(encrypted_table)

# Шаг 4: Дешифровка
decrypted_text = decrypt_text(magic_square, encrypted_table)

# Вывод результата
print("Магический квадрат:")
for row in magic_square:
    print(row)

print("\nТаблица с шифрованием:")
for row in encrypted_table:
    print(row)

print("\nЗашифрованное сообщение:")
print(encrypted_text)

print("\nРасшифрованное сообщение:")
print(decrypted_text)
