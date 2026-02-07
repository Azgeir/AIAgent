from functions.get_files_info import get_files_info


def test(working_directory, directory):
    print("Result for current directory:")
    print(get_files_info(working_directory, directory))




if __name__ == "__main__":
    test("calculator", ".")
    test("calculator", "pkg")
    test("calculator", "/bin")
    test("calculator", "../")


