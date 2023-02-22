import os
import argparse

## parse args (duh)
def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [TARGET_NAME]...",
        description="get all articles from a substack"
    )

    parser.add_argument(
        "--help", action="usage",
        usage = f"{parser.prog} version 0.0.1"
    )
    parser.add_argument(
        "--package", help="path to the .deb archive you wish to install.", type=str
    )

    parser.add_argument(
        "--install-path", help="path to the directory you with to use as a fake root for your packages.", type=str
    )
    return parser

#XDG_CONFIG_PATH
#LD_LIBRARY_PATH
#PATH

def verify_install_path(install_path):
    absolute_install_path = os.path.abspath(install_path)
    environment_vars = ['PATH', 'LD_LIBRARY_PATH', 'XDG_CONFIG_PATH']

    for v in environment_vars:
        full_var = os.environ[v]
        if not full_var.__contains__(absolute_install_path):
            print("")

def main():
    arg_parser = init_argparse()
    args = arg_parser.parse_args()

    verify_install_path(arg_parser.install-path)

if __name__ == '__main__':
    main()
