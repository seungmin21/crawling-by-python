import requests
from bs4 import BeautifulSoup
import csv

# 검색어와 URL 설정
search_query = 'python web scraping'  # 검색할 키워드
google_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"

# 헤더 설정 (구글은 자동화된 요청을 차단할 수 있기 때문에 브라우저 유저 에이전트처럼 보이게 설정)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

# 구글 검색 페이지 요청
response = requests.get(google_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 검색 결과 추출
results = soup.find_all('div', class_='tF2Cxc')  # 구글 검색 결과는 'tF2Cxc' 클래스에 포함됨

# CSV 파일에 저장할 리스트 생성
data = []

# 검색 결과에서 링크와 제목을 추출하여 리스트에 저장
for result in results:
    title = result.find('h3').text  # 제목
    link = result.find('a')['href']  # 링크
    data.append([title, link])

# CSV 파일로 저장
with open('google_search_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])  # 헤더 작성
    writer.writerows(data)  # 데이터 작성

print("크롤링 완료, 데이터가 CSV 파일에 저장되었습니다.")
