from .idro import *
import os
import json

if not Helper.check_directory(path=local_path):
    raise "Необнаружено языковой папки!"
else:
    _directories = Helper.directories(local_path)
    _languages = []
    if len(_directories) == 0:
        raise "Необнаружено языковых пакетов!"
    elif default_language not in _directories:
        raise "Необнаружено базового языкового пакета!"
    elif default_language in _directories and Helper.count_files(f"{local_path}/{default_language}", type=".json") == 0:
        raise "Необнаружено компонентов базового языкового пакета!"
    else:
        for language in _directories:
            if Helper.count_files(f"{local_path}/{language}", type=".json") == 0:
                continue
            _languages.append(language)

        for language in _languages:
            if language not in languages:
                languages[language] = {}
            categories = Helper.files(f"{local_path}/{language}", type=".json")
            for category in categories:
                category_path = f"{local_path}/{language}/{category}"
                with open(category_path, 'r', encoding='utf-8') as f:
                    inf = json.load(f)
                languages[language].update(inf)
