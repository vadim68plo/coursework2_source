from utils.utils import get_post_by_pk
import pytest


def test_get_post_by_pk():
    post = get_post_by_pk(222)
    assert post == [], "Неверное значение"


def test_get_post_by_pk_2():
    post = get_post_by_pk(1)
    assert type(post) == list, "Должен передаваться список"


