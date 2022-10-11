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


def get_tag_in_last_commit(repo):
    try:
        tags = repo.git.describe('--exact-match', 'HEAD')
        tag_list = tags.split('\n')
    except git.exc.GitCommandError as e:
        tag_list = []

    return tag_list


def get_tags(repo):
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    tags.reverse()
    return tags


def main():
    args = get_input_args()

    repo = git.Repo(args.repo_path)
    
    return get_tags(repo)

print(main())
