import pytest
from app import app


@pytest.fixture()
def test_client():
    app_ = app.app
    return app_.test_client()

class TestMain:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус-код всех постов неверный"


