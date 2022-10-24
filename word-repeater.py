def main():
    word = input("Enter word to repeat: ")
    n = int(input("Enter number of times to repeat: "))

    for i in range(1, n):
        print(word)


if __name__ == "__main__":
    main()
