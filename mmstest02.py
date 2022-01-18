#장문 MMS 발송 (첨부파일 포함)

import requests
import json

#요청 url
url = "https://api-sms.cloud.toast.com/sms/v3.0/appKeys/본인정보넣기/sender/mms"

headers = {
        'X-Secret-Key': '본인정보넣기',
        'Content-Type' : 'application/json;charset=UTF-8',
}

#파일 첨부 위한 fileBody 값은 파일 byte[]를 Base64로 인코딩 해야함
#import base64

#sitename = 'Man'
#sitename_bytes = sitename .encode('ascii')
#sitename_base64 = base64.b64encode(sitename_bytes)
#sitename_base64_str = sitename_base64.decode('ascii')
#print(sitename_base64_str) ->출력 시 'Man'이'TWFu'으로 변경됨을 확인

#필수 값
data = {
        'title': '반갑습니다',
        'body': '안녕하세요.\n장문 발송 테스트용 메시지 입니다.',
        'sendNo': '01011112222',
        'fileName': 'Man.jpg',
        'createUser': 'Authenticated User',
        'fileBody': 'TWFu', #Base64로 인코딩한 값
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