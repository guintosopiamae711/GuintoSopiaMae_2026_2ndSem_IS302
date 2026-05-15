try:
    with open("data.txt", "r") as file_smg:
        content_smg = file_smg.read()
    print(content_smg)
except FileNotFoundError:
    print("File does not exist")
