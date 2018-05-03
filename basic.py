# .*. coding: utf8 .*.
#문자열 출력
print "python" 

#변수 선언
msg = "hello python"
print msg
# 문자열 슬라이싱
print msg[1:3]
print msg[-3:]
print msg[:-2]
print msg[::-1]

#리스트
data = []
#리스트 자료 입력
data.append("hi")
data.append(123)
data.append(1.2)
#리스트 출력
print data
#리스트 데이터 제거
data.pop()
print data
data.pop()
print data
#리스트 요소 인덱스 검색
print data.index("hi")
#인덱스 검색시 에러발생
#print data.index("hi222")

#사전(딕셔너리)
#{키 : 값}
user = {}
user['me'] = {'age': 30, 'address':'daejeon'}
user['you'] = {'age': 22, 'address':'seoul'}
#사전 출력
print user
# 사전 데이터 검색 키 활용
print user['me']
print "user keys:", user.keys()
print "me" in user.keys()

#제어
#if, if else, if elif else
num=4
if num > 0:
    print "num >0"

if num > 5:
    print "num >5"
else:
    print "num <5"

if num % 2 == 0:        #나머지 연산
    print "even"
elif num % 2 == 1:
    print "odd"
else:
    print "????"

#함수
def addition(numbers):  #numbers는 인자이다. :는 정의(스코프를 가진다.) 함수안에서만 참조가능
    result = 0
    for number in numbers:
        result += number
    return result

    data = [1, 2, 3]
    print addition(data)

    def help():
        print "id ----- print user id"
        print "pwd ----- print current path"
        print "quit ----- exit program"
        print "ip ----- print ip address"
    
    help()
# 라이브러리 불러오기
import os
import platform
import subprocess
# 무한루프
def shell():
    while True:
        cmd = raw_input('>>> ')
        if cmd == 'id':
            if platform.system() == 'Windows':
                print os.environ.get("USERNAME")    #os라이브러리 불러와서 id 출력
            else:
                print os.getenv('USER')             #큰 틀을 잡고 하나씩 구현할 때 pass 사용    
        elif cmd == 'pwd':
            print os.getcwd()
            pass
        elif cmd == 'quit':
            print "bye~"
            break                                   #무한루프 탈출     
        elif cmd == 'ip':                           #IP주소 확인코드 만들기
            if platform.system() =='Windows':
                buf = subprocess.check_output('ipconfig')
                index = buf.find("IPv4")             #전체에서 IPv4를 찾는다
                newline = buf[index:].find("\n")     #인덱스로부터 다음줄로 가려면 몇칸이나 가야하는가를 newline에 저장
                #print index, newline                 
                ipline = buf[index:index+newline]    #[index:index+newline]은 index에서 시작해서 index+newline에서 끝남-> 한줄을 의미
                ip = ipline.split(':')
                print ip[1].strip()                  #strip->앞의 공백 하나를 벗겨낸다
            else:
                buf = subprocess.check_output('ifconfig')
                target = 'addr:'
                index = buf.find(target) + len(target)
                space = buf[index:].find(' ')
                #print index, space
                print buf[index:index+space]
        else:
            help()
    
#urlib2 사용
import urllib2
import re
url = 'https://box.cdpython.com/ezen/'
req = urllib2.Request(url)               #url 요청으로 변환
res = urllib2.urlopen(req)
html = res.read()
#print html 
#re 모듈(정규표현식)을 사용한 패턴 매칭
ipaddress, port = re.findall("\d+\.\d+\.\d+\.\d+\/\d+",html)[0].split('/') #split 두정보를 쪼개준다
print "ip:", ipaddress, "port:", port