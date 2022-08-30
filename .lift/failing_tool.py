#!/usr/bin/env python3
import argparse

def emit_version():
    print(1)


def emit_name():
    print("failing_tool")


def emit_applicable():
    print("true")

def run():
    print('[{\"type\" : \"lift test dev1\",\"message\" : \"testing lift in dev1\", \"file\" : \".lift/failing_tool.py\",\"line\" : 1}]')
    print('[{\"type\" : \"lift test dev1\",\"message\" : \"testing lift in dev1\", \"file\" : \".lift/failing_tool.py\",\"line\" : 2}]')
    # raise Exception('Feeling under the weather')

def main():
    parser = argparse.ArgumentParser(description='Failing Tool')
    parser.add_argument('path', metavar='PATH', help='Path to code')
    parser.add_argument('commit_hash', metavar='HASH', help='Commit hash')
    parser.add_argument('command', metavar='COMMAND', help='Command')

    args = parser.parse_args()

    path = args.path

    command = args.command

    if command == "version":
        emit_version()
    elif command == "name":
        emit_name()
    elif command == "applicable":
        emit_applicable()
    elif command == "run":
        run()

if __name__ == "__main__":
    main()
