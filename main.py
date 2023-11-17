import sys
import argparse
import os
from PyPDF2 import PdfReader
import re
import tldextract
import requests
from src.engines.github import GitHub

class PdfParser:
    def __init__(self, input_list, debug=False):
        self.input_list = input_list
        self.debug = debug

    @staticmethod
    def match_file(file_name):
        data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        file_path = os.path.join(data_folder, file_name)

        if os.path.isfile(file_path):
            return file_path
        else:
            return None

    def parse_pdf(self, input_list, debug_val=False):
        for item in input_list:
            file_insight = self.match_file(item)

            if file_insight is None:
                print(f"File {item} not found, recheck the names")
                continue

            reader = PdfReader(file_insight)
            num_pages = len(reader.pages)

            if debug_val:
                print("File opened")

            if Scraper.page_check(num_pages):
                print("Number of pages is okay")
                lookup_links = Scraper.get_links(reader)
                if debug_val:
                    print(lookup_links)
                links_dict = Scraper.return_dict(lookup_links)
                diverter = Diverter(links_dict, debug_val)
                diverter.search_links()

                for domain, links in links_dict.items():
                    print(f"Domain: {domain}")
                    for link in links:
                        print(f"Link: {link}")
            else:
                print("Number of pages is not okay")
                continue

class Scraper:
    @staticmethod
    def page_check(num_pages):
        max_page_threshold = 4
        min_page_threshold = 1

        if num_pages > max_page_threshold or num_pages < min_page_threshold:
            return False
        return True

    @staticmethod
    def get_links(reader):
        links = []
        for page in reader.pages:
            page_text = page.extract_text()
            regex = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
            page_links = regex.findall(page_text)
            links.extend([link[0] for link in page_links])
        return links

    @staticmethod
    def return_dict(links):
        res_dict = {}
        for link in links:
            domain = tldextract.extract(link).domain
            if domain not in res_dict:
                res_dict[domain] = []
            res_dict[domain].append(link)
        return res_dict

class Diverter:
    def __init__(self, links, debug=False):
        self.debug = debug
        self.links = links

    def search_links(self):
        links = self.links

        for domain, link_list in links.items():
            if domain.lower() == 'github':
                for link in link_list:
                    if isinstance(link, str):  # Check if the link is a string
                        github = GitHub(link)  # Create an instance of GitHub with the link
                        github.clean()
                        github.api()
                    else:
                        print(f"Invalid link for domain {domain}: {link}")

# main.py
def check_args():
    parser = argparse.ArgumentParser(description='PDF parser endpoint')
    parser.add_argument('-f', '--file', help='File to parse')
    parser.add_argument('-u', '--url', help='Url to parse')
    parser.add_argument('-d', '--debug', help='Debug mode', action='store_true')

    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        return

    filenames = [args.file] if args.file else []
    url_list = [args.url] if args.url else []

    if filenames:
        parser = PdfParser(filenames, args.debug)
        parser.parse_pdf(filenames, args.debug)
    elif url_list:
        parser = PdfParser(url_list, args.debug)
        parser.parse_pdf(url_list, args.debug)
    else:
        print("Please provide either a file or URL to parse.")

if __name__ == "__main__":
    check_args()