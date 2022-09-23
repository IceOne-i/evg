import json
import os
import pathlib

script_dir = pathlib.Path(__file__).parent.resolve()

local_path = f"locales"
default_language = "ru"

languages = {

}


class Helper:
    def __init__(self):
        pass

    @staticmethod
    def count_directories(path: str) -> int:
        a = f'{path}'
        count = 0
        for x in os.listdir(a):
            if Helper.check_directory(f"{path}/{x}"):
                count += 1
        return count

    @staticmethod
    def directories(path: str) -> list:
        a = f'{path}'
        directories = []
        for x in os.listdir(a):
            if Helper.check_directory(f"{path}/{x}"):
                directories.append(x)
        return directories

    @staticmethod
    def count_files(path: str, type: str = None) -> int:
        a = f'{path}'
        count = 0
        for x in os.listdir(a):
            if Helper.check_file(f"{path}/{x}"):
                if type is not None:
                    if not x.endswith(type):
                        continue
                count += 1
        return count

    @staticmethod
    def files(path: str, type: str = None) -> list:
        a = f'{path}'
        files = []
        for x in os.listdir(a):
            if Helper.check_file(f"{path}/{x}"):
                if type is not None:
                    if not x.endswith(type):
                        continue
                files.append(x)
        return files

    @staticmethod
    def check_directory(path: str) -> bool:
        a = f'{path}'
        return os.path.isdir(a)

    @staticmethod
    def check_file(path: str) -> bool:
        a = f'{path}'
        return os.path.isfile(a)


class Setup:
    def __init__(self):
        pass

    @staticmethod
    def localedir(localedir: str) -> str:
        local_path = localedir
        return local_path

    @staticmethod
    def language(language: str) -> str:
        default_language = language
        return default_language


class MSG:
    def __init__(self, language: str):
        self.language = language
        if self.language not in languages:
            self.language = default_language

    def msg(self, msg: str) -> str:
        language: dict = languages[self.language]
        try:
            return language[msg]
        except Exception as e:
            raise "Необнаружено языкового ключа!"
