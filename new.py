import time

def create_key_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = prepare_input(key)
    key_matrix = []

    for char in key:
        if char not in key_matrix:
            key_matrix.append(char)

    for char in alphabet:
        if char not in key_matrix:
            key_matrix.append(char)

    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def prepare_input(text):
    cleaned_text = ''.join(char.upper() for char in text if char.isalpha())
    cleaned_text = cleaned_text.replace("J", "I")
    return cleaned_text

def get_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt():
    plaintext = input("Masukkan plain text: ")
    key = input("Masukkan kunci Playfair: ")

    key_matrix = create_key_matrix(key)

    plaintext = prepare_input(plaintext)
    ciphertext = ""

    start_time_playfair = time.time()

    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        row1, col1 = get_position(key_matrix, char1)
        row2, col2 = get_position(key_matrix, char2)

        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5]
            ciphertext += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1]
            ciphertext += key_matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_matrix[row1][col2]
            ciphertext += key_matrix[row2][col1]

    end_time_playfair = time.time()
    execution_time_playfair = end_time_playfair - start_time_playfair
    print("Hasil Enkripsi Playfair:", ciphertext)
    print("Waktu eksekusi Playfair Encrypt: {:.6f} detik".format(execution_time_playfair))

    return ciphertext

def playfair_decrypt(ciphertext, key_matrix):
    plaintext = ""
    ciphertext = prepare_input(ciphertext)

    start_time_playfair = time.time()

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1] if i + 1 < len(ciphertext) else 'X'
        row1, col1 = get_position(key_matrix, char1)
        row2, col2 = get_position(key_matrix, char2)

        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5]
            plaintext += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1]
            plaintext += key_matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += key_matrix[row1][col2]
            plaintext += key_matrix[row2][col1]

    end_time_playfair = time.time()
    execution_time_playfair = end_time_playfair - start_time_playfair
    print("Hasil Dekripsi Playfair:", plaintext)
    print("Waktu eksekusi Playfair Decrypt: {:.6f} detik".format(execution_time_playfair))

    return plaintext

def zigzag_encrypt(plaintext, key):
    if key <= 1:
        return plaintext

    result = [''] * key
    index = 0
    direction = 1

    for char in plaintext:
        result[index] += char
        index += direction

        if index == key - 1 or index == 0:
            direction *= -1

    ciphertext_zigzag = ''.join(result)

    start_time_zigzag = time.time()
    print("Hasil Enkripsi Zigzag:", ciphertext_zigzag)
    end_time_zigzag = time.time()
    execution_time_zigzag = end_time_zigzag - start_time_zigzag
    print("Waktu eksekusi Zigzag Encrypt: {:.6f} detik".format(execution_time_zigzag))

    return ciphertext_zigzag

def zigzag_decrypt(ciphertext, key):
    if key <= 1:
        return ciphertext

    result = [''] * key
    index = 0
    direction = 1

    for char in ciphertext:
        result[index] += '*'
        index += direction

        if index == key - 1 or index == 0:
            direction *= -1

    decrypted_text = [''] * key
    char_index = 0

    for i in range(key):
        for j in range(len(result[i])):
            decrypted_text[i] = decrypted_text[i][:j] + ciphertext[char_index] + decrypted_text[i][j + 1:]
            char_index += 1

    final_result = ''
    index = 0
    direction = 1

    for i in range(len(ciphertext)):
        final_result += decrypted_text[index][0]
        decrypted_text[index] = decrypted_text[index][1:]
        index += direction

        if index == key - 1 or index == 0:
            direction *= -1

    start_time_zigzag = time.time()
    print("Hasil Dekripsi Zigzag:", final_result)
    end_time_zigzag = time.time()
    execution_time_zigzag = end_time_zigzag - start_time_zigzag
    print("Waktu eksekusi Zigzag Decrypt: {:.6f} detik".format(execution_time_zigzag))

    return final_result

def main():
    start_time_main = time.time()

    choice = input("Pilih 'E' untuk enkripsi atau 'D' untuk dekripsi: ").upper()

    if choice == 'E':
        ciphertext_playfair = playfair_encrypt()
        key_zigzag = 3
        zigzag_encrypt(ciphertext_playfair, key_zigzag)
    elif choice == 'D':
        ciphertext_zigzag = input("Masukkan cipher text Zigzag: ")
        key_zigzag = 3
        decrypted_zigzag = zigzag_decrypt(ciphertext_zigzag, key_zigzag)
        print("Hasil Dekripsi Zigzag:", decrypted_zigzag)

        key_playfair = input("Masukkan kunci Playfair untuk dekripsi: ")
        key_matrix_playfair = create_key_matrix(key_playfair)
        playfair_decrypt(decrypted_zigzag, key_matrix_playfair)
    else:
        print("Pilihan tidak valid. Pilih 'E' atau 'D.'")

    end_time_main = time.time()
    execution_time_main = end_time_main - start_time_main
    print("Total waktu eksekusi program: {:.6f} detik".format(execution_time_main))

if __name__ == "__main__":
    main()
