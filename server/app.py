import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    # app.run(debug=True, threaded=True) threaded位设置可能IE卡死bug
    app.run(debug=True)
