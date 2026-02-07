from functions.run_python_file import run_python_file


def test(working_directory, file_path, args=None):
    #print("Result for current file:")
    f = run_python_file(working_directory, file_path, args)
    print(f)




if __name__ == "__main__":
    test("calculator", "main.py")
    test("calculator", "main.py", ["3 + 5"])
    test("calculator", "tests.py")
    test("calculator", "../main.py")
    test("calculator", "nonexistent.py")
    test("calculator", "lorem.txt")