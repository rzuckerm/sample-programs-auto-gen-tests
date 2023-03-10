from glotter import project_test, project_fixture


@project_fixture("helloworld")
def hello_world(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("helloworld")
def test_hello_world(hello_world):
    actual = hello_world.run()
    expected = "Hello, World!"
    actual = actual.strip().strip('"')
    assert actual == expected
