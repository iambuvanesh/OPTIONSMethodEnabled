# OPTIONSMethodEnabled

A simple Python tool to check if a domain or list of domains support the HTTP `OPTIONS` method, and retrieve the allowed HTTP methods via the `Allow` header.

## 💡 Features

- Check a **single domain** or **multiple domains** from a file.
- Uses **HTTPS** by default.
- Color-coded output:
  - ✅ Green: OPTIONS method is supported
  - ⚠️ Yellow: Non-200 response
  - ❌ Red: Error connecting to domain

## 🛠️ Installation

```bash
git clone https://github.com/iambuvanesh/OPTIONSMethodEnabled.git
cd OPTIONSMethodEnabled
pip install -r requirements.txt
````

> Make sure Python 3 is installed.

## 📁 Input File Format

* Plain text
* One domain per line

**Example `subdomains.txt`:**

```
example.com
testsite.org
secure.example.net
```

## 📦 Usage

### 🔹 Check a single domain

```bash
python OPTIONSMethodEnabled.py -u example.com
```

### 🔹 Check multiple domains from a file

```bash
python OPTIONSMethodEnabled.py -f subdomains.txt
```

## 📄 Example Output

```
[+] example.com supports OPTIONS. Allowed methods: GET, POST, OPTIONS
[-] anotherdomain.com responded with status code 403
[!] Error checking invalidsite.xyz: HTTPSConnectionPool...
```

## 📜 License

This project is open-source and available under the [MIT License](https://github.com/iambuvanesh/OPTIONSMethodEnabled/blob/main/LICENSE).

---
