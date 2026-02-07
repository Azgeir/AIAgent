from functions.write_file import write_file


def test(working_directory, file_path):
    #print("Result for current file:")
    f = write_file(working_directory, file_path)
    print(f)




if __name__ == "__main__":
    test("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    test("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    test("calculator", "/tmp/temp.txt", "this should not be allowed")