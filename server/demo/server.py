# https://www.cnblogs.com/cleven/p/10858016.html
from flask import Flask, request, Response, jsonify, url_for, \
    redirect, abort, render_template_string, session, \
    render_template, make_response
import json
from werkzeug.utils import secure_filename
from werkzeug.routing import BaseConverter
import os


class MyIntConverter(BaseConverter):
    def __init__(self, url_map):
        super(MyIntConverter, self).__init__(url_map)

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return value * 2


app = Flask(__name__)
app.url_map.converters['my_int'] = MyIntConverter

# session加密
app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'

# 文件上传目录
app.config['UPLOAD_FOLDER'] = 'static/uploads'
# 支持的文件格式
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


# 判断文件名是否支持的格式
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def hello_world():
    # r = request.args.get('info', 'hi')
    r = request.args.getlist('info')
    return str(r)


@app.route('/register', methods=['POST'])
def register():
    # print(request.headers)
    # print(request.stream.read())
    # data = request.form
    # print(data)
    # print(data['name'])
    # print(data.get('name'))
    # print(data.getlist('name'))
    print(request.json)
    result = {'n': request.json['name'], 'p': request.json['password']}
    # return Response(json.dumps(result), mimetype='application/json')
    return jsonify(result)


@app.route('/upload', methods=['POST'])
def upload():
    upload_file = request.files['image']
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        # 文件保存到static/uploads 目录，文件名同上传时使用的文件名
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'success'
    else:
        return 'failed'


# @app.route('/user/<uid>')
# @app.route('/user/<int:uid>')
@app.route('/user/<my_int:uid>')
def user(uid):
    abort(401)
    print(uid)
    print(type(uid))
    print(url_for('hello_world'))
    # print(url_for('user', name='letian'))
    # print(url_for('page', num=1, q='hadoop mapreduce 10%3'))
    # print(url_for('static', filename='uploads/01.jpg'))
    # return str(uid)
    return redirect(url_for('hello_world'))


@app.errorhandler(401)
def page_unauthorized(error):
    # resp = make_response(render_template('error.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    return render_template_string('<h1>401 {{error_info}}</h1>', error_info=error), 401


@app.route('/login')
def login():
    page = '''
    <form action="{{ url_for('do_login') }}" method="post">
        <p>name: <input type="text" name="user_name" /></p>
        <input type="submit" value="Submit" />
    </form>
    '''
    return render_template_string(page)


@app.route('/do_login', methods=['POST'])
def do_login():
    name = request.form.get('user_name')
    session['user_name'] = name
    return 'success'


@app.route('/show')
def show():
    return session['user_name']


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))


@app.route('/cart', methods=['GET', 'POST'])
@app.route('/cart/<name>', methods=['GET'])
def cart(name=None):
    if request.method == 'POST':
        return 'post cart'
    else:
        return render_template('cart.html', name=name)


@app.route('/mcookies')
def mcookies():
    username = request.cookies.get('username')
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp


@app.route('/mredirect')
def mredirect():
    # 使用 redirect() 函数可以重定向。使用 abort() 可以 更早退出请求，并返回错误代码:
    return redirect(url_for('login'))
    # abort(401)
    # this_is_never_executed()


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=80, debug=True)
