from flask import Flask
from typing import List
from EconomicsHealthProject.src.web.WebRoutes import WebRoutes


class Web:
    @staticmethod
    def main(args: List[str]):
        """main method"""
        app = Flask(__name__)
        WebRoutes.register(app)
        return app
        # return app.run(host='0.0.0.0', port=5050)
