import requests
import json

def save_image(image_url, file_name):
  img_response = requests.get(image_url)

  if (img_response.status_code == 200):
    with open(file_name, "wb") as fp:
      fp.write(img_response.content)

url = "https://dapi.kakao.com/v2/search/image"

headers = {
  "Authorization": "KakaoAK f52244653be28de0d611c44101b063dd"
}

data = {
  "query": "펭수" #검색하고 싶은 단어로 바꿔주세요~ 디폴드 값은 펭수입니다 
}

response = requests.post(url, headers=headers, data=data)

if response.status_code != 200:
  print("error! because ", response.json())
else:
  count = 0
  for image_info in response.json()['documents']:
    print(f"[{count}th] image_url =", image_info['image_url'])
    count = count + 1
    file_name = "test_%d.jpg" % count
    save_image(image_info['image_url'], file_name)
    if count >= 5:  #저장하고 싶은 이미지 수로 바꿔주세요~ 디폴드 값은 5개입니다
      break
