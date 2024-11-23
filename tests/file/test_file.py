import os

from file import File

class TestFile:
    __file1 = File(os.path.join(".." + os.sep + "resources" + os.sep + "test.txt"))
    __file2 = File(".." + os.sep + "resources" + os.sep + "test.tar.gz")
    __directory1 = File(".." + os.sep + "resources" + os.sep + "test")

    def test_get_path(self):
        assert self.__file1.path == ".." + os.sep + "resources" + os.sep + "test.txt"
        assert self.__file2.path == ".." + os.sep + "resources" + os.sep + "test.tar.gz"
        assert self.__directory1.path == ".." + os.sep + "resources" + os.sep + "test"

    def test_get_extension(self):
        assert self.__file1.extension == "txt"
        assert self.__file2.extension == "tar.gz"
        assert self.__directory1.extension == ""

    def test_get_filename(self):
        assert self.__file1.filename == "test.txt"
        assert self.__file2.filename == "test.tar.gz"
        assert self.__directory1.filename == "test"

    def test_is_exist(self):
        assert True == os.path.exists("/Users/retrotv/Desktop/git/python/file/tests/resources/test.txt")
    #     assert True == self.__file1.is_exist
    #     assert True == self.__file2.is_exist
    #     assert True == self.__directory1.is_exist
    #
    # def test_is_directory(self):
    #     assert False == self.__file1.is_directory
    #     assert False == self.__file2.is_directory
    #     assert True == self.__directory1.is_directory
    #
    # def test_is_file(self):
    #     assert True == self.__file1.is_file
    #     assert True == self.__file2.is_file
    #     assert False == self.__directory1.is_file
    #
    # def test_can_read(self):
    #     assert True == self.__file1.can_read
    #     assert True == self.__file2.can_read
    #     assert True == self.__directory1.can_read
    #
    # def test_can_write(self):
    #     assert True == self.__file1.can_write
    #     assert True == self.__file2.can_write
    #     assert True == self.__directory1.can_write
    #
    # def test_can_execute(self):
    #     assert False == self.__file1.can_execute
    #     assert False == self.__file2.can_execute
    #     assert True == self.__directory1.can_execute
    #
    # def test_size(self):
    #     assert self.__file1.size == 23
    #     assert self.__file2.size == 380
    #     assert self.__directory1.size != 0
    #
    # def test_mkdir(self):
    #     f = File("../resources/testdir/innerdir")
    #     f.mkdir()
    #
    #     directory = File("../resources/testdir")
    #     assert True == directory.is_exist
    #
    #     inner_direcotry = File("../resources/testdir/innerdir")
    #     assert inner_direcotry.is_exist
