import os
import pathlib
import argparse 
import configparser


'''
@usage
-----------------------------------------
config tool_name
config -a --add     path        tool_name
config -d --delete  tool_name
'''


class Config:
    def __init__(self, file):
        self.file = file
        self.config = configparser.ConfigParser()
        self.config.read(self.file)

    def get_editor(self):
        return self.config['GENERAL']['editor']

    def get_path(self, tool_name):
        return self.config[tool_name]['path']

    def add_path(self, tool_name, path):
        self.config[tool_name] = {}
        self.config[tool_name]['path'] = path
        with open(self.file, 'w') as configfile:
            self.config.write(configfile)

    def del_path(self, tool_name):
        self.config.remove_section(tool_name)
        with open(self.file, 'w') as configfile:
            self.config.write(configfile)


def main():

    config = Config('config.ini')

    parser = argparse.ArgumentParser(prog = 'fig', description = 'edit dotfiles with a centralized tool')
    option = parser.add_mutually_exclusive_group()

    parser.add_argument('tool', help = 'name of the tool to configure or modify')
    option.add_argument('-a', '--add', nargs = 1, metavar = 'path', help = 'add a new config file path')
    option.add_argument('-d', '--delete', action = 'store_true', help = 'delete an existing config file path')
    
    args = parser.parse_args()

    print(args)

    if args.add:
        config.add_path(args.tool, args.add[0])

    elif args.delete:
        config.del_path(args.tool)    

    else:
        os.system(config.get_editor() + ' ' + config.get_path(args.tool))


if __name__ == "__main__":
    main()

