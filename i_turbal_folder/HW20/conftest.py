import pytest
import application

@pytest.fixture(autouse=True)
def app():
    yield application.DesignCalculator()

@pytest.fixture(scope='class',autouse=True)
def class_scope():
    print('\n Class starts')
    yield
    print('\n Class ends')

@pytest.fixture(scope='module')
def module_scope():
    print('\nmodule starts')
    yield
    print('\n module ends')

@pytest.fixture(scope='session')
def session_scope():
    print('\n session starts')
    yield
    print('\n session ends')



