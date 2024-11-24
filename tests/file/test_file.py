import os
import platform
import pytest

from file import File

class TestFile:
    __resource_abs_dir = os.path.join(
          # test_file.py가 존재하는 디렉터리 경로
          os.path.dirname(os.path.realpath(__file__))

          # 부모 디렉터리로 이동
        , os.pardir

          # resources 디렉터리로 이동
        , "resources"
    )
    __file1 = File(os.path.join(__resource_abs_dir + os.sep + "test.txt"))
    __file2 = File(__resource_abs_dir + os.sep + "test.tar.gz")
    __directory1 = File(__resource_abs_dir + os.sep + "test")

    def test_get_path(self):
        assert self.__file1.path == self.__resource_abs_dir + os.sep + "test.txt"
        assert self.__file2.path == self.__resource_abs_dir + os.sep + "test.tar.gz"
        assert self.__directory1.path == self.__resource_abs_dir + os.sep + "test"

    def test_get_extension(self):
        assert self.__file1.extension == "txt"
        assert self.__file2.extension == "tar.gz"
        assert self.__directory1.extension == ""

    def test_get_filename(self):
        assert self.__file1.filename == "test.txt"
        assert self.__file2.filename == "test.tar.gz"
        assert self.__directory1.filename == "test"

    def test_is_exist(self):
        assert True == self.__file1.is_exist
        assert True == self.__file2.is_exist
        assert True == self.__directory1.is_exist

    def test_is_directory(self):
        assert False == self.__file1.is_directory
        assert False == self.__file2.is_directory
        assert True == self.__directory1.is_directory

    def test_is_file(self):
        assert True == self.__file1.is_file
        assert True == self.__file2.is_file
        assert False == self.__directory1.is_file

    def test_can_read(self):
        assert True == self.__file1.can_read
        assert True == self.__file2.can_read
        assert True == self.__directory1.can_read

    def test_can_write(self):
        assert True == self.__file1.can_write
        assert True == self.__file2.can_write
        assert True == self.__directory1.can_write

    @pytest.mark.skipif(platform.uname().system == "Windows", reason="Windows에서는 실행 권한을 체크할 수 없습니다.")
    def test_can_execute(self):
        assert False == self.__file1.can_execute
        assert False == self.__file2.can_execute
        assert True == self.__directory1.can_execute

    def test_size(self):
        assert self.__file1.size == 23
        assert self.__file2.size == 380
        assert self.__directory1.size == 0 or self.__directory1.size == 96 or self.__directory1.size == 4096

    def test_mkdir_and_rm(self):
        f = File(os.path.join(self.__resource_abs_dir, "testdir/innerdir"))
        f.mkdir()

        directory = File(os.path.join(self.__resource_abs_dir, "testdir"))
        assert True == directory.is_exist

        inner_directory = File(os.path.join(self.__resource_abs_dir, "testdir/innerdir"))
        assert inner_directory.is_exist

        result = directory.rm()
        assert not result
        assert True == directory.is_exist

        inner_directory.rm()
        assert False == inner_directory.is_exist

        directory.rm()
        assert False == directory.is_exist
