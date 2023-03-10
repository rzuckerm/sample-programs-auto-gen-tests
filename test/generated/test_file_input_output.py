from glotter import project_test, project_fixture


@project_fixture("fileinputoutput")
def file_input_output(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test("fileinputoutput")
def test_file_io(file_input_output):
    actual = file_input_output.run()
    expected = file_input_output.exec("cat output.txt")
    actual = actual.strip()
    expected = expected.strip()
    assert actual == expected
