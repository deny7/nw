# .*. coding: utf8 .*.
# 소켓 라이브러리 로딩
import socket
import threading
def handler(conn, adress):
        while True: 
            try:
                # 클라이언트가 전송한 데이터 수신
                data = conn.recv(1024)
            except:
                print "Exception!!"
                break
            print "address %s sent data %s" % (address[0], data)
            if not data:
                #데이터를 보내지 않은 클라이언트 연결 종료
                conn.close()
                break
            print "address %s send data: %s"% \
                ( address[0], data)
            # 수신 데이터를 클라이언트에 전송 
            conn.send(data)                   #=> 들여쓰기 잘못됨!!
# 서버 정보
# * = (와일드카드, 모두)
info = ("0.0.0.0", 9999)
# 소켓 생성
s = socket.socket()
# 9999번 포트 바인딩
s.bind(info)                                # 통로 연다는 의미
# 바인딩 포트 리스닝
s.listen(5)    
while True:                                 # 동시 5개까지 본다는 의미(크게 줘도 무방하다.)
    # 접속요청 승인 === 개선사항1: 위의 While문에 쓰레드thread를 줘야됨!!!!! 
    conn, address = s.accept()              # 서버의 역할=바인딩, 리스닝, 승인
    print "[+] new connection from %s(%d)" % (address[0], address[1])
    th = threading.Thread(target=handler, args=(conn, address))
    th.start()