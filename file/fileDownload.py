from flask import Flask, request as rq, send_file

# 打开选择文件夹对话框

app = Flask(__name__)


# 接口测试
@app.route('/py/fileDownload', methods=['POST'])
def hello_world():
    print(1)
    filePath = rq.form.get('fileDownLoadPath')
    print(2)
    return send_file(filePath)


if __name__ == '__main__':
    print("fileDownload")
    app.run(host="127.0.0.1", port=5005)
