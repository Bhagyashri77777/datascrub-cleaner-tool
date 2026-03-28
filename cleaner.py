# A simple Data Science utility to clean messy text data
print("--- 🧹 Welcome to Neural Knights DataScrub 🧹 ---")

while True:
    print("\n--- Main Menu ---")
    print("1. Clean messy text (Remove symbols & extra spaces)")
    print("2. Exit the tool")
    
    choice = input("What do you want to do? (Enter 1 or 2): ")
    
    if choice == '1':
        messy_text = input("Enter your messy data here: ")
        clean_text = ""
        
        # Loop through and only keep letters, numbers, and spaces
        for char in messy_text:
            if char.isalnum() or char.isspace():
                clean_text = clean_text + char
                
        # Remove extra spaces to make it neat
        final_text = " ".join(clean_text.split())
        
        print("\n--- ✨ Cleaning Complete ✨ ---")
        print("Original Data:", messy_text)
        print("Cleaned Data :", final_text)
        print("Status: Data is ready for AI models! ✅")
        
    elif choice == '2':
        print("Bye! Exiting DataScrub...")
        print("Keep coding! ✨ - Built by Bhagyashri Gawali")
        break
        
    else:
        print("Wrong choice! Please enter 1 or 2.")
