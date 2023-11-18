- Main
  |
  └── check_args()  # Function to handle command line arguments
      |
      └── PdfParser  # Class for PDF parsing
          |
          ├── match_file()  # Method to match a file
          |
          ├── parse_pdf()  # Method to parse PDF files
          |   |
          |   └── Scraper  # Class for web scraping
          |       |
          |       ├── page_check()  # Method to check the number of pages
          |       |
          |       ├── get_links()  # Method to get links from a PDF
          |       |
          |       └── return_dict()  # Method to return a dictionary of links
          |
          └── Diverter  # Class for link diversion
              |
              └── search_links()  # Method to search for links
                  |
                  └── GitHub  # Class for GitHub-specific operations