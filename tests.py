
def run_tests(func, result):
    with open("test_data.txt") as f:
        test_data = f.read()
        func_result = func(test_data)
        assert func_result == result
