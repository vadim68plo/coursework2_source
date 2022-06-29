from utils.utils import get_posts_by_user
import pytest


def test_get_posts_by_user():
    with pytest.raises(ValueError):
        get_posts_by_user("Tom")

def test_get_posts_by_user_2():
    post = get_posts_by_user("leo")
    assert type(post) == list, "Должен передаваться список"

