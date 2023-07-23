import re

def valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"
    return re.match(pattern, password)

def main():
    passwords_input = input("Enter a sequence of comma-separated passwords: ")

    passwords = passwords_input.split(",")

    valid_passwords = [password for password in passwords if valid_password(password)]

    print(",".join(valid_passwords))

if __name__ == "__main__":
    main()
