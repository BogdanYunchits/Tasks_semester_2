def write_text_to_file():
    with open("example.txt", "w", encoding="utf-8") as file:
        file.write("This is the first line.\n")
        file.write("This is the second line.\n")
        file.write("This is the third line.\n")

write_text_to_file()

def read_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

read_text_from_file("example.txt")
