# Palindrome Checker

def is_palindrome(text):
    # Convert to lowercase and remove spaces
    cleaned = text.lower().replace(" ", "")
    
    # Check if the text is the same forwards and backwards
    return cleaned == cleaned[::-1]

# Main program
def main():
    user_input = input("Enter a word or number: ")

    if is_palindrome(user_input):
        print("✅ It's a palindrome!")
    else:
        print("❌ It's not a palindrome.")

# Run the program
if __name__ == "__main__":
    main()
