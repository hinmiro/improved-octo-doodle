import base64


def encrypt():
    string = input("Type raw string to encode base64: ")
    encoded_data = base64.b64encode(string.encode()).decode("utf-8")
    return encoded_data


def decrypter():
    string = input("Type base64 string to decode: ")
    decoded_byte = base64.b64decode(string)
    decoded_data = decoded_byte.decode()
    return decoded_data


def file_encoder(PATH):
    with open(PATH, "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            new_line = base64.b64encode(line.encode()).decode("utf-8")
            file.write(f"{new_line}\n")
        file.truncate()


def file_decoder(PATH):
    with open(PATH, "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            new_byte = base64.b64decode(line)
            new_line = new_byte.decode()
            file.write(f"{new_line}")
        file.truncate()


def processor(choice):
    if choice == 1:
        data = encrypt()
        print(data)
    elif choice == 2:
        data = decrypter()
        print(data)
    elif choice == 3:
        path = input("type complete path to text file you want encode to base64: ")
        file_encoder(path)
    elif choice == 4:
        path = input("type complete path to text file you want decode from base64: ")
        file_decoder(path)
    elif choice == 0:
        print("Shutting down, good bye")
        return 0


user_choice = 66
print(":::Encoder:::Decode:::\n")

while user_choice != 0:
    try:
        user_choice = int(input("Choose one of below by typing number:\n"
                                "1. Encode one string (raw password)\n"
                                "2. Decode one string (raw base64)\n"
                                "3. Encode file\n"
                                "4. Decode file\n"
                                "0. End program\n"))
    except ValueError:
        print("Faulty choice , use numbers")
    user_choice = processor(user_choice)
