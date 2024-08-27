import os
import re
import requests
from bs4 import BeautifulSoup

HOSTS_PATH = "/etc/hosts" if os.name == 'posix' else r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"


def block_websites(websites):
    """Blocks websites by modifying the hosts file."""
    with open(HOSTS_PATH, 'r+') as hosts_file:
        content = hosts_file.read()
        for website in websites:
            if website not in content:
                hosts_file.write(f"{REDIRECT_IP} {website}\n")
                print(f"Blocked {website}")


def unblock_websites(websites):
    """Unblocks websites by removing entries from the hosts file."""
    with open(HOSTS_PATH, 'r+') as hosts_file:
        content = hosts_file.readlines()
        hosts_file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                hosts_file.write(line)
        hosts_file.truncate()
        print(f"Unblocked {', '.join(websites)}")


def scrape_websites(urls):
    """Extract data from websites to identify patterns."""
    extracted_urls = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('http'):
                    extracted_urls.append(href)
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return extracted_urls


def pattern_recognition(urls, pattern):
    """Identify and filter websites based on a pattern."""
    regex = re.compile(pattern)
    matched_urls = [url for url in urls if regex.search(url)]
    return matched_urls


def main():
    print("Welcome to the Website Blocker Application")
    action = input("Do you want to (b)lock or (u)nblock websites? ").strip().lower()

    if action not in ('b', 'u'):
        print("Invalid option.")
        return

    websites = input("Enter the websites to block/unblock (comma separated): ").split(',')
    websites = [website.strip() for website in websites]

    if action == 'b':
        block_websites(websites)
    elif action == 'u':
        unblock_websites(websites)

    pattern = input("Enter a regex pattern to match websites (or press Enter to skip): ").strip()
    if pattern:
        extracted_urls = scrape_websites(websites)
        matched_urls = pattern_recognition(extracted_urls, pattern)
        print(f"Websites matching pattern '{pattern}': {', '.join(matched_urls)}")


if __name__ == "__main__":
    main()
