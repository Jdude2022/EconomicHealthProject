# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()

import sys
from EconomicHealthProject.src.web.Web import Web

app = Web.main(sys.argv)
# app.run()
if __name__ == '__main__':
     app.run()