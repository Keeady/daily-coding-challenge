from Singleton import logging


def test_get_instance():
    instance = logging.logging()
    instance2 = logging.logging()

    assert instance == instance2
