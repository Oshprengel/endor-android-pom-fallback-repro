import requests


def main():
    r = requests.get("https://example.com")
    print(r.status_code)


if __name__ == "__main__":
    main()
