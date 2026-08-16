from app import create_app


def test_create_app_bootstraps_without_sqlalchemy_registry_errors():
    app = create_app()
    assert app is not None
    assert app.name == "app"
