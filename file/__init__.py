import os
import pathlib


class File:
    """
    파일에 대한 기능을 제공하는 클래스입니다.
    """
    __path: str

    def __init__(self, path: str):
        self.__path = path

    @property
    def path(self) -> str:
        """
        파일 경로를 반환합니다.
        :return (str): 파일 경로
        """
        return self.__path

    @property
    def extension(self) -> str:
        """
        파일 확장자명을 반환합니다.
        :return (str): 파일 확장자명
        """
        extensions = pathlib.Path(self.__path).suffixes
        extensions_len = len(extensions)

        if extensions_len == 0:
            return ""
        elif extensions_len == 1:
            return extensions[0][1:]
        else:
            ex = ""
            for extension in extensions:
                ex = ex + extension
            return ex[1:]

    @property
    def filename(self) -> str:
        """
        파일명을 반환합니다.
        :return (str): 파일명
        """
        return os.path.basename(self.__path)

    @property
    def is_exist(self) -> bool:
        """
        파일 혹은 디렉터리가 존재하는지 여부를 반환함.
        :return (bool): 파일 혹은 디렉터리 존재여부
        """
        return os.path.exists(self.__path)

    @property
    def is_directory(self) -> bool:
        """
        디렉터리인지 여부를 반환함.
        :return (bool): 디렉터리 여부
        """
        return os.path.isdir(self.__path)

    @property
    def is_file(self) -> bool:
        """
        파일인지 여부를 반환함.
        :return (bool): 파일 여부
        """
        return os.path.isfile(self.__path)

    @property
    def can_read(self) -> bool:
        """
        파일을 읽을 수 있는지 여부를 반환함.
        :return (bool): 파일 읽기 가능 여부
        """
        return os.access(self.__path, os.R_OK)

    @property
    def can_write(self) -> bool:
        """
        파일을 쓸 수 있는지 여부를 반환함.
        :return (bool): 파일 쓰기 가능 여부
        """
        return os.access(self.__path, os.W_OK)

    @property
    def can_execute(self) -> bool:
        """
        파일을 실행할 수 있는지 여부를 반환함.
        :return (bool): 파일 실행 가능 여부
        """
        return os.access(self.__path, os.X_OK)

    @property
    def size(self) -> int:
        """
        파일 크기를 반환함. (바이트 단위)
        :return (int): 파일 크기
        """
        return os.path.getsize(self.__path)

    def mkdir(self) -> None:
        """
        파일 경로에 디렉터리를 생성함.
        지정한 경로까지 재귀적으로 생성합니다.
        """
        os.makedirs(self.__path, exist_ok=True)
