import concurrent.futures
import functools
import os
import time
from configparser import ConfigParser
from os.path import dirname, expanduser, exists, join, realpath

import click

CONFIG_PATH = join(dirname(realpath(__file__)), 'config', 'project_controller.cfg')  # Config file path
GIT_PATH, GIT_BRANCH = 'Git Path', 'Git Branch'  # Config sections


@click.group()
def main():
    pass


@main.command()
def sync():
    """
    Synchronize local git repository with remote ones.
    """

    import subprocess
    from multiprocessing import cpu_count

    from git_pull import git_pull

    config = ConfigParser()
    if not exists(CONFIG_PATH):
        click.echo(f'Enable to find config file, please check whether {CONFIG_PATH} exitsts.\n'
                   f'You could create config file template with create_config option.')
        return
    config.read(CONFIG_PATH)

    # use git pull to synchronous all the repository simultaneously
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        tasks = {}
        for project, path in config[GIT_PATH].items():
            branch = config[GIT_BRANCH].get(project, 'master')
            tasks[executor.submit(functools.partial(
                git_pull, expanduser(path), branch))] = (path, branch)

        if not len(tasks):
            click.echo('No repository to synchronize.')
            return
        for task in concurrent.futures.as_completed(tasks):
            path, branch = tasks[task]
            try:
                task.result()
            except subprocess.CalledProcessError:
                click.echo(f'Synchronize failed in {path}:{branch}.')
        else:
            time.sleep(0.1)  # wait for logging message printing
            click.echo('All repository is synchronized.')


@main.command()
@click.argument('output', type=click.Choice(['mongo', 'file']), default='mongo')
@click.option('--file', default='archive_document.json')
@click.option('--mongo', default='localhost:27017')
def doc_archive(output, file, mongo):
    """
    Reconstruct document to review file into a json format file or mongodb.
    """

    from document_archive import document_archive

    json_data = document_archive()

    if output=='file':
        import json
        from bson import json_util
        from pprint import pprint

        click.echo(f'Succesfully retrived {len(json_data)} data:\n......')
        pprint(json_data[-5:])
        try:
            with open(file, 'w', encoding='utf-8') as fh:
                json.dump(json_data, fh, default=json_util.default)
        except IOError:
            click.echo(f'Unable to write file {realpath(file)}.')
            return
        click.echo(
            f'Json file is generated. Please check in {realpath(file)}.')

    if output=='mongo':
        import pymongo
        from pymongo.errors import PyMongoError, ConnectionFailure

        click.echo(f'Trying to connect mongodb in {mongo}.')
        try:
            client = pymongo.MongoClient(f'mongodb://{mongo}/')
        except ConnectionFailure:
            click.echo(f'Unable to connect {mongo}.')
            return

        try:
            database = client.doc_search
            collection = database.document_meta
        except PyMongoError:
            click.echo(
                'Unable to find correct collection in database. Please confirm doc_search.document_meta exists.')
            return
        try:
            result = collection.insert_many(json_data)
        except PyMongoError:
            click.echo('Unable insert data.')
            return
        click.echo(
            f'{len(result.inserted_ids)} documents have been loaded into mongodb.')


@main.command()
def create_config():
    """
    Create config file template for project controller.
    """

    if exists(CONFIG_PATH):
        click.echo(f'Config file {CONFIG_PATH} already existed.')
        return
    sections = {GIT_PATH: '# Config project name and local path of the project\n'
                          '# Syntax:{project name} = {Path/to/repo}\n',
                GIT_BRANCH: '# Config project name and branch to synchronize, default master if not config\n'
                            '# Syntax:{project name} = {repository branch}\n'}
    with open(CONFIG_PATH, 'w') as file:
        for section_name, comment in sections.items():
            file.write(f'[{section_name}]\n')
            file.write(comment)
            file.write('\n')
    click.echo(f'Config file template is created.')


if __name__ == '__main__':
    main()
