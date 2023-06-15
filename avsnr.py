import requests
r_s = requests.session()
import webbrowser
from time import sleep

print('''
               instagram : @arvsbr
               telegram channel @arsvbr
    ██████╗  █████╗ ███╗   ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
    ██╔══██╗██╔══██╗████╗  ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    ██████╔╝███████║██╔██╗ ██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
    ██╔══██╗██╔══██║██║╚██╗██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
    ██████╔╝██║  ██║██║ ╚████║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ \n''')

print('Please verify your information before registering it\nمن فضلك تاكد من معلوماتك قبل تسجيلها\n')
print('spam [1] \nbusiness [2] \nviolence [3] \nporn [4]\nManual [5]\n')
number1 = input('nmber : ')

if number1 == '1':
    def report_spam_easy(): # سبام

        spam_name = input('Your name : ')
        spam_username = input('Username : ')
        spam_email = input('Your email : ')

        url = 'https://www.facebook.com/ajax/help/contact/submit/page'

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'content-length': '921',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'fr=07trjqu9vVEDWnFgc..BggI_u...1.0.BggI_u.; datr=NpCAYGDo9894gkBjdeQep6Gb; wd=1366x581',
            'dnt': '1',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/help/instagram/contact/1652567838289083',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
            'x-fb-lsd': 'AVrZo3HBsNc'
        }

        data = {
            'jazoest': '2947',
            'lsd': 'AVrZo3HBsNc',
            'AccountType': 'Personal',
            'name': spam_name,
            'Field1489970557888767': spam_username,
            'email': spam_email,
            'Field236858559849125_iso2_country_code': '',
            'Field236858559849125': 'Saudi Arabia',
            'support_form_id': '1652567838289083',
            'support_form_hidden_fields': '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":true,"1615324488732156":true,"236548136468765":true}',
            'support_form_fact_false_fields': '[]',
            '__user': '0',
            '__a': '1',
            '__dyn': '7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa87i0n2US1kyE1e42C2218w5uwtU6e0D83mwaS0zE0I6aw',
            '__csr': '',
            '__req': '5',
            '__beoa': '0',
            '__pc': 'PHASED:DEFAULT',
            '__bhv': '2',
            '__no_rdbl': '0',
            'dpr': '1',
            '__ccg': 'MODERATE',
            '__rev': '1003660634',
            '__s': 'xn9ebq:cuks1u:d7qd87',
            '__hsi': '6953722469318193550-0',
            '__comet_req': '0',
            '__spin_r': '1003660634',
            '__spin_b': 'trunk',
            '__spin_t': '1619039678',
        }

        r = r_s.post(url, headers=headers, data=data).text

        print('request sent ✅')
        print('You will be answered by email')


    report_spam_easy()

if number1 == '2':
    def report_Business(): # تجاري

        Business_name = input('name : ')
        Business_username = input('username : ')
        Business_email = input('your email : ')

        url = "https://help.instagram.com/ajax/help/contact/submit/page"

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '914',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YG5AvAALAAEkMbUoaQn1-qDPRBwX; ig_did=C3F3DCD9-6B3A-47D4-A1F8-537AF1831A91; ig_nrcb=1; datr=3tF3YGjWgN7bOapnNZVh04Jr; shbid=14307; shbts=1619135575.6352756; csrftoken=MR8vmzxqQqC2RDT8rirEO3cG5kdFS6IT; ds_user_id=251639156; dpr=1.5',
            'origin': 'https://help.instagram.com',
            'referer': 'https://help.instagram.com/contact/1652567838289083?helpref=page_content',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'x-fb-lsd': 'AVpR0iagdDA',
        }

        data = {
            'jazoest': '2931',
            'lsd': 'AVpR0iagdDA',
            'AccountType': 'Business',
            'name': Business_name,
            'Field1489970557888767': Business_username,
            'email': Business_email,
            'Field236858559849125_iso2_country_code': '',
            'Field236858559849125': 'Saudi Arabia',
            'support_form_id': '1652567838289083',
            'support_form_hidden_fields': '{"904224879693114":false,"495070633933955":false,"1489970557888767":false,"488955464552044":false,"236858559849125":false,"1638971086372158":false,"1615324488732156":false,"236548136468765":false}',
            'support_form_fact_false_fields': '[]',
            '__user': '0',
            '__a': '1',
            '__dyn': '7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE0I6aw',
            '__csr': '',
            '__req': '5',
            '__beoa': '0',
            '__pc': 'PHASED:DEFAULT',
            '__bhv': '2',
            '__no_rdbl': '0',
            'dpr': '1.5',
            '__ccg': 'GOOD',
            '__rev': '1003674731',
            '__s': '5mag8q:u8g4ws:tp6de5',
            '__hsi': '6954303624420095857-0',
            '__comet_req': '0',
            '__spin_r': '1003674731',
            '__spin_b': 'trunk',
            '__spin_t': '1619174989',
        }

        r = r_s.post(url, headers=headers, data=data).text

        print('Done send | wait 15 minutes ')
        print('Check your email... ')

    report_Business()

