"""Console script for python_yapi."""
import argparse
import os
import sys
from configparser import ConfigParser


class YApiCli:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--base_url', help='YApi base url')
        self.parser.add_argument('--email', help='YApi user email')
        self.parser.add_argument('--password', help='YApi user password')
        self.parser.set_defaults(func=self.login)

        self.subparsers = self.parser.add_subparsers(dest='command', help='sub-command help')

        self.parse_add_project()
        self.parse_add_interface()

        config_file = '/Users/superhin/.yapi_config'
        self.config = {}
        if os.path.exists(config_file):
            conf = ConfigParser()
            conf.read(config_file)
            self.config['base_url'] = conf.get('DEFAULT', 'base_url')
            self.config['email'] = conf.get('DEFAULT', 'email')
            self.config['password'] = conf.get('DEFAULT', 'password')

        print('Config', self.config)

    def parse_add_project(self):
        parser = self.subparsers.add_parser('add_project', help='add_project help')
        parser.add_argument('--name', help='project name')
        parser.add_argument('--group_id', help='project group id')
        parser.add_argument('--color', help='project color')
        parser.add_argument('--icon', help='project icon')

        parser.set_defaults(func=self.add_project)

    def parse_add_interface(self):
        parser = self.subparsers.add_parser('add_interface', help='add_project help')
        parser.add_argument('--title', help='project name')
        parser.add_argument('--method', help='project group id')
        parser.add_argument('--project_id', help='project group id')

        parser.set_defaults(func=self.add_interface)

    def login(self, args):
        print(args.base_url)
        print(args.email, args.password)

    @staticmethod
    def add_project(args):
        print(args.base_url)
        print(args.email, args.password)
        print(args.name)
        print(args.group_id)
        print(args.color)
        print(args.icon)

    @staticmethod
    def add_interface(args):
        print(args.title)
        print(args.method)
        print(args.project_id)

    def parse_args(self):
        """Console script for python_yapi."""
        args = self.parser.parse_args()
        args.func(args)
        # if args.command == 'add_project':
        #     print(args.name)
        #     print(args.group_id)
        #     print(args.color)
        #     print(args.icon)
        #
        # if args.command == 'add_interface':
        #     print(args.title)
        #     print(args.method)
        #     print(args.project_id)
        # print("Sub Arguments: " + str(args._))
        # args = parser.parse_args()
        #
        # print("Arguments: " + str(args._))
        # print("Replace this message by putting your code into "
        #       "python_yapi.cli.main")
        return 0


if __name__ == "__main__":
    sys.exit(YApiCli().parse_args())  # pragma: no cover
