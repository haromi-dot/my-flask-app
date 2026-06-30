from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>🎉 ECR + ECS 핸즈온! (EC2 from)</h1>
    <p>이 앱은 EC2의 Docker 컨테이너에서 실행 중입니다!</p>
    <p>당신은 비전문가에서 DevOps 엔지니어로 변신 중 🚀</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)