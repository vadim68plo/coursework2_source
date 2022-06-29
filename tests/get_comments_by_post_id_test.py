from utils.utils import get_comments_by_post_id
import pytest


def test_get_comments_by_post_id():
    with pytest.raises(ValueError):
        get_comments_by_post_id("1")

def test_get_comments_by_post_id_2():
    post = get_comments_by_post_id(1)
    assert type(post) == list, "Должен передаваться список"




