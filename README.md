# Pattern-Matching

<img src="./images/patterns.png" >

## Options

```
python3 ./pm.py -h                                                                                                                     ─╯
usage: pm.py [-h] -u URL_FILE -p PATTERN [-o OUTPUT] [-a]

Match patterns from a file in URLs and print/save truncated results.

options:
  -h, --help            show this help message and exit
  -u URL_FILE, --url-file URL_FILE
                        File containing URLs
  -p PATTERN, --pattern PATTERN
                        Pattern file to use (e.g., xss.txt)
  -o OUTPUT, --output OUTPUT
                        File to save output results (optional)
  -a, --after           Include pattern values in the output
```

## Usage

```
python3 ./pm.py -u All_Urls.txt -p secrets.txt
```
