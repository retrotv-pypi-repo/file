import unittest
import logging

from file import File


class FileTests(unittest.TestCase):
    __log = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        # encoding="UTF-8",
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S'
    )
    __file1 = File("../resources/test.txt")
    __file2 = File("../resources/test.tar.gz")
    __directory1 = File("../resources/test")

    def test_get_path(self):
        self.__log.info("파일 경로: %s", self.__file1.path)
        self.assertEqual(self.__file1.path, "../resources/test.txt")

        self.__log.info("파일 경로: %s", self.__file2.path)
        self.assertEqual(self.__file2.path, "../resources/test.tar.gz")

        self.__log.info("파일 경로: %s", self.__directory1.path)
        self.assertEqual(self.__directory1.path, "../resources/test")

    def test_get_extension(self):
        self.__log.info("파일 확장자명: %s", self.__file1.extension)
        self.assertEqual(self.__file1.extension, "txt")

        self.__log.info("파일 확장자명: %s", self.__file2.extension)
        self.assertEqual(self.__file2.extension, "tar.gz")

    def test_get_filename(self):
        self.__log.info("파일명: %s", self.__file1.filename)
        self.assertEqual(self.__file1.filename, "test.txt")

        self.__log.info("파일명: %s", self.__file2.filename)
        self.assertEqual(self.__file2.filename, "test.tar.gz")

    def test_is_exist(self):
        self.__log.info("파일 존재여부: %s", self.__file1.is_exist)
        self.assertTrue(self.__file1.is_exist)

        self.__log.info("파일 존재여부: %s", self.__file2.is_exist)
        self.assertTrue(self.__file2.is_exist)

        self.__log.info("디렉터리 존재여부: %s", self.__directory1.is_exist)
        self.assertTrue(self.__directory1.is_exist)

    def test_is_directory(self):
        self.__log.info("디렉터리 여부: %s", self.__file1.is_directory)
        self.assertFalse(self.__file1.is_directory)

        self.__log.info("디렉터리 여부: %s", self.__file2.is_directory)
        self.assertFalse(self.__file2.is_directory)

        self.__log.info("디렉터리 여부: %s", self.__directory1.is_directory)
        self.assertTrue(self.__directory1.is_directory)

    def test_is_file(self):
        self.__log.info("파일 여부: %s", self.__file1.is_file)
        self.assertTrue(self.__file1.is_file)

        self.__log.info("파일 여부: %s", self.__file2.is_file)
        self.assertTrue(self.__file2.is_file)

        self.__log.info("파일 여부: %s", self.__directory1.is_file)
        self.assertFalse(self.__directory1.is_file)

    def test_can_read(self):
        self.__log.info("파일 읽기 가능 여부: %s", self.__file1.can_read)
        self.assertTrue(self.__file1.can_read)

        self.__log.info("파일 읽기 가능 여부: %s", self.__file2.can_read)
        self.assertTrue(self.__file2.can_read)

        self.__log.info("디렉터리 읽기 가능 여부: %s", self.__directory1.can_read)
        self.assertTrue(self.__directory1.can_read)

    def test_can_write(self):
        self.__log.info("파일 쓰기 가능 여부: %s", self.__file1.can_write)
        self.assertTrue(self.__file1.can_write)

        self.__log.info("파일 쓰기 가능 여부: %s", self.__file2.can_write)
        self.assertTrue(self.__file2.can_write)

        self.__log.info("디렉터리 쓰기 가능 여부: %s", self.__directory1.can_write)
        self.assertTrue(self.__directory1.can_write)

    def test_can_execute(self):
        self.__log.info("파일 실행 가능 여부: %s", self.__file1.can_execute)
        self.assertFalse(self.__file1.can_execute)

        self.__log.info("파일 실행 가능 여부: %s", self.__file2.can_execute)
        self.assertFalse(self.__file2.can_execute)

        self.__log.info("디렉터리 실행 가능 여부: %s", self.__directory1.can_execute)
        self.assertTrue(self.__directory1.can_execute)

    def test_size(self):
        self.__log.info("파일 크기: %s", self.__file1.size)
        self.assertEqual(self.__file1.size, 23)

        self.__log.info("파일 크기: %s", self.__file2.size)
        self.assertEqual(self.__file2.size, 380)

        self.__log.info("디렉터리 크기: %s", self.__directory1.size)
        self.assertNotEqual(self.__directory1.size, 0)

    def test_mkdir(self):
        f = File("../resources/testdir/innerdir")
        f.mkdir()

        directory = File("../resources/testdir")
        self.assertTrue(directory.is_exist)

        inner_direcotry = File("../resources/testdir/innerdir")
        self.assertTrue(inner_direcotry.is_exist)

if __name__ == '__main__':
    unittest.main()
