# localdpkg-42 

This script is made to formalize the install of packages on 42school's linux-based machines.

## Usage:

```sh
# python3 ./main.py --package_path ~/Downloads/ripgrep_13.0.0-4+b2_amd64.deb --package_name ripgrep --install_path ~/.local
#                                 exa_1.0.deb                          # exa                         # ~/.local STRONGLY recommended
python3 ./main.py --package_path <path_to_deb_archive> --package_name <package_name> --install_path <install_path>
```

## What it does:
This script will execute if your install path contains /bin, /share and /lib, and if the environment variables `$PATH`, `$XDG_DATA_DIRS` point to them
# TODO: LD_LIBRARY_PATH 

## How to get .deb files
The simplest way to get .deb files is to use `apt` like so:
```sh
apg-get install --download-only <package_name>
```

Otherwise, you can download them on the web directly
