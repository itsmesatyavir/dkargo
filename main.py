import requests
import json
import time
from colorama import Fore, Style

def display_banner():
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "Forest Army - DKA Faucet Claimer")
    print(Fore.CYAN + "Join us: " + Fore.YELLOW + "http://t.me/forestarmy")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

def get_wallet_addresses():
    try:
        with open("wallet.forest", "r") as file:
            wallets = [line.strip() for line in file if line.strip()]
            return wallets if wallets else None
    except FileNotFoundError:
        print(Fore.RED + "Error: wallet.forest file not found." + Style.RESET_ALL)
        return None

def request_faucet(wallet_address):
    url = "https://dkargo.io/en/developers/faucet"
    headers = {
        "authority": "dkargo.io",
        "method": "POST",
        "path": "/en/developers/faucet",
        "scheme": "https",
        "Accept": "text/x-component",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-IN",
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://dkargo.io",
        "Referer": "https://dkargo.io/en/developers/faucet",
        "Sec-Ch-Ua": '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge";v="127"',
        "Sec-Ch-Ua-Mobile": "?1"
    }
    
    payload = [wallet_address]
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(Fore.GREEN + f"[SUCCESS] DKA Claimed for {wallet_address}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"[ERROR] Failed for {wallet_address}: {response.text}" + Style.RESET_ALL)

def main():
    display_banner()
    wallets = get_wallet_addresses()
    if not wallets:
        print(Fore.RED + "No wallet addresses found. Exiting..." + Style.RESET_ALL)
        return
    
    for wallet in wallets:
        request_faucet(wallet)
        time.sleep(5)  # Prevent spam, adjust if needed

if __name__ == "__main__":
    main()
