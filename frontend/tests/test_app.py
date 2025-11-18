from app.app import main


def test_home_page():
    component = main()
    assert component is not None
