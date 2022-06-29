from utils.utils import search_post
import pytest


def test_search_post():
    post = search_post("Графика")
    assert post == [], "Неверное значение"


def test_search_post_2():
    post = search_post("на")
    assert type(post) == list, "Должен передаваться список"