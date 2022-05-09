#!/usr/bin/env python

import argparse
import git


def get_input_args():
    parser = argparse.ArgumentParser(description=(
        'Get git release tags associated with the current commit ID.'
    ))
    parser.add_argument(
        '--repo-path',
        type=str,
        default='.',
        help='Path to the git repository'
    )

    return parser.parse_args()


def main():
    args = get_input_args()

    repo = git.Repo(args.repo_path)
    tags = repo.git.tag('-l', '--contains', 'HEAD')
    tag_list = tags.split('\n')


print(main())
