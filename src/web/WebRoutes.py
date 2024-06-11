from flask import render_template
from flask_classful import FlaskView, route
from src.inidicator import GrabnClean
from src.inidicator import Utilities
import os  # worried about cors/ file error


class WebRoutes(FlaskView):
    route_base = '/'
    @route('/')
    def home(self):
        """Home Page."""
        # TODO ADD ALASKA and HI TO THE HOME SCREEN
        state_date = GrabnClean().grab_series_json(self)
        return render_template("index.html", unit='B', gdp=state_date[0], unr=state_date[1], med=state_date[2])

    @route('/statesData.json')
    def data(self):
        """Data Page."""
        return render_template("statesData.json")

    @route('/states/<state>')
    def state(self, state):
        """Grabs the state once clicked, and renders it."""
        #TODO If state not in Util dict, 404.
        state_abv = Utilities.state_to_abbreviation(state)
        img = os.path.join('../', 'static', 'images', state_abv + '.png')

        state_info = GrabnClean().grab_series_states(self, state)
        return render_template("state_view.html", state_name=state, state_img=img, unit='M',
                               gdp=state_info[0], unr=state_info[1], med=state_info[2])
