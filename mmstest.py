#장문 MMS 발송 (첨부파일 미 포함)

import requests
import json

#요청 url
url = "https://api-sms.cloud.toast.com/sms/v3.0/appKeys/본인정보넣기/sender/mms"

headers = {
        'X-Secret-Key': '본인정보넣기',
        'Content-Type' : 'application/json;charset=UTF-8',
}

#필수 값
data = {
        'title': '장문 발송 메시지',
        'body': '안녕하세요.\n장문 발송 테스트용 메시지 입니다.',
        'sendNo': '01011112222',
        'recipientList': [{
            'recipientNo' : '01011112222'
        }]
}

#데이터들 json 문자열로 바꿈
jsonData = json.dumps(data)
#통신 요청
response = requests.post(url,headers=headers,data=jsonData)

#응답 확인
print(response.status_code)

if response.json().get('resultcode') == 0:
    print('메시지 보내기 성공')
else:
    print('메시지 보내기 완료: '+ str(response.json()))