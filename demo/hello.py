def main():
    name = input("Enter your name: ")
    if name.strip() == "":
        print("You didn't enter a name! Please try again next time.")
    else:
        print(f"Hello, {name}! Welcome to my GitHub demo.")

if __name__ == "__main__":
    main()