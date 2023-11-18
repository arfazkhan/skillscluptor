# Skill Scluptor

## Overview

This command line tool provides PDF file and URL analysis capabilities, controlled through command line arguments. Users can specify the file or URL to analyze and choose to run in debug mode.

## Basic Tool Algorithm

### Main
- `check_args()`: Function to handle command line arguments.

    - `PdfParser`: Class for PDF parsing.
        - `match_file()`: Method to match a file.
        - `parse_pdf()`: Method to parse PDF files.
            - `Scraper`: Class for web scraping.
                - `page_check()`: Method to check the number of pages.
                - `get_links()`: Method to extract links from a PDF.
                - `return_dict()`: Method to return a dictionary of links.

        - `Diverter`: Class for link diversion.
            - `search_links()`: Method to search for links.
                - `GitHub`: Class for GitHub-specific operations.

## GitHub Script Algorithm

### GitHub
- `__init__()`: Constructor method.
- `clean()`: Method to clean the GitHub link.
- `api()`: Method to perform GitHub API operations.
    - `keyword_analysis()`: Method to perform keyword analysis.
    - `benchmarking()`: Method to perform proficiency benchmarking.
        - `get_proficiency_score()`: Method to calculate the overall proficiency score.
            - `activity_score()`: Method to calculate the activity score.
                - Calculate the ratio of active repositories to total repositories.
            - `popularity_score()`: Method to calculate the popularity score.
                - Calculate the ratio of popular repositories to total repositories.
            - `quality_score()`: Method to calculate the code quality score.
                - Calculate the ratio of quality repositories to total repositories.
            - `open_source_score()`: Method to calculate the open source score.
                - Calculate the ratio of open source repositories to total repositories.
            - `complexity_score()`: Method to calculate the complexity score.
                - Calculate the ratio of complex repositories to total repositories.
            - `collaboration_score()`: Method to calculate the collaboration score.
                - Calculate the ratio of collaborative events to total repositories.
            - `learning_score()`: Method to calculate the learning and growth score.
                - Calculate the ratio of repositories focused on documentation and collaboration to total repositories.
    - `summarize()`: Method to generate a summary based on proficiency score.

## Usage

To analyze a PDF file or URL, run the tool from the command line and provide the necessary arguments. Use the debug mode flag to enable additional information during analysis.

Example:
```bash
python main.py -f path/to/file.pdf --debug
