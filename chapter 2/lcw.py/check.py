# Palindrome Checker Program in Python

def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = "".join(s.split()).lower()
    return cleaned == cleaned[::-1]

# Main Program
print("===== Palindrome Checker =====")
choice = input("Do you want to check a (1) Word or (2) Number? Enter 1 or 2: ")

if choice == "1":
    word = input("Enter a word or sentence: ")
    if is_palindrome(word):
        print(f"✅ '{word}' is a Palindrome!")
    else:
        print(f"❌ '{word}' is NOT a Palindrome.")

elif choice == "2":
    num = input("Enter a number: ")
    if is_palindrome(num):
        print(f"✅ {num} is a Palindrome!")
    else:
        print(f"❌ {num} is NOT a Palindrome.")

else:
    print("⚠️ Invalid choice, please enter 1 or 2.")
