#!/usr/bin/env python3
import re
import argparse
import sys

def load_patterns(pattern_file):
    try:
        with open(pattern_file, 'r') as file:
            patterns = file.read().splitlines()
        return patterns
    except FileNotFoundError:
        print(f"Error: File {pattern_file} not found.")
        return []

def process_urls(urls, patterns, output_file=None, after_match=False):
    results = []

    for url in urls:
        url = url.strip()
        for pattern in patterns:
            # Escape pattern to handle special characters
            regex = re.compile(f"({re.escape(pattern)}[^&]*)")
            match = regex.search(url)
            if match:
                if after_match:
                    # After the value, check for space or '&' and truncate accordingly
                    end_pos = match.end()
                    if len(url) > end_pos and (url[end_pos] == ' ' or url[end_pos] == '&'):
                        # Truncate everything after space or '&'
                        result = url[:end_pos]
                    else:
                        result = url[:match.end()]
                else:
                    # Include pattern but exclude value
                    result = url[:match.start() + len(match.group(1).split("=")[0]) + 1]
                print(result)  # Print each matched result
                results.append(result)  # Add to the results list
                break  # Stop checking after the first match in this URL

    # Write results to the output file if specified
    if output_file:
        try:
            with open(output_file, 'w') as file:
                file.write("\n".join(results))
            print(f"Results saved to {output_file}")
        except IOError:
            print(f"Error: Could not write to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Match patterns from a file in URLs and print/save truncated results.",
        epilog="Examples:\n"
               "  pm -u urls.txt -p patterns.txt\n"
               "  pm -u urls.txt -p patterns.txt -o results.txt\n"
               "  pm -u urls.txt -p patterns.txt -a",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-u", "--url-file", help="File containing URLs (optional, stdin is used if not provided)")
    parser.add_argument("-p", "--pattern", required=True, help="Pattern file to use (e.g., xss.txt)")
    parser.add_argument("-o", "--output", help="File to save output results (optional)")
    parser.add_argument("-a", "--after", action="store_true", help="Include pattern values in the output")

    args = parser.parse_args()

    # Load patterns from the file provided in -p
    patterns = load_patterns(args.pattern)
    if not patterns:
        print(f"Error: No patterns loaded from the file {args.pattern}.")
        exit(1)

    # Load URLs from file or stdin
    if args.url_file:
        try:
            with open(args.url_file, 'r', encoding='utf-8') as file:
                urls = file.readlines()
        except UnicodeDecodeError:
            with open(args.url_file, 'r', encoding='iso-8859-1') as file:
                urls = file.readlines()
        except FileNotFoundError:
            print(f"Error: File {args.url_file} not found.")
            exit(1)
    else:
        if sys.stdin.isatty():
            print("Error: No input URLs provided via stdin or -u.")
            exit(1)
        try:
            # Read stdin as bytes first
            raw_input = sys.stdin.buffer.read()
            try:
                urls = raw_input.decode('utf-8').splitlines()
            except UnicodeDecodeError:
                # Fallback to iso-8859-1 if UTF-8 fails
                urls = raw_input.decode('iso-8859-1').splitlines()
        except Exception as e:
            print(f"Error reading stdin: {e}")
            exit(1)

    process_urls(urls, patterns, args.output, args.after)
