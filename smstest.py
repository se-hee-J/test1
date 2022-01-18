import requests
import json

#요청 url
url = "https://api-sms.cloud.toast.com/sms/v3.0/appKeys/본인정보넣기/sender/sms"

headers = {
        'X-Secret-Key': '본인정보넣기',
        'Content-Type' : 'application/json;charset=UTF-8',
}

#필수 값
data = {
        'body': '안녕하세요.\n일반 발송 테스트용 메시지 입니다.감사합니다.',
        'sendNo': '01011112222',
        'RequestDate':'2022-01-15 00:00',
        'recipientList': [{
            'recipientNo' : '01011112222'
        }]
}

#데이터들 json 형식으로 바꿈
jsonData = json.dumps(data)
#통신 요청
response = requests.post(url,headers=headers,data=jsonData)

#응답 확인
print(response.status_code)

if response.json().get('resultcode') == 0:
    print('메시지 보내기 성공')
else:
    print('메시지 보내기 완료: '+ str(response.json()))