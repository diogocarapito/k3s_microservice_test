from app.app import app


def test_home_page():
    component = app()
    assert component is not None
