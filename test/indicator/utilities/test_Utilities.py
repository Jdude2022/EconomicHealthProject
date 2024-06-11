from src.inidicator import Utilities

class TestUtilities:

    def test_state_conversion(self):
        states = ["Alabama", "Kentucky", "Ohio"]
        abv = ["AL", "KY", "OH"]
        for i in range(len(states)):
            test_var = Utilities.state_to_abbreviation(states[i])
            assert test_var == abv[i]
