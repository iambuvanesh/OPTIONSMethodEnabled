import requests
import argparse

# ANSI color codes
GREEN = "\033[92m"
RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"

def check_options(domain):
    url = f"https://{domain}"
    try:
        response = requests.options(url, timeout=5)
        if response.status_code == 200:
            allowed_methods = response.headers.get('Allow', 'Not specified')
            print(f"{GREEN}[+] {domain} supports OPTIONS. Allowed methods: {allowed_methods}{RESET}")
        else:
            print(f"{YELLOW}[-] {domain} responded with status code {response.status_code}{RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[!] Error checking {domain}: {e}{RESET}")

def main():
    parser = argparse.ArgumentParser(description="Check if domains support the OPTIONS method")
    parser.add_argument('-u', '--url', help="Single domain to check (e.g. example.com)")
    parser.add_argument('-f', '--file', help="File containing a list of domains")

    args = parser.parse_args()

    if args.url:
        check_options(args.url)
    elif args.file:
        try:
            with open(args.file, "r") as file:
                domains = file.read().splitlines()
                for domain in domains:
                    check_options(domain)
        except FileNotFoundError:
            print(f"{RED}[!] File not found: {args.file}{RESET}")
    else:
        print(f"{YELLOW}[!] Please provide either a single URL with -u or a file with -f{RESET}")

if __name__ == "__main__":
    main()
  
