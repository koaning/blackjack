import pytest 

from blackjack.common import card_score

@pytest.mark.parametrize("cards,score", [('JK', 20), ('KKK', 0), ('AA', 12), ('AK', 21)])
def test_simple_usecase(cards, score):
    assert card_score(cards) == score

@pytest.mark.parametrize("cards", ["", 1])
def test_raise_error(cards):
    with pytest.raises(ValueError):
        card_score(cards)

def test_will_fail():
    assert False
