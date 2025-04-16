import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def login(email, password_to_check, stored_logins):
    hashed_password = hash_password(password_to_check)
    if email in stored_logins and stored_logins[email] == hashed_password:
        return True
    else:
        return False
def main():
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "alice@wonderland.com": hash_password("rabbitHole42"),
        "bob@builder.com": hash_password("canWeFixIt")
    }
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Login failed. Check your email or password.")
if __name__ == '__main__':
    main()
