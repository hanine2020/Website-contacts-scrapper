

# Website Scraper for Contact Information

This Website Scraper is a Python script designed for automated data extraction from websites. It scrapes web pages and PDF files to extract contact information such as email addresses and phone numbers. The script uses multithreading to process multiple links concurrently, improving efficiency.

## Features

- Scrapes websites for links and extracts text content.
- Identifies and prints contact information (emails and phone numbers) from web pages.
- Processes PDF files to extract text and identify contact information.
- Uses multithreading to process multiple links concurrently for improved performance.
- Utilizes `tqdm` for progress tracking.

## Dependencies

The script requires the following Python libraries:

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.
- `re`: For regular expressions to find contact information.
- `threading`: For multithreading.
- `tqdm`: For displaying progress bars.
- `PyMuPDF` (`fitz`): For processing PDF files.

## Script Explanation
### 1. normalize(url, link)
This function normalizes links to ensure they are complete URLs. It handles relative paths, absolute paths, and full URLs.

### 2. contact_phone_check(format_txt)
This function checks if a given text contains contact information using regular expressions for email addresses and phone numbers.

### 3. pdf_check(url)
This function checks if a URL points to a PDF file based on the file extension.

### 4. process_pdf_link(pdf_url)
This function processes PDF files. It downloads the PDF, extracts text from each page, and prints it if contact information is found.

### 5. process_link(normalized_link, pbar)
This function processes individual links. It handles both PDF and HTML links, extracting and printing text with contact information. It updates the progress bar after processing each link.

### 6. scrape_website(url)
This function initiates the web scraping process. It fetches the initial page, extracts links, and processes each link using multithreading.

## Notes
- The script avoids processing certain file types (e.g., images, videos) by checking the file extensions in the URLs.
- Make sure the website you are scraping allows web scraping by checking its robots.txt file and terms of service.
- In the `main()` function, specify the website URL you want to scrape by updating the `url` variable:
## License
This project is licensed under the MIT LICENSE.
