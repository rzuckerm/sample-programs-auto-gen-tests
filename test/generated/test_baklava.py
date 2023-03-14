from glotter import project_test, project_fixture

PROJECT_NAME = "baklava"


@project_fixture(PROJECT_NAME)
def baklava(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(PROJECT_NAME)
def test_baklava(baklava):
    actual = baklava.run()
    expected = [
        "          *",
        "         ***",
        "        *****",
        "       *******",
        "      *********",
        "     ***********",
        "    *************",
        "   ***************",
        "  *****************",
        " *******************",
        "*********************",
        " *******************",
        "  *****************",
        "   ***************",
        "    *************",
        "     ***********",
        "      *********",
        "       *******",
        "        *****",
        "         ***",
        "          *",
    ]
    actual_list = actual.splitlines()
    expected_list = expected
    assert len(actual_list) == len(expected_list), "Length not equal"
    for index in range(len(expected_list)):
        assert (
            actual_list[index] == expected_list[index]
        ), f"Item {index + 1} is not equal"
