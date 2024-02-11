import pytest
from src.item import Item

item1 = Item("Samsung", 75000, 15)
item2 = Item("HTC", 15000, 10)

@pytest.fixture
def position():
    return Item("Смартфон",1000, 2)


def test_item_init(position):
    assert position.name == "Смартфон"
    assert position.price == 1000
    assert position.quantity == 2


def test_calculate_total_price(position):
    assert position.calculate_total_price() == 2000


def test_apply_discount(position):
    position.pay_rate = 0.8
    position.apply_discount()
    assert position.price == 800

def test_repr():
    assert repr(item1) == "Item('Samsung', 75000, 15)"
    assert repr(item2) == "Item('HTC', 15000, 10)"
def test_str():
    assert str(item1) == 'Samsung'
    assert str(item2) == "HTC"
