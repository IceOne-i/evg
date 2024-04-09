import os
import pathlib

_script_dir = pathlib.Path(__file__).parent.resolve()
default_language = "en-US"

languages = {}

default_text = "oOps"


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
    def directories(path: str) -> list[str]:
        a = f'{path}'
        directories = []
        for x in os.listdir(a):
            if Helper.check_directory(f"{path}/{x}"):
                directories.append(x)
        return directories

    @staticmethod
    def count_files(path: str, file_type: str = None) -> int:
        a = f'{path}'
        count = 0
        for x in os.listdir(a):
            if Helper.check_file(f"{path}/{x}"):
                if file_type is not None:
                    if not x.endswith(file_type):
                        continue
                count += 1
        return count

    @staticmethod
    def files(path: str, file_type: str = None) -> list[str]:
        a = f'{path}'
        files = []
        for x in os.listdir(a):
            if Helper.check_file(f"{path}/{x}"):
                if file_type is not None:
                    if not x.endswith(file_type):
                        continue
                files.append(x)
        return files

    @staticmethod
    def check_directory(path: str) -> bool:
        a = f'{path}'
        return os.path.isdir(a)

    @staticmethod
    def check_file(path: str, file_type: str = None) -> bool:
        a = f'{path}'
        if file_type is not None:
            if not path.endswith(file_type):
                return False
        return os.path.isfile(a)

    @staticmethod
    def check_language(language: str) -> bool:
        if language in languages:
            return True
        return False

    @staticmethod
    def check_word(language: str, word: str) -> bool:
        if Helper.check_language(language):
            if word in languages[language]:
                return True
        return False


class Setup:
    def __init__(self):
        pass

    @staticmethod
    def language(language: str) -> str:
        global default_language
        default_language = language
        return default_language

    @staticmethod
    def text(text: str) -> str:
        global default_text
        default_text = text
        return default_text


class MSG:
    def __init__(self, language: str):
        self.language = language
        if self.language not in languages:
            global default_language
            self.language = default_language

    def msg(self, msg: str, default: str = None, *args, **kwargs):
        language: dict = languages[self.language]
        answer = language.get(msg)
        if answer is None:
            if default is not None:
                return default
            else:
                return languages[default_language].get(msg, default_text)
        else:
            return answer.format(*args, **kwargs)