if number1 == '3':
    def report_violence(): # عنف

        violence_name = input('name : ')
        violence_email = ('email for report acc : ')
        violence_username = input('username : ')
        violence_MN = input('your phone : ')

        violence_massege = ('Hello there is someone'
                            'They claim that I am publishing racism and my personal account item'
                            'But I do not have my personal account, I’m not racist, and you can check that and I will post clips to me personally '
                            'Just help me please beg you I wish you a humorous arithmetic band '
                            'as fast as possible'
                            f'my email:{violence_email}'
                            f'user name:{violence_username}'
                            'So, could you help me to restore my account? Please, help me to restore my account because , I don t want to lose my account .')

        url = "https://help.instagram.com/ajax/help/contact/submit/page"

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '914',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YG5AvAALAAEkMbUoaQn1-qDPRBwX; ig_did=C3F3DCD9-6B3A-47D4-A1F8-537AF1831A91; ig_nrcb=1; datr=3tF3YGjWgN7bOapnNZVh04Jr; shbid=14307; shbts=1619135575.6352756; csrftoken=MR8vmzxqQqC2RDT8rirEO3cG5kdFS6IT; ds_user_id=251639156; dpr=1.5',
            'origin': 'https://help.instagram.com',
            'referer': 'https://help.instagram.com/contact/1652567838289083?helpref=page_content',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'x-fb-lsd': 'AVpR0iagdDA',
        }

        data = {

            'jazoest': '2864',
            'lsd': 'AVpR0iag50A',
            'name': violence_name,
            'email': violence_email,
            'instagram_username': violence_username,
            'mobile_number': violence_MN,
            'appeal_reason': violence_massege,
            'support_form_id': '606967319425038',
            'support_form_hidden_fields': '{ }',
            'support_form_fact_false_fields': '[]',
            '__user': '0',
            '__a': '1',
            '__dyn': '7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642 - 7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5 - 0jx0Fwww6DwtU6e0D83mwaS0zE0I6aw',
            '__csr': '',
            '__req': '8',
            '__beoa': '0',
            '__pc': 'PHASED:DEFAULT',
            '__bhv': '2',
            '__no_rdbl': '0',
            'dpr': '1.5',
            '__ccg': 'GOOD',
            '__rev': '1003674731',
            '__s': 'vn2qg3:u8g4ws: yuj7ac',
            '__hsi': '6954309849736242370 - 0',
            '__comet_req': '0',
            '__spin_r': '1003674731',
            '__spin_b': 'trunk',
            '__spin_t': '1619176438',
        }

        r = r_s.post(url, headers=headers, data=data).text

        print('Done send | wait 15 minutes ')
        print('Check your email... ')


    report_violence()

