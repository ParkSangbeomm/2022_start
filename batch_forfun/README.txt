히즈넷 공지 자동 확인 프로그램

***크롬드라이버와, python3, pip가 필요함***

1. python 라이브러리 설치가 되어있는지 확인을 해야함
    - pip list --format=columns : 현재 설치되어 있는 라이브러리들 보여줌
   selenium, pyperclip가 설치되어 있어야함
   설치되어 있지 않다면 다음 명령어로 설치
    - pip install selenium
    - pip install pyperclip

2. ps 커맨드를 통해서 현재 켜져있는 프로세스를 확인해야함. headless로 프로그램이 돌아가기 때문에 종료가 되지 않으면 백그라운드에서 계속 메모리를 잡아먹음.
   확인 및 프로세스를 죽일때는 다음과 같은 명령어가 필요함
    - ps : 프로세스 확인
    - kill -9 [PID] : ps눌러서 나오는 프로세스 아이디 입력

3. 만약 배치파일이 권한이 부족해서 실행이 되지 않는다면 파일이 있는 위치로 가서 chmod +x [파일이름] 명령어를 입력해야함

4. hisnet_news 배치 파일의 3번째 줄에 실행시키고 싶은 파이썬 파일을 위치와함께 넣어야함

5. hisnet_new.py 는 학부공지만 확인하는 프로그램
   hisnet_news_test.py 는 일반공지를 확인하는 프로그램
    5-1. hisnet_new.py 는 새로운 공지가 몇 개인지 수를 비교해서 변화를 확인하는 프로그램
    5-2. hisnet_news_test.py 는 첫번째 공지의 이름을 비교해서 변화를 확인하는 프로그램 

6. 코드 내부 라인 기준
    37, 38 : 총 144번이 돌아가면 알아서 종료됨
    40 : 숫자가 초를 의미함(ex 300은 5분). 현재 학부공지는 5분 단위, 일반공지는 3분 단위로 실행됨.
    48 : 크롬드라이버 위치 넣어야함
    61, 68 : 아이디와 비밀번호를 넣으면 됨

7. 새로운 공지가 나오면 히즈넷이 켜짐