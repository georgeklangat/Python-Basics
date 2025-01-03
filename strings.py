text = "I love poetry and coding"
course = "WEB DEVELOPMENT"
print(text)

# Accessing an element in a string
print(text[0])

# Size/length of the string
print(len(text))

# Modifying a string
print(course.lower())

# string concatenation
greeting = "Hello"
first_name = "Georges"

print(greeting +' '+ first_name)

# Slicing the string

b = "  Hello, world"
print(b[2:])
print(b[-5:-2])
print(b.strip())
print(b.replace("H","J"))
print(b.split(",")) # returns a list where the text between the specified separator

# escape characters
text = "I love poetry \"life\" and coding"

# Demonstration of various string methods
def string_methods_demo():
    sample_text = "Hello, World!"

    # Convert to uppercase
    print("Uppercase:", sample_text.upper())

    # Convert to lowercase
    print("Lowercase:", sample_text.lower())

    # Check if string starts with "Hello"
    print("Starts with 'Hello':", sample_text.startswith("Hello"))

    # Check if string ends with "World!"
    print("Ends with 'World!':", sample_text.endswith("World!"))

    # Find the position of a substring
    print("Position of 'World':", sample_text.find("World"))

    # Replace a substring
    print("Replace 'World' with 'Python':", sample_text.replace("World", "Python"))

    # Split string into a list
    print("Split string by comma:", sample_text.split(","))

    # Join a list of strings
    words = ["Python", "is", "awesome"]
    print("Join words with spaces:", " ".join(words))

    # Check if string is alphanumeric
    alphanumeric_text = "Python3"
    print("Is 'Python3' alphanumeric?:", alphanumeric_text.isalnum())

    # Strip whitespace
    text_with_spaces = "   padded text   "
    print("Strip spaces:", text_with_spaces.strip())

    # Count occurrences of a character
    print("Count of 'l':", sample_text.count('l'))

    # Reverse a string (using slicing)
    print("Reversed string:", sample_text[::-1])

# Call the function
string_methods_demo()
