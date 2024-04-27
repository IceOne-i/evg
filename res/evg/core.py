import os
import pathlib
from random import choice
from typing import Union

_script_dir = pathlib.Path(__file__).parent.resolve()
default_language = "en-US"

languages = {}

default_text = "oOps"
default_file_types = ["json"]


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
    def count_files(path: str, file_types: Union[str, list[str], None] = None) -> int:
        count = 0
        for x in os.listdir(path):
            if Helper.check_file(f"{path}/{x}", file_types=file_types) is True:
                count += 1
        return count

    @staticmethod
    def files(path: str, file_types: Union[str, list[str], None] = None) -> list[str]:
        files = []
        for x in os.listdir(path):
            if Helper.check_file(f"{path}/{x}", file_types=file_types) is True:
                files.append(x)
        return files

    @staticmethod
    def check_directory(path: str) -> bool:
        a = f'{path}'
        return os.path.isdir(a)

    @staticmethod
    def check_file_type(file_name: str, file_types: Union[str, list[str], None] = None) -> bool:
        if file_types is None:
            file_types = default_file_types
        else:
            if type(file_types) is str:
                file_types = [file_types]
        for x in file_types:
            if file_name.endswith(f".{x}"):
                return True
            else:
                continue
        return False

    @staticmethod
    def check_file(file: str, file_types: Union[str, list[str], None] = None) -> bool:
        if os.path.isfile(file):
            if file_types is not None:
                if Helper.check_file_type(file, file_types) is False:
                    return False
            return True
        else:
            return False

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

    @staticmethod
    def __list_or_str(answer: Union[str, list], random: bool) -> str:
        if type(answer) is list:
            if random is True:
                return choice(answer)
            else:
                return answer[0]
        else:
            return answer

    def msg(self, msg: str, default: str = None, random: bool = True, *args, **kwargs):
        language: dict = languages[self.language]
        answer = language.get(msg)
        if answer is None:
            if default is not None:
                answer = default
            else:
                answer = languages[default_language].get(msg, default_text)
        answer = self.__list_or_str(answer=answer, random=random).format(*args, **kwargs)
        return answer
