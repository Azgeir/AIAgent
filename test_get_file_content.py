from functions.get_file_content import get_file_content


def test(working_directory, file_path):
    print("Result for current file:")
    f = get_file_content(working_directory, file_path)
    print(f)




if __name__ == "__main__":
    test("calculator", "main.py")
    test("calculator", "pkg/calculator.py")
    test("calculator", "/bin/cat")
    test("calculator", "pkg/does_not_exist.py")