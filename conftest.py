import pytest
from gallows_main import Game


@pytest.fixture(scope='function', params=[('abracadabra', 'a',
                                           (0, 3, 5, 7, 10)), ('abc', 'c',
                                                               (2,))])
def components(request):
    return request.param


@pytest.fixture()
def fail_components():
    return 'abc', 'q'


@pytest.fixture()
def foo_components():
    return Game()
