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


def main():
    parser = argparse.ArgumentParser(prog = 'fig', description = 'edit dotfiles with a centralized tool')

    parser.add_argument('tool', help='name of the tool to configure or modify')

    option = parser.add_mutually_exclusive_group()

    option.add_argument('-a', '--add', nargs = 1, metavar = 'path', help = 'add a new config file path')
    option.add_argument('-d', '--delete', action = 'store_true', help = 'delete an existing config file path')

    args = parser.parse_args()

    print(args)

    if args.add:
        print(f'received add command with tool name: {args.tool} and path: {args.add[0]}')
    elif args.delete:
        print(f'received delete command with tool name: {args.tool}')


if __name__ == "__main__":
    main()
