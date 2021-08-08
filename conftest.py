import pytest
from fixture.application import Application


@pytest.fixture()
def app():
    application = Application()
    return application
