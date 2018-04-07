import os
import subprocess
import click
from configparser import ConfigParser

CONFIG_PATH = r'config/project_controler.cfg'


@click.group()
def main():
    pass


@main.command()
def sync():
    """
    Synchronize local git repository with remote ones
    :return:
    """
    GIT_CONFIG = 'Git Path'

    config = ConfigParser()
    try:
        config.read(CONFIG_PATH)
    except:
        click.echo(f'Enable to open config file, please check in {CONFIG_PATH}.')
    for branch in config[GIT_CONFIG]:
        path = config[GIT_CONFIG][branch]
        try:
            git_pull(path, branch)
        except subprocess.CalledProcessError as exc:
            click.echo(f'Synchronize failed in {path}:{branch}.')


def git_pull(path, branch):
    """
    git pull from remote repository
    :param path: path of local root repository
    :param branch: branch to checkout
    :return:
    """
    os.chdir(path)
    subprocess.run(['git', 'checkout', branch], check=True)
    subprocess.run(['git', 'pull', '--rebase'], check=True)


if __name__ == '__main__':
    main()
