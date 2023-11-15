# Get user input
#user_input = input("Enter a string: ")

# Calculate the length of the string
#length_of_string = len(user_input)

# Display the result
#print(f"The length of the string is: {length_of_string}")

# Specify the path to your text file
file_path = 'G:/research27-09-2023/charactor length/charactors.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the content of the file
    file_content = file.read()

    # Calculate the length of the string
    length_of_string = len(file_content)

    # Display the result
    print(f"The length of the string in the file is: {length_of_string}")

