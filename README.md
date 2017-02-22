# aws-lambda-scheduled-python3-script
shows how to run python3 script on AWS Lambda periodically

This project shows how to run python3 script periodically on AWS Lambda.
이 프로젝트는 Python3로 작성된 스크립트를 주기적으로 AWS Lambda 위에서 실행시키는 것을 보여줍니다.

This demo runs myrobot.py script which crawls Naver IT News Section(Korean News Portal) Page and send it to personal email via Gmail.

User must modify placeholder for Gmail Login, and reciever's email address. 

## How to Run, 실행방법

Open myrobot.py with your favorite editor. Edit 
myrobot.py 스크립트를 원하는 에디터로 열어서 다음 부분을 수정합니다.


> MAIL_SENDER_ID = 'your-gmail-id@gmail.com'
>
> MAIL_SENDER_PASSWORD = 'your-gmail-password'
> 
> RECIEVER_EMAIL = "reciever-email"
>
> RECIEVER_NAME = "reciever's name" 

with correct information.
로그인이 가능하고, 이메일을 받을 수 있는 유효한 값을 입력하여야합니다.

Upload this on AWS Instance to run make command. It will build wrapped python code for AWS Lambda.
Follow instruction from http://www.cloudtrek.com.au/blog/running-python-3-on-aws-lambda/

이 코드를 어떻게 AWS Lambda에 올릴 수 있는지는 여기를 참조하세요. 

## Sample Run on Your Machine, 내 컴퓨터에서 테스트 실행해보기

It is always good idea to test code before deployment. After modifying myrobot.py, you can check 
the script by running with terminal `python3 myrobot.py 1`.

코드를 업로드하기 전에 정상 작동하는지를 체크하는것은 좋은 습관입니다. myrobot.py를 위 설명대로 수정한 후 
`python3 myrobot.py 1`을 입력해서 잘 작동하나 테스트해보세요. 

Don't forget to run `pip install -r requirements.txt` in virtualenv.
파이썬 가상환경(virtualenv)를 만든 후 필요한 패키지를 `pip install -r requirements.txt` 설치하는것을 잊지 마세요.


## Acknowledge

http://www.cloudtrek.com.au/blog/running-python-3-on-aws-lambda/
