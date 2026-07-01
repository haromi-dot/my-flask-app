from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>🎉 자동 배포 테스트!! </h1>
    <p>🚀 이 앱은 EC2의 Docker 컨테이너에서 실행 중입니다!🚀 </p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)