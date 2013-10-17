__author__ = 'Duminsky Nick'
"""
Config file format and default values (if exist):
[BASIC]
ProjectFolder:
LogFile: (OutputFolder) + /log
OutputFolder: (ProjectFolder) + /docs/
IntendStyle:(space|tab)
"""

import configparser


def get_config(configpath: str) -> dict:
    res = {}
    try:
        config = configparser.ConfigParser()
        config.read(configpath)
        for key in config['BASIC']:
            res[key] = config['BASIC'].get(key)
        return res
    except IsADirectoryError:
        print(configpath, 'is a directory', sep=' ')


def write_config(configpath: str, kwargs: dict) -> None:
    """
    writes config file. kwargs = {'projectfolder': path_to_project,
                                  'logfile': path_to_log_file,
                                  'outputfolder': path_to_output_folder,
                                  'intendstyle': space|tab}
    """
    try:
        config = configparser.ConfigParser(kwargs)
        with open(configpath, mode='w', encoding='utf-8') as confopen:
            config.write(confopen)
    except IsADirectoryError:
        print(configpath, 'is a directory', sep=' ')