# 1단계: 기반 이미지
FROM python:3.11-slim

# 2단계: 작업 디렉토리
WORKDIR /app

# 3단계: requirements.txt 복사
COPY requirements.txt .

# 4단계: 의존성 설치
RUN pip install -r requirements.txt

# 5단계: 앱 코드 복사
COPY app.py .

# 6단계: 포트 열기
EXPOSE 5000

# 7단계: 앱 실행
CMD ["python", "app.py"]