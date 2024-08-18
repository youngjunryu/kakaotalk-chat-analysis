# 소개 
카카오톡 채팅방 대화 내용 CSV 파일을 분석하여 사용자 메시지 비율과 가장 자주 언급된 단어를 계산합니다.

# 사용법
1. To get started, clone the repository and install the required libraries.
```angular2html
$ git clone https://github.com/youngjunryu/kakaotalk-chat-analysis.git
$ pip install -r requirements.txt
```

2. Set the CSV file path in the main.py
```angular2html
file_path = 'path/to/your/chat_data.csv'
```

3. Run the script
```angular2html
$ python main.py
```

# 기능
* 사용자 메시지 비율 계산 
  * 각 사용자가 전체 메시지에서 차지하는 비율을 계산하고, 이를 백분율 형식으로 출력합니다. 
* 가장 자주 언급된 단어 식별 
   * 대화 내용을 하나의 텍스트로 결합한 후, 텍스트를 토큰화하고 비알파벳 문자를 제거하여 단어의 빈도수를 계산합니다.
   * 가장 빈도수가 높은 상위 50개 단어와 그 비율을 출력합니다.
