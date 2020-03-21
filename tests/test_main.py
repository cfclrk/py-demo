import py_demo


def test_version():
    v = py_demo.__version__
    assert type(v) == str
