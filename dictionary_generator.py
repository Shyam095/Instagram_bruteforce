import itertools

def generate_passwords(length=6):
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:,.<>?'
    for password_length in range(length, length + 1):
        for password in itertools.product(characters, repeat=password_length):
            yield ''.join(password)

def save_to_file(passwords, filename='passwords.txt'):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

if __name__ == '__main__':
    length = int(input('Enter the maximum password length (default is 6): '))
    passwords = generate_passwords(length)
    save_to_file(passwords)
    print(f'{length} character passwords have been generated and saved to "passwords.txt".')
