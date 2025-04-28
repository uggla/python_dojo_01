#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from playwright.sync_api import sync_playwright

def save_as_pdf():

    chrome_path = "/usr/bin/google-chrome"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path=chrome_path)
        context = browser.new_context()
        page = context.new_page()

        try:
            hostname = os.getenv("HOSTNAME")
            output = os.getenv("OUTPUT", "output")
        except:
            print("Missing hostname or output env variables")
            sys.exit(1)

        url = f"http://{hostname}:8000/slides/{output}.html?print-pdf#/"
        pdf_output = f"/data/{output}.pdf"
        img_output = f"/data/{output}.png"
        poutput = f"{output}.pdf"

        print(f"Hostname: {hostname}")
        print(f"Url: {url}")

        # Open URL
        page.goto(url, wait_until="load")

        # Take a full-page screenshot
        page.screenshot(path=img_output, full_page=True)

        # Save page as PDF
        page.pdf(path=pdf_output, print_background=True,
                display_header_footer=False, prefer_css_page_size=True)

        print(f"PDF saved as {poutput}")

        browser.close()

def main():
    save_as_pdf()

if __name__ == "__main__":
    main()
