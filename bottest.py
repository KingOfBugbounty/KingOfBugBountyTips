import os

domain = input("Domain to Search: ")
subfile = f"{domain.split('.')[0]}_subs.txt"
http200 = f"{domain.split('.')[0]}_http200.txt"
portscan = f"{domain.split('.')[0]}_portscan.txt"
allports = "80,443,81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672"
crawKatana = f"{domain.split('.')[0]}_crawling.txt"
nucleiResp = f"{domain.split('.')[0]}_nuclei.txt"
xssgf = f"{domain.split('.')[0]}_gfxss.txt"
dalfox = "dalfox pipe --skip-bav --mining-dom  --deep-domxss --ignore-return -b 'https://ofjaaaaah.xss.ht/' --follow-redirects --silence"
dalfoxfile = f"{domain.split('.')[0]}_dalfox.txt"
crawKatanaJS = f"{domain.split('.')[0]}_crawlingJS.txt"
unfullDomains = f"{domain.split('.')[0]}_unfullDomains.txt"
fullDomains = f"{domain.split('.')[0]}_fulldomains.txt"
full1 = f"{domain.split('.')[0]}_fulldomains200.txt"
blacklist = "md,jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico"
katanalist = "js,jsp,json,php,aspx,asp"
UserAgent = "User-Agent: OFJAAAH"
#notify = "notify -provider discord -silent"

 
os.system(f"subfinder -all -d {domain} -silent -o {subfile}")
os.system(f"cat {subfile} | naabu -silent -p {allports} | anew {portscan}")
os.system(f"cat {portscan} | httpx -silent | anew {http200}")
os.system(f"cat {http200} | katana -d 10 -silent -o {crawKatana} -ef {blacklist} -em {katanalist}")
os.system(f"cat {crawKatana} | unfurl domains | anew {unfullDomains}")
os.system(f"cat {unfullDomains} {subfile} | anew {fullDomains}")
os.system(f"cat {fullDomains} | httpx -silent | anew {full1}")
os.system(f"cat {full1} | katana -d 10 -silent -em {katanalist} -o {crawKatanaJS}")
os.system(f"cat {full1} | nuclei -severity low,medium,high,critical -silent -o {nucleiResp} -H {UserAgent}")


