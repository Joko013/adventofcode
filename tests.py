
def run_tests(func, result):
    with open("test_data") as f:
        test_data = f.read()
        assert func(test_data) == result
