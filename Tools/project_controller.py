import functools
import pathlib
import time
from configparser import ConfigParser
from pathlib import Path

import click

from calculate_size import calculate_size
from util.logger import MyLogger

CONFIG_PATH: Path = Path(__file__).parent / 'config' / 'project_controller.cfg'  # Config file path
GIT_PATH, GIT_BRANCH = 'Git Path', 'Git Branch'  # Config sections


@click.group()
def main():
    pass


@main.command()
def sync():
    """
    Synchronize local git repository with remote ones.
    """

    import concurrent.futures
    import subprocess

    from git_pull import git_pull

    logger = MyLogger('Sync')
    config = ConfigParser()

    if not CONFIG_PATH.exists():
        logger.error(f'Enable to find config file, please check whether {CONFIG_PATH} exists.\n'
                     f'You could create config file template with create_config option.')
        return
    config.read(CONFIG_PATH)

    # use git pull to synchronous all the repository simultaneously
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = {}
        for project, path_str in config[GIT_PATH].items():
            path = Path(path_str)
            branch = config[GIT_BRANCH].get(project, 'master')
            tasks[executor.submit(functools.partial(git_pull, path.expanduser(), branch))] = (path, branch)

        if not len(tasks):
            logger.error('No repository to synchronize.')
            return
        for task in concurrent.futures.as_completed(tasks):
            path, branch = tasks[task]
            try:
                task.result()
            except subprocess.CalledProcessError:
                logger.exception(f'Synchronize failed in {path}:{branch}.')
        else:
            time.sleep(0.1)  # wait for logging message printing
            logger.info('All repository is synchronized.')


@main.command()
@click.argument('output', type=click.Choice(['mongo', 'file']), default='mongo')
@click.option('--file', default='archive_document.json')
@click.option('--mongo', default='localhost:27017')
def doc_archive(output, file, mongo, bson=None):
    """
    Reconstruct document to review file into a json format file or mongodb.
    """

    from document_archive import document_archive

    logger = MyLogger('Archive')
    json_data = document_archive()

    if output == 'mongo':
        import pymongo
        from pymongo.errors import PyMongoError, ConnectionFailure

        logger.info(f'Trying to connect mongodb in {mongo}.')
        try:
            client = pymongo.MongoClient(f'mongodb://{mongo}/')
        except ConnectionFailure:
            logger.exception(f'Unable to connect {mongo}.')
            return

        try:
            database = client.doc_search
            collection = database.document_meta
        except PyMongoError:
            logger.exception(
                'Unable to find correct collection in database. Please confirm doc_search.document_meta exists.')
            return
        try:
            result = collection.insert_many(json_data)
        except PyMongoError:
            logger.exception('Unable insert data.')
            return
        logger.info(
            f'{len(result.inserted_ids)} documents have been loaded into mongodb.')
    elif output == 'file':
        import json
        from bson import json_util
        from pprint import pprint

        logger.info(f'Successfully retrieve {len(json_data)} data:\n......')
        pprint(json_data[-5:])
        try:
            with open(file, 'w', encoding='utf-8') as fh:
                json.dump(json_data, fh, default=json_util.default)
        except IOError:
            logger.exception(f'Unable to write file {str(file)}.')
            return
        logger.info(
            f'Json file is generated. Please check in {str(file)}.')


@main.command()
def create_config():
    """
    Create config file template for project controller.
    """

    logger = MyLogger('Config')

    if CONFIG_PATH.exists():
        logger.error(f'Config file {CONFIG_PATH} already existed.')
        return
    sections = {GIT_PATH: '# Config project name and local path of the project\n'
                          '# Syntax:{project name} = {Path/to/repo}\n',
                GIT_BRANCH: '# Config project name and branch to synchronize, default master if not config\n'
                            '# Syntax:{project name} = {repository branch}\n'}

    config_template = ''
    for section_name, comment in sections.items():
        config_template += f'[{section_name}]\n'
        config_template += comment
        config_template += '\n'
    CONFIG_PATH.write_text(config_template)
    logger.info(f'Config file template is created.')


@main.command()
@click.argument('path', type=click.STRING, default='.')
@click.option('--by_size', is_flag=True, show_default=True, default=False)
def list_size(path: str, by_size: bool):
    """
    List file and folder size under given path.
    """
    logger = MyLogger('List size')
    path = pathlib.Path(path)
    logger.info(f'Listing size of {path}')
    calculate_size(path, by_size)


if __name__ == '__main__':
    main()
