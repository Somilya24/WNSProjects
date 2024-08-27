# Website Blocker and Scraper Application

## Project Background

This project is a Python-based tool designed to help users block or unblock websites by modifying the system's `hosts` file. Additionally, it can scrape websites for links and identify patterns in the URLs using regular expressions. This can be useful for monitoring, filtering, or analyzing web content.

## Features
- **Block Websites:** Redirect websites to `127.0.0.1` by adding entries to the `hosts` file.
- **Unblock Websites:** Remove previously added entries from the `hosts` file.
- **Scrape Websites:** Extract all links from the specified websites.
- **Pattern Recognition:** Identify and filter URLs based on a user-defined regular expression pattern.

## How to Run the Code

### Prerequisites
- Python 3.x
- Admin or root privileges (necessary for modifying the `hosts` file)

### Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Somilya24/WNSProjects.git
   cd WebsiteBlocker
   
2. **Install Required Packages:**
Install the required Python libraries using pip:
    ```bash
    pip install requests beautifulsoup4
   
3. **Run the Application:**
   Execute the script using Python:
   ```bash
   python WebsiteBlocker.py

## Usage
1. **Blocking or Unblocking Websites:**

    The program will prompt you to choose between blocking or unblocking websites.
    Enter the websites you wish to block/unblock as a comma-separated list.

   
2. **Pattern Recognition:**


    After blocking/unblocking, the application allows you to enter a regex pattern to match URLs from the given websites. If you skip this step, the program will end.
## Example Screenshots
1. Blocking Websites:
This screenshot shows the application blocking websites by modifying the hosts file.
![Screenshot (518)](https://github.com/user-attachments/assets/57bbcac6-8d5e-46a8-923d-ca413a9a9a14)
2. Unblocking Websites:
This screenshot demonstrates unblocking websites, removing entries from the hosts file.
![Screenshot (519)](https://github.com/user-attachments/assets/8027ef55-8b49-4226-851b-16e715fa5572)
## Important Notes
1. **Permissions:** Ensure you have the necessary administrative or root permissions to modify the hosts file.

2. **Responsibility:** Use this tool responsibly, especially when blocking or scraping websites.

## Conclusion
This application offers a simple yet powerful way to manage website access and analyze web content. Whether for productivity, parental control, or research, this tool provides a straightforward interface for interacting with the web.

