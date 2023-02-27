import argparse
import os
import subprocess

## parse args (duh)
def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [TARGET_NAME]...",
        description="install a .deb package to a directory (~/.local/ recommended)"
    )

    parser.add_argument(
        "--package_path", help="Path to the .deb archive you wish to install.", type=str
    )
    parser.add_argument(
        "--package_name", help="Name of the package.", type=str
    )
    parser.add_argument(
        "--install_path", help="Path to the directory you with to use as a fake root for your packages.", type=str
    )
    return parser

#XDG_DATA_DIRS
#LD_LIBRARY_PATH
#PATH
def verify_install_path(install_path):
    absolute_install_path = os.path.abspath(install_path)
    environment_vars = ['PATH', 'XDG_DATA_DIRS'] # LD_LIBRARY_PATH

    for v in environment_vars:
        full_var = os.environ[v]
        found = False
        splits = full_var.split(":")
        for s in splits:
            if full_var.__contains__(absolute_install_path):
                found = True
        if not found:
            print(f"You need to add {absolute_install_path} to the {v} environment variable for this to work")
            exit (1)

def extract_package(package_path, package_name):
    mkdir_cmd = "mkdir -p " + package_name
    dpkg_cmd = "dpkg" + " -x " + package_path + " " + package_name

    print(mkdir_cmd)
    print(dpkg_cmd)
    subprocess.run(mkdir_cmd, shell=True)
    subprocess.run(dpkg_cmd, shell=True)

def move_contents_to_dir(install_path, package_name):
    absolute_install_path = os.path.abspath(install_path)
    share_path = absolute_install_path + "/share"
    bin_path = absolute_install_path + "/bin"
    lib_path = absolute_install_path + "/lib"

    if not os.path.exists(share_path):
        print(f"{share_path} does not exist")
        exit(1)
    if not os.path.exists(bin_path):
        print(f"{bin_path} does not exist")
        exit(1)
    if not os.path.exists(lib_path):
        print(f"{lib_path} does not exist")
        exit(1)

    extracted_package_path = os.path.abspath(package_name)
    extracted_share_path = extracted_package_path + "/usr/share"
    extracted_bin_path = extracted_package_path + "/usr/bin"
    extracted_lib_path = extracted_package_path + "/usr/lib"
    if os.path.exists(extracted_bin_path):
        print(f"Copying binaries to {extracted_bin_path}")
        cp_command = "cp -iv " + extracted_bin_path + "/* " + bin_path
        subprocess.run(cp_command, shell=True)
    if os.path.exists(extracted_share_path):
        print(f"{extracted_share_path} does not exist")
    if os.path.exists(extracted_lib_path):
        print(f"{extracted_lib_path} does not exist")

def main():
    arg_parser = init_argparse()
    args = arg_parser.parse_args()

    verify_install_path(args.install_path)

    extract_package(args.package_path, args.package_name)
    move_contents_to_dir(args.install_path, args.package_name)

if __name__ == '__main__':
    main()
