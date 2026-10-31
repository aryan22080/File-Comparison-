import filecmp

if __name__ == "__main__":
    file1 = "test1.txt"
    file2 = "test2.txt"

    # Compare the two files
    result = filecmp.cmp(file1, file2)
    if result ==True:
        print("Both are identical with same content")
    else:
        print("Files are different")