if number1 == '4':
    def porn():

        porn_name = input('name : ')
        porn_username = input('username : ')
        porn_email = input('email : ')
        porn_phone = input('phone : ')
        porn_text = f'Hi my name is {porn_name} from KSA I have been using Instagram for 4 years, and I did not violate the rules of the company respected. I just had a campaign of reports to disable my account because I was fighting extortionists. I hope to recover my account and I am happy to reply if it is good or not good for me. Finally, my Arab brother, who is in the technical support of the company, please help me and bring me back my account because hackers and blackmailers have become many in Arab societies and I fight this phenomenon. please help me'

        url = 'https://help.instagram.com/contact/606967319425038?helpref=page_content'

        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '701',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YG5AvAALAAEkMbUoaQn1-qDPRBwX; ig_did=C3F3DCD9-6B3A-47D4-A1F8-537AF1831A91; ig_nrcb=1; datr=3tF3YGjWgN7bOapnNZVh04Jr; shbid=17869; shbts=1620697371.3704317; csrftoken=HDcpPLNGRzK23zvBvmltr7JD7UM9OhMu; ds_user_id=497206816; sessionid=497206816%3Aot01Zg2dFkiXMY%3A19; dpr=1.5',
            'origin': 'https://help.instagram.com',
            'referer': 'https://help.instagram.com/contact/606967319425038?helpref=page_content',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
            'sec-ch-ua-mobile': '?0',
        }

        data = {
            'jazoest': '2863',
            'lsd': 'AVpIE7-iCyA',
            f'name': {porn_name},
            f'email': {porn_email},
            f'instagram_username': {porn_username},
            'mobile_number': {porn_phone},
            'appeal_reason': {porn_text},
            'support_form_id': '606967319425038',
            'support_form_hidden_fields': '{}',
            'support_form_fact_false_fields': '[]',
            '__user': '0',
            '__a': '1',
            '__dyn': '7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE0I6aw',
            '__csr': '',
            '__req': '4',
            '__beoa': '0',
            '__pc': 'PHASED:DEFAULT',
            '__hs': '18762.PHASED:DEFAULT.2.0',
            '__bhv': '2',
            'dpr': '1.5',
            '__ccg': 'GOOD',
            '__rev': '1003797623',
            '__s': '20v2cx:vubja1:s4m7bt',
            '__hsi': '6962331872811420648-0',
            '__comet_req': '0',
            '__spin_r': '1003797623',
            '__spin_b': 'trunk',
            '__spin_t': '1621044211',
        }

        r = r_s.post(url , headers=headers , data=data).text

        print('Done send | wait 15 minutes ')
        print('Check your email... ')
    porn()

if number1 == '5':
    def links():
        print('\nspam [1] \nbusiness [2] \nviolence [3] \nporn [4]\n')

        num = input('number : ')

        if num == '1':
            print('SPAM : https://www.facebook.com/ajax/help/contact/submit/page\n')
            webbrowser.open('https://www.facebook.com/ajax/help/contact/submit/page')

        if num == '2':
            print('BUSINESS : https://help.instagram.com/ajax/help/contact/submit/page\n')
            webbrowser.open('https://help.instagram.com/ajax/help/contact/submit/page')
        if num == '3':
            print('VIOLENCE : https://help.instagram.com/ajax/help/contact/submit/page\n')
            webbrowser.open('https://help.instagram.com/ajax/help/contact/submit/page')

            print('Hello there is someone They claim that I am publishing racism and my personal account item But I do not have my personal account, I’m not racist, and you can check that and I will post clips to me personal Just help me please beg you I wish you a humorous arithmetic band as fast as possible my email: ((email)) user name: ((username)) So, could you help me to restore my account? Please, help me to restore my account because , I don t want to lose my account .')
            sleep(100)
        if num == '4':
            print('PORN : https://help.instagram.com/contact/606967319425038?helpref=page_content\n')
            webbrowser.open('https://help.instagram.com/contact/606967319425038?helpref=page_content')

            print('Hi my name is ((name)) from KSA I have been using Instagram for 4 years, and I did not violate the rules of the company respected. I just had a campaign of reports to disable my account because I was fighting extortionists. I hope to recover my account and I am happy to reply if it is good or not good for me. Finally, my Arab brother, who is in the technical support of the company, please help me and bring me back my account because hackers and blackmailers have become many in Arab societies and I fight this phenomenon. please help me')
            sleep(100)
    links()
#hello @arvsbr is here
