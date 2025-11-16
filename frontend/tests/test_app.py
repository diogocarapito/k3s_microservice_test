from app.app import home


def test_home_page():
    component = home()
    assert component is not None
