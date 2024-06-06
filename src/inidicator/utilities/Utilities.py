

class Utilities:
    state_abbreviations = {"Alabama": "AL", "Kentucky": "KY", "Ohio": "OH",
                           "Alaska": "AK", "Louisiana": "LA", "Oklahoma": "OK",
                           "Arizona": "AZ", "Maine": "ME", "Oregon": "OR",
                           "Arkansas": "AR", "Maryland": "MD", "Pennsylvania": "PA",
                           "AmericanSamoa": "AS", "Massachusetts": "MA", "PuertoRico": "PR",
                           "California": "CA", "Michigan": "MI", "RhodeIsland": "RI",
                           "Colorado": "CO", "Minnesota": "MN", "SouthCarolina": "SC",
                           "Connecticut": "CT", "Mississippi": "MS", "SouthDakota": "SD",
                           "Delaware": "DE", "Missouri": "MO", "Tennessee": 'TN',
                           "DistrictofColumbia": "DC", "Montana": "MT", "Texas": "TX",
                           "Florida": "FL", "Nebraska": "NE", "TrustTerritories": "TT",
                           "Georgia": "GA", "Nevada": "NV", "Utah": "UT",
                           "Guam": "GU", "NewHampshire": "NH", "Vermont": "VT",
                           "Hawaii": "HI", "NewJersey": "NJ", "Virginia": "VA",
                           "Idaho": "ID", "NewMexico": "NM", "VirginIslands": "VI",
                           "Illinois": "IL", "NewYork": "NY", "Washington": "WA",
                           "Indiana": "IN", "NorthCarolina": "NC", "WestVirginia": "WV",
                           "Iowa": "IA", "NorthDakota": "ND", "Wisconsin": "WI",
                           "Kansas": "KS", "NorthernMarianaIslands": "MP", "Wyoming": "WY"}

    @staticmethod
    def state_to_abbreviation(state: str):
        """Method to convert a full state name to abbreviation.

        :param state: State name
        :return: State abbreviation from the dictionary above
        """
        print(state)
        # Throw an error if State with space makes it in.
        return Utilities.state_abbreviations.get(state)
