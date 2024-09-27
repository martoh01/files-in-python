# file_handling_assignment.py
# Author: Martoh, PLP 2024 CLASS, Kenya

# File Creation: Creating and writing to 'my_file.txt'
try:
    # Open the file in write mode ('w'), this will create the file if it doesn't exist
    with open('my_file.txt', 'w') as file:
        # Writing three lines of text, including strings and numbers
        file.write("Hello, this is the first line.\n")
        file.write("Here is a number: 12345.\n")
        file.write("The last line of this section.\n")
    print("File created and initial content written successfully.")

except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display: Reading the file content
try:
    # Open the file in read mode ('r')
    with open('my_file.txt', 'r') as file:
        content = file.read()  # Reading the content of the file
        print("\n--- File Content After Initial Write ---")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An error occurred during file reading: {e}")

# File Appending: Appending additional lines to 'my_file.txt'
try:
    # Open the file in append mode ('a')
    with open('my_file.txt', 'a') as file:
        # Appending three more lines of text
        file.write("This is an appended line 1.\n")
        file.write("Adding another number: 67890.\n")
        file.write("This is the final appended line.\n")
    print("\nAdditional lines appended successfully.")

except Exception as e:
    print(f"An error occurred during file appending: {e}")

# Reading and displaying the updated file content
try:
    # Open the file in read mode again to show the final content
    with open('my_file.txt', 'r') as file:
        content = file.read()  # Reading the updated content of the file
        print("\n--- Final File Content After Appending ---")
        print(content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("\nFile handling script execution completed by Martoh, PLP 2024 CLASS.")
