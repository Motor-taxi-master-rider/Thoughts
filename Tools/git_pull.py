import os
import subprocess

from util.logger import MyLogger

PULL_CACHE = {}


def git_pull(path: str, branch: str):
    """
    git pull from remote repository
    :param path: path of local root repository
    :param branch: branch to checkout
    """
    if path not in PULL_CACHE:
        git_puller = GitPuller(path)
        git_puller.pull(branch)
        PULL_CACHE[path] = git_puller
    else:
        PULL_CACHE[path].pull(branch)


class GitPuller:
    def __init__(self, repo_path: str):
        """
        :param repo_path: path of local root repository
        """
        self._repo_path = repo_path
        self._logger = MyLogger(os.path.basename(repo_path).upper())

    def pull(self, branch: str):
        """
        git pull from remote repository
        :param branch: branch to checkout
        """

        os.chdir(self._repo_path)

        current_branch = subprocess.check_output(
            'git rev-parse --abbrev-ref HEAD').decode()[:-1]
        if not current_branch == branch:
            checkout = subprocess.Popen(
                ['git', 'checkout', branch], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self._log_result(checkout)

        pull = subprocess.Popen(
            ['git', 'pull', '--rebase'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self._log_result(pull)

    def _log_result(self, process: subprocess.Popen):
        with process.stdout as stdout, process.stderr as stderr:
            stdout = stdout.read().decode('utf-8')
            if stdout:
                self._logger.info(stdout[:-1])

            stderr = stderr.read().decode('utf-8')
            if stderr:
                self._logger.error(stderr[:-1])
        process.wait()
