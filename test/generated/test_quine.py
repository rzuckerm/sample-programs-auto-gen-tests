from glotter import project_test, project_fixture

PROJECT_NAME = "quine"


@project_fixture(PROJECT_NAME)
def quine(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
def test_quine(quine):
    actual = quine.run()
    with open(quine.full_path, "r", encoding="utf-8") as file:
        expected = file.read()
    actual = actual.strip()
    expected = expected.strip()
    assert actual == expected
