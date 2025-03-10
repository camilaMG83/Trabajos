#Typewriter.py

def create_a_typewriter_file():
    try:
        name_of_file = input("Enter the name you want for your file (after you write your desired file name with no spaces, please write .txt after it): ")

        print(f"The file '{name_of_file}' will be created in a few moments..." )

        if not name_of_file.endswith(".txt"):
            print("This is an invalid file name, remember it needs to end with '.txt'")
            return 

        with open(name_of_file, "w", encoding="UTF-8") as file:
            print("Start writing your text. Type 'the end' on a new line when you are done, to save and then exit the program.")
            while True:
                line = input()  
                if line.lower() == "the end":
                    break  

                file.write(line + "\n") 

            print("Your file has been successfully saved!")

    except Exception as e:
        print(f"An error occurred: {e}")


def word_counting(name_of_file):
    try:
        with open(name_of_file, "r", encoding="UTF-8") as file: 
            content = file.read()  
            word_count = len(content.split())  
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print("This file was not found. You need to create a file first.")


def main():
    create_a_typewriter_file() 
    name_of_file = input("Enter the name of the file to count the words in: ")
    word_counting(name_of_file) 

main()
