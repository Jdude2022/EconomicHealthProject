from EconomicHealthProject.src.keys.Key import Key
from EconomicHealthProject.src.inidicator.utilities.Utilities import Utilities
from fredapi import Fred


class GrabnClean:
    """Gets data from the FRED API and formats for use in pandas."""
    @staticmethod
    def grab_series_json(self):
        """Grabs key from where the key is.
        TODO:
            args:
                category: series ID
                """

        key = Key()
        fred = Fred(api_key=f'{key.key}')
        gdp = fred.get_series('GDP')
        gdp = gdp.tail(1)
        unr = fred.get_series('UNRATE')
        unr = unr.tail(1)
        med = fred.get_series('MEHOINUSA646N')
        med = med.tail(1)
        return gdp[0], unr[0], med[0]


    @staticmethod
    def grab_series_states(self, state):
        key = Key()
        fred = Fred(api_key=f'{key.key}')
        abv = Utilities.state_to_abbreviation(state)
        gdp = fred.get_series(abv + 'NGSP')
        gdp = gdp.tail(1)
        unr = fred.get_series(abv + 'UR')
        unr = unr.tail(1)
        med = fred.get_series('MEHOINUS' + abv + 'A646N')
        med = med.tail(1)
        return gdp[0], unr[0], med[0]
