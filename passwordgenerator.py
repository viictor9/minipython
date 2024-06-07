

SECURE = (('s', '5'), ('a', '@'), ('o', '0'), ('i', '1'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password


if __name__ == "__main__":
    Enter = input("Enter your password: ")
    password = securePassword(Enter)
    print(f"your secure password is {password}")