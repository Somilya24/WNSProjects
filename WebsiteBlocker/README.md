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

# Code Overview

1. **Imports**

   - **`os`**: Provides a way of using operating system-dependent functionality. Here, it is used to determine the path of the hosts file.
   - **`re`**: Provides regular expression matching operations, used for pattern recognition.
   - **`requests`**: Used for making HTTP requests to fetch website content.
   - **`BeautifulSoup`**: A library used for parsing HTML and XML documents, used to scrape data from websites.

2. **Constants**

   - **`HOSTS_PATH`**: This constant determines the path of the hosts file based on the operating system (`/etc/hosts` for Unix-like systems and `C:\Windows\System32\drivers\etc\hosts` for Windows).
   - **`REDIRECT_IP`**: The IP address to which blocked websites will be redirected (typically `127.0.0.1` for localhost).

3. **Functions**

   - **`block_websites(websites)`**:
     - **Purpose**: Blocks websites by modifying the hosts file, redirecting them to `127.0.0.1`.
     - **Parameters**: `websites` (list) - A list of website URLs to block.
     - **Operation**:
       - Opens the hosts file in read and append mode (`r+`).
       - Checks if each website is already blocked.
       - If not, it appends an entry to the hosts file to block the website.
  
   - **`unblock_websites(websites)`**:
     - **Purpose**: Unblocks websites by removing entries from the hosts file.
     - **Parameters**: `websites` (list) - A list of website URLs to unblock.
     - **Operation**:
       - Opens the hosts file in read and write mode (`r+`).
       - Reads the content of the file and checks each line.
       - Removes lines that contain the specified websites.
       - Truncates the file to remove any excess data.
  
   - **`scrape_websites(urls)`**:
     - **Purpose**: Scrapes URLs from the provided websites to extract all the hyperlinks (`<a href>` tags).
     - **Parameters**: `urls` (list) - A list of website URLs to scrape.
     - **Operation**:
       - Sends a GET request to each URL using the `requests` library.
       - Parses the HTML response using BeautifulSoup.
       - Extracts and returns all hyperlinks that start with `http`.

   - **`pattern_recognition(urls, pattern)`**:
     - **Purpose**: Identifies and filters websites based on a given regular expression pattern.
     - **Parameters**:
       - `urls` (list): A list of URLs to be checked.
       - `pattern` (str): A regular expression pattern to match against the URLs.
     - **Operation**:
       - Compiles the given pattern using the `re` module.
       - Filters the list of URLs and returns only those that match the pattern.

4. **`main()` Function**

   - **Purpose**: Acts as the entry point for the application.
   - **Operation**:
     - Prompts the user for an action: block or unblock websites.
     - Takes a list of websites as input from the user.
     - Calls the respective function (`block_websites` or `unblock_websites`) based on user input.
     - Optionally, allows the user to input a regex pattern to match websites.
     - If a pattern is provided, scrapes the provided websites and identifies URLs matching the pattern using `pattern_recognition`.

5. **`if __name__ == "__main__":`**

   - Ensures that the `main()` function is called only when the script is run directly and not imported as a module.


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

