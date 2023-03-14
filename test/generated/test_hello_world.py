from glotter import project_test, project_fixture

PROJECT_NAME = "helloworld"


@project_fixture(PROJECT_NAME)
def hello_world(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
def test_hello_world(hello_world):
    actual = hello_world.run()
    expected = "Hello, World!"
    actual = actual.strip().strip('"')
    assert actual == expected
