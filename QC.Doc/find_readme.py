#!/usr/bin/env python

import argparse
from pathlib import Path


# Follows GitHub supported markup languages
# -- https://github.com/github/markup/blob/master/README.md#markups
AVAILABLE_EXTENSIONS = [
    '', # allow no-extension README
    '.markdown', '.mdown', '.mkdn', '.md',
    '.textile',
    '.rdoc',
    '.org',
    '.creole',
    '.mediawiki', '.wiki',
    '.rst',
    '.asciidoc', '.adoc', '.asc',
    '.pod'
]


def get_input_args():
    parser = argparse.ArgumentParser(
        description='Find main README file of a code repository.')
    parser.add_argument(
        'repo_root_path',
        metavar='PATH',
        type=str,
        help='Root path of the code repository'
    )
    parser.add_argument(
        '--extension',
        metavar='EXTENSION',
        type=str,
        action='append',
        help=(
            'Filter README extension (default: %s)' % AVAILABLE_EXTENSIONS
        )
    )

    return parser.parse_args()


def get_st_size(file_name):
    return Path(file_name).stat().st_size


def find_readmes(root_path, extensions):
    readme_file_list = []
    for extension in extensions:
        readme_file = 'README' + extension
        if list(Path(root_path).glob(readme_file)):
            readme_file_list.append(readme_file)
    return readme_file_list


def main():
    args = get_input_args()
    if not args.extension:
        args.extension = AVAILABLE_EXTENSIONS

    readme_file_list = find_readmes(
        root_path=args.repo_root_path,
        extensions=args.extension
    )
    return [
        {readme: {'size': get_st_size(readme)}}
        for readme in readme_file_list
    ]


print(main())
