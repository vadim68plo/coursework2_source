import json


def get_posts_all():

    '''Возвращает список всех постов'''

    path = "../data/data.json"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_comments_all():

    '''Возвращает список всех постов'''

    path = "../data/comments.json"

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_posts_by_user(user_name):

    '''Возвращает список постов по имени пользовтаеля'''

    posts = get_posts_all()
    posts_user = []

    for post in posts:
        if user_name in post["poster_name"]:
            posts_user.append(post)

    if len(posts_user) == 0:
        raise ValueError("Пользователь не найден")
    else:
        return posts_user


def get_comments_by_post_id(post_id:int):

    '''Возвращает список комментариев по имени id'''

    posts = get_comments_all()
    posts_id = []


    for post in posts:
        if post_id == post["post_id"]:
            posts_id.append(post)

    if len(posts_id) == 0:
        raise ValueError("Пост не найден")

    return posts_id


def search_post(post_in):

    '''Возвращает список всех постов по введеному слову'''

    posts = get_posts_all()
    _search_post = []
    for post in posts:
        if post_in.lower() in post["content"].lower():
            _search_post.append(post)

    return _search_post


def get_post_by_pk(pk:int):

    '''Возвращает список пост по индефикатору'''

    posts = get_posts_all()
    _search_post = []
    for post in posts:
        if pk == post["pk"]:
            _search_post.append(post)

    return _search_post



