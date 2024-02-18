from src.keyboard import Keyboard


kb = Keyboard("Dark Project KD87A", 9600, 5)
assert str(kb) == "Dark Project KD87A"


def test_language():
    """Проверяет изначальную раскладку клавиатуры"""
    assert str(kb.language) == "EN"


def test_change_lang():
    """Проверяет смену языка"""
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
