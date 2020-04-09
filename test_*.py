from gallows_main import Game
import pytest
import coverage


def test_find_index(components):
    (string, letter, expected_output) = components
    result = Game.find_indexes(string, letter)
    assert result == list(expected_output)


@pytest.mark.xfail
def test_not_find_index(fail_components):
    assert Game.find_indexes(*fail_components)


@pytest.mark.parametrize('x', ['q', 's', 'b', 'm', 't'])
def test_foo(x, foo_components):
    if (foo_components.foo(x) == 'Вы победили') or \
            (foo_components.foo('q') == 'Буква угадана'):
        assert True
    elif foo_components.foo(x) == 'Такой буквы нет!':
        assert False


@pytest.mark.parametrize('x', ['e', 'q'])
def test_end_of_game(x, foo_components):
    foo_components.word = 't _ s t i n g'
    foo_components.current_word = 'testing'
    foo_components.possible_points = 1
    if foo_components.foo(x) == 'Вы победили':
        assert True
    elif foo_components.foo(x) == 'Вы проиграли':
        assert False
