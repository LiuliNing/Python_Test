# 导入Flask类
import json

from flask import Flask, request as rq
import Student
# 实例化，可视为固定格式
app = Flask(__name__)


# 接口测试
@app.route('/py/jsonTest', methods=['GET'])
def hello_world():
    print("form:", rq.form)
    print("data:", rq.data)
    print("values:", rq.values)
    print("args:", rq.args)
    print("json:", rq.json)
    data = json.loads(rq.data)
    Student.Student.__repr__(data)
    return rq.json


def obj2dict(obj):
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def dict2obj(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        instance = class_(**args)
    else:
        instance = d
    return instance


# 启动web应用，端口为5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
