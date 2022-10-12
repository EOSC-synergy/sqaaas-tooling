#!/usr/bin/env python3

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
    tags = repo.tags
    repo.git.config('--global', '--add', 'safe.directory', "'*'")
    repo.git.tag('--sort=-taggerdate')
    # tags = sorted(repo.tags, key=lambda t: t.tag.tagged_date)
    # tags.reverse()
    tags = [str(tag) for tag in tags]

    return tags


def main():
    args = get_input_args()

    repo = git.Repo(args.repo_path, odbt=git.db.GitDB)
    
    return get_tags(repo)

print(main())
