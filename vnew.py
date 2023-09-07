from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

def random_function():
    # JSON 요청 데이터 가져오기
    request_data = request.get_json()

    # "classnum" 키가 있는지 확인하고 값을 가져오기
    classnum = request_data.get("classnum")

    # "classnum"이 없거나 숫자가 아니면 오류 응답을 반환
    if classnum is None or not isinstance(classnum, (int, float)):
        return jsonify({"error": "Invalid input"}), 400

    # classnum 값을 7배로 곱한 후 응답으로 반환
    result = classnum * 7
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": str(result)
                    }
                }
            ]
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()