# Pattern-Matching

<img src="./images/patterns.png" >

## Options

```
pm -h
usage: pm [-h] [-u URL_FILE] -p PATTERN [-o OUTPUT] [-a]

Match patterns from a file in URLs and print/save truncated results.

options:
  -h, --help            show this help message and exit
  -u URL_FILE, --url-file URL_FILE
                        File containing URLs (optional, stdin is used if not provided)
  -p PATTERN, --pattern PATTERN
                        Pattern file to use (e.g., xss.txt)
  -o OUTPUT, --output OUTPUT
                        File to save output results (optional)
  -a, --after           Include pattern values in the output

Examples:
  pm -u urls.txt -p xss.txt
  pm -u urls.txt -p sqli.txt -o results.txt
  pm -u urls.txt -p rce.txt -a
```

## Usage
```
pm -u params.txt -p /opt/Pattern-Matching/patterns/xss.txt -r "XSS" -o xss_params_output.txt
```
```
pm -u All_Urls.txt -p secrets.txt -o secret-output.txt
```

## Piping
```
cat urls.txt | pm -p tools/Pattern-Matching/patterns/sqli.txt
```

## installation

```
cd /opt/
sudo git clone https://github.com/bhunterex/Pattern-Matching.git
cd
sudo chmod +x /opt/Pattern-Matching/pm.py
sudo ln -sf /opt/Pattern-Matching/pm.py /usr/local/bin/pm
pm -h
```
