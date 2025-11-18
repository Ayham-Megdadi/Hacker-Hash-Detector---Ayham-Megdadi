import sys
import binascii
import hashlib

def detect_hash_type(hash_str):
    length = len(hash_str)
    hash_types = {
        32: "MD5",
        40: "SHA1",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }
    return hash_types.get(length, None)
    
def is_valid_hex(s):
    try:
        binascii.unhexlify(s)
        return True
    except Exception:
        return False

def generate_md5(plaintext):
    return hashlib.md5(plaintext.encode()).hexdigest()

def interactive_mode():
    while True:
        print("""
        
 $$$$$$\            
$$  __$$\           
$$ /  $$ |$$\   $$\ 
$$$$$$$$ |$$ |  $$ |
$$  __$$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |
\__|  \__| \____$$ |
          $$\   $$ |
          \$$$$$$  |
           \______/ 
        """)
        print("""==============================================
     ETHICAL HASH DETECTOR TOOL - v1.0
        Developed by: Ayham Belal Megdadi
        For Educational & Ethical Use Only
==============================================""")
        print("\n========== Select the Desired Option ==========")
        print("1) Detect hash type")
        print("2) Generate 'MD5' from plaintext")
        print("3) Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            h = input("Enter hash strin: ").strip().lower()

            if not is_valid_hex(h):
                print("\n[!] Invalid hex string. Only characters 0-9 and a-f are allowed.")
                continue
            hash_type = detect_hash_type(h)
            if hash_type:
                print(f"\nDetected hash type: {hash_type}")
            else:
                print("\nUnknown hash type - unfortunately")
        elif choice == "2":
            plaintext = input("Enter plaintext: ").strip()
            md5_value = generate_md5(plaintext)
            print(f"\nMD5: {md5_value}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("\n [!] Invalid option, try again")

def cli_mode(hash_str):
    hash_str = hash_str.lower()
    if not is_valid_hex(hash_str):
        print("Invalid hex string.")
        return
    hash_type = detect_hash_type(hash_str)
    if hash_type:
        print(f"Detected hash type: {hash_type}")
    else:
        print("Unknown hash type - unfortunately")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 Ayham.py <hash>")
        sys.exit()
    if len(sys.argv) == 2:
        # CLI mode
        cli_mode(sys.argv[1])
    else:
        # Interactive mode
        interactive_mode()
