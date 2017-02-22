import argparse

verbosity = False


# Change below placeholder to your information. 

MAIL_SENDER_ID = 'your-gmail-id@gmail.com'
MAIL_SENDER_PASSWORD = 'your-gmail-password'

RECIEVER_EMAIL = "reciever-email"
RECIEVER_NAME = "reciever's name" 

# End of placeholder


def parse_args():
    """
    get how many times should it run this script. 
    """
    parser = argparse.ArgumentParser(description="this script crawl and send the result to user email for n times.")
    parser.add_argument("num", type=int,
                        help="number of request to try")
    parser.add_argument("-v", "--verbosity", type=bool,
                        help="show verbose message")
    args = parser.parse_args()
    if args.verbosity:
        verbosity = True
    return args.num
    

    
def crawl():
    from bs4 import BeautifulSoup
    import urllib.request

    url = 'http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105'


    r = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(r, "lxml")
    
    headline_form = soup.find_all("ul", class_="type06_headline")[0]
    items = headline_form.find_all("li")

    headline_form = soup.find_all("ul", class_="type06")[0]
    items = items + headline_form.find_all("li")
    articles = []
    for item in items:
        # print(item.prettify())
        try:
            link_elements = item.find_all("a")
            title = link_elements[-1].get_text().strip()
            content_preview = item.find("dd").find(text=True, recursive=False).strip()
            link = link_elements[-1]['href']
            article = {}
            article['title'] = title
            article['content_preview'] = content_preview
            article['link'] = link
            articles.append(article)
        except:
            pass
            # print("cannot parse")
            # print(item.prettify())
        # break
        
    return articles
    
def send_email(user, pwd, recipient, subject, body):
    """
    Take Gmail id and password, use the account info to send email. 

    이메일을 보내려는 구글 계정의 아이디, 비밀번호 등을 받아서, 내가 원하는데로 이메일을 보냅니다.
    
    user: 구글 아이디
    pwd: 그 아이디 암호
    recipient: 고객님 이메일주소
    subject: 이메일 제목
    body: 이메일 내용
    """
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    message = MIMEText(TEXT.encode('utf-8'), _charset="utf--8")
    message['Subject'] = Header(SUBJECT.encode('utf-8'), "utf-8")
    message['From'] = FROM
    message['To'] = ". ".join(TO)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        print('login success')
        server.sendmail(FROM, TO, message.as_string())
        print('sendmail success')
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")
        
def write_and_send_mail(user, articles):
    target_email = user['email']
    target_name = user['name']

    subject = target_name+"님! 네이버 IT뉴스 속보입니다"
    response =  '다음은 속보 목록입니다.\n\n'
    for article in articles:
        response = response + "제목: " + article['title'] + "\n"
        response = response + "내용요약: " + article['content_preview'] + "\n"
        response = response + "링크: " + article['link'] + "\n"
        response = response + "\n"
        
    response = response + "\n\n이상 전달 끝!\n\n"
    send_email(MAIL_SENDER_ID, MAIL_SENDER_PASSWORD, target_email, subject, response)

if __name__ == '__main__':    
    num = parse_args()
    
    user = {}
    user['email'] = RECIEVER_EMAIL
    user['name'] = RECIEVER_NAME
    
    for i in range(num):
        articles = crawl()
        write_and_send_mail(user, articles)

    
    
