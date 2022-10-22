import myproject.scripts
import myproject.scripts.calculations


def test_myfunction():
    res = myproject.scripts.calculations.myfunction()
    assert res == "blue"
