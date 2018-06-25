import concurrent.futures
import functools
import os
import time
from configparser import ConfigParser

import click

from document_archive import document_archive
from git_pull import git_pull

CONFIG_PATH = r'config/project_controler.cfg'  # Config file path
GIT_PATH, GIT_BRANCH = 'Git Path', 'Git Branch'  # Config sections


@click.group()
def main():
    pass


@main.command()
def sync():
    """
    Synchronize local git repository with remote ones
    """
    import subprocess
    from multiprocessing import cpu_count

    config = ConfigParser()
    if not os.path.exists(CONFIG_PATH):
        click.echo(f'Enable to read config file, please check in {os.path.realpath(CONFIG_PATH)}.\n'
                   f'You could create config file template with create_config option.')
        return
    config.read(CONFIG_PATH)

    # use git pull to synchronous all the repository simultaneously
    with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        tasks = {}
        for project, path in config[GIT_PATH].items():
            branch = config[GIT_BRANCH].get(project, 'master')
            tasks[executor.submit(functools.partial(
                git_pull, path, branch))] = (path, branch)

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
@click.option('--file', default='archive_document.json')
@click.option('--no-file', is_flag=True)
@click.option('--mongo', default='localhost:27017')
@click.option('--no-mongo', is_flag=True)
def doc_archive(file, no_file, mongo, no_mongo):
    """
    Reconstruct document to review file into a json format file
    """
    import json
    import pymongo
    from pprint import pprint
    from pymongo.errors import PyMongoError, ConnectionFailure

    json_data = document_archive()

    if not no_file:
        click.echo(f'Succesfully retrived {len(json_doc)} data:\n......')
        pprint(json_data[-5:])
        try:
            with open(file, 'w', encoding='utf-8') as fh:
                json.dump(json_data, fh)
        except IOError:
            click.echo(f'Unable to write file {os.path.realpath(file)}.')
            return
        click.echo(
            f'Json file is generated. Please check in {os.path.realpath(file)}.')

    if not no_mongo:
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
    Create config file template for project controller
    """
    if os.path.exists(CONFIG_PATH):
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
