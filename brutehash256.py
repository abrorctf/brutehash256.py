from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid Input")
    print("Syntax: python3 brutehash256.py <wanted_hash>")
    exit()

wanted_hash = sys.argv[1]
password_file = "../../../../../usr/share/wordlists/rockyou.txt"
attempts = 0

with open(password_file, 'r', encoding='latin-1') as password_list:
    for password in password_list:
        password = password.strip().encode('latin-1')
        password_hash = sha256sumhex(password) # type: ignore

        sys.stdout.write(f"\r[{attempts}] Trying: {repr(password)} == {password_hash}")
        sys.stdout.flush()

        if password_hash == wanted_hash:
            print(f"\n[+] Match found! {wanted_hash} == {repr(password)}")
            exit()

        attempts += 1

print("\n[-] Password not found!")
