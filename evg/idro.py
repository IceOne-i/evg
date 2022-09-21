import json
import os
import pathlib

script_dir = pathlib.Path(__file__).parent.resolve()

local_path = f"locales"
default_language = "ru"


class Checker:
    def __init__(self):
        pass

    def check_directory(self, directory: str) -> bool:
        a = f'{directory}'
        print(a)
        return os.path.isdir(a)

    def check_language(self, directory: str, language: str) -> bool:
        a = f'{directory}/{language}'
        print(a)
        return os.path.isdir(a)

    def check_file(self, path: str, file: str) -> bool:
        a = f'{path}/{file}.json'
        print(a)
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
    def __init__(self, language: str, category: str):
        self.language = language
        self.category = category
        if not Checker().check_language(directory=local_path, language=self.language):
            if Checker().check_language(directory=local_path, language=default_language):
                self.language = default_language
            else:
                raise f"Необнаружено языкового пакета!"

        if not Checker().check_file(path=f"{local_path}/{self.language}", file=self.category):
            raise "Необнаружено языковой категории!"

    def msg(self, msg: str) -> str:
        with open(f'{local_path}/{self.language}/{self.category}.json', 'r', encoding='utf-8') as f:
            text = json.load(f)
        try:
            return text[msg]
        except Exception as e:
            raise "Необнаружено языкового ключа!"
