from flask import Flask, render_template
from typing import List
from datetime import timedelta
from EconomicHealthProject.src.web.WebRoutes import WebRoutes


class Web:
    @staticmethod
    def main(args: List[str]):
        """main method"""
        app = Flask(__name__)
        app.secret_key = "secret key"
        app.permanent_session_lifetime = timedelta(minutes=30)
        WebRoutes.register(app)
        # app.register_error_handler(404, Web.page_not_found)
        return app
        # return app.run(host='0.0.0.0', port=5050)

    @staticmethod
    def page_not_found(e):
        return render_template('404.html'), 404

