from glotter import project_test, project_fixture


@project_fixture("quine")
def quine(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("quine")
def test_quine(quine):
    actual = quine.run()
    with open(quine.full_path, "r", encoding="utf-8") as file:
        expected = file.read()
    actual = actual.strip()
    expected = expected.strip()
    assert actual == expected
