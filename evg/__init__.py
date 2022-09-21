from .idro import *

if not Checker().check_directory(directory=idro.local_path):
    raise "Необнаружено языковой папки!"