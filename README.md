# apple_watcher
  
30분마다 애플 공홈의 맥북15인치 고급형 모델의 구매버튼이 활성화 되어있는지 체크합니다.
구매버튼이 활성화되면 프로그램 시작시 입력한 전화번호로 '구매 가능'이라고 iMessage를 보냅니다.

## 요구사항
  - Python 3
  
  For Linux(Ubuntu, Debian, Mint):
  ```bash
  $ sudo apt-get install python3 python3-pip
  ```
  For Max OS X:
  ```bash
  $ brew install python
  ```
  
  홈브류가 없을 시 https://www.python.org/getit/ 참고해서 설치하세요.
  
  
## 설치 및 실행
```bash
$ source /path/to/venv/bin/activate
(venv)$ pip install -r requirements.txt
(venv)$ python apple_watcher
(venv)$ 전화번호를 입력하세요. (ex. +82-10-1234-5678): +82-10-1234-5678
```
한가지 유의할점은 메시지를 보내고 싶은 전화번호는 iMessage에 메세지를 보낸 이력이 있어야합니다.
