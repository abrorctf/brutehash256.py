# brutehash256.py
A Python SHA-256 hash brute-forcer using the rockyou.txt wordlist. Reads each password, hashes it with Pwntools’ sha256sumhex(), and compares against a target hash. Displays progress in real time and stops when the matching password is found.


# 🔐 SHA-256 Hash Brute Forcer

A fast and simple Python tool for brute-forcing SHA-256 hashes using a wordlist.  
Built with [Pwntools](https://docs.pwntools.com/en/stable/) for efficient hashing and real-time progress display.

---

## 📜 Description
This script attempts to find the plaintext password for a given SHA-256 hash by checking each entry in a wordlist file (default: `rockyou.txt`).  
It encodes each word in `latin-1`, hashes it with `sha256sumhex()`, and compares it to the target.  
Progress is shown in the terminal, and the script stops once a match is found or the list ends.

---

## 🚀 Features
- ✅ Brute-force attack using SHA-256
- ✅ Reads from large wordlists
- ✅ Real-time progress updates
- ✅ Stops immediately when a match is found

---

## 🛠 Requirements
- Python 3.x
- [Pwntools](https://docs.pwntools.com/en/stable/)

Install dependencies:
```bash
pip install pwntools

📂 Wordlist

The script uses the popular rockyou.txt wordlist by default:

/usr/share/wordlists/rockyou.txt

Make sure it’s installed:

sudo apt install wordlists

💻 Usage

python3 brutehash256.py <sha256_hash>

Example:

python3 brutehash256.py e3afed0047b08059d0fada10f400c1e5b5c0e1e3c2f6e6dcf4e6a1f7b5f5a5a7

📌 Example Output

[1523] Trying: b'password123' == 482c811da5d5b4bc6d497ffa98491e38
[+] Match found! e3afed0047b08059d0fada10f400c1e5 == b'password123'

⚠ Disclaimer

This tool is intended for educational purposes only.
Do not use it for unauthorized access or illegal activities.
