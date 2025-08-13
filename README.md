# brutehash256.py
A Python SHA-256 hash brute-forcer using the rockyou.txt wordlist. Reads each password, hashes it with Pwntools’ sha256sumhex(), and compares against a target hash. Displays progress in real time and stops when the matching password is found.
