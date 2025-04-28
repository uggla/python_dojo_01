#!/usr/bin/env -S uv run
# -*- coding: utf-8 -*-

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "staticjinja",
# ]
# ///
import http.server
import socketserver
import os
import subprocess
import sys
import argparse

PORT = 8000
SLIDES_DIR = "slides"
Handler = http.server.SimpleHTTPRequestHandler


def check_tools():
    try:
        subprocess.check_output("which staticjinja >/dev/null 2>&1", shell=True)

        if not os.path.exists("reveal.js/package.json"):
            raise FileNotFoundError
    except subprocess.CalledProcessError:
        print(
            "staticjinja is missing, " "Please install it with pip install staticjinja",
            file=sys.stderr,
        )
        sys.exit(1)
    except FileNotFoundError:
        print(
            "Could not find reveal.js, "
            "Please get the submodules using "
            "git submodule init && git submodule update",
            file=sys.stderr,
        )


def serve_content():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at http://localhost:{}".format(PORT))
        httpd.serve_forever()


def build_presentations():
    print("Building presentation for {}".format(SLIDES_DIR))
    os.chdir(SLIDES_DIR)
    subprocess.check_output("staticjinja build", shell=True)
    os.chdir("..")


def watch():
    print("\033[32mStaticjinja watch for {}\033[0m".format(SLIDES_DIR))
    os.chdir(SLIDES_DIR)
    command = ["staticjinja", "watch"]  # Replace with your shell command and arguments

    # Run the command in the background
    process = subprocess.Popen(
        command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    os.chdir("..")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--watch", help="Watch for template changes", action="store_true"
    )
    args = parser.parse_args()

    check_tools()
    build_presentations()
    if args.watch:
        watch()
    serve_content()


if __name__ == "__main__":
    main()
