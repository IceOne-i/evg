from .idro import *
_local_path = f"locales"

if not Helper.check_directory(path=_local_path):
    os.makedirs(f"{_local_path}/{default_language}")
if Helper.count_directories(path=_local_path) == 0 or not Helper.check_directory(path=_local_path):
    os.makedirs(f"{_local_path}/{default_language}")

_directories = Helper.directories(_local_path)
_languages = []

if Helper.count_files(f"{_local_path}/{default_language}", type=".json") == 0:
    with open(f"{_local_path}/{default_language}/example.json", "w") as _f:
        _f.write("""{
        "hello": "Hello world!"
}""")
        _f.close()
else:
    for language in _directories:
        if Helper.count_files(f"{_local_path}/{language}", type=".json") == 0:
            continue
        _languages.append(language)

    for language in _languages:
        if language not in languages:
            languages[language] = {}
        categories = Helper.files(f"{_local_path}/{language}", type=".json")
        for category in categories:
            category_path = f"{_local_path}/{language}/{category}"
            try:
                with open(category_path, 'r', encoding='utf-8') as _f:
                    inf = json.load(_f)
                    _f.close()
                languages[language].update(inf)
            except json.decoder.JSONDecodeError as e:
                print(f"ВНИМАНИЕ! -> Файл {category} не был успешно загружен!\n"
                      f"ОШИБКА: {e}")
