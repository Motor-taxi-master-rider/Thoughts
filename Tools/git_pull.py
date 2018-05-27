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
        self._logger = MyLogger(os.path.basename(repo_path))

    def pull(self, branch: str):
        """
        git pull from remote repository
        :param branch: branch to checkout
        """

        os.chdir(self._repo_path)

        with open(os.devnull, 'w') as rubbish:
            checkout = subprocess.Popen(['git', 'checkout', branch], stdout=rubbish, stderr=subprocess.PIPE)
            with checkout.stderr as checkout_err:
                self._log_result('', checkout_err.read().decode('utf-8'))
            checkout.wait()

        pull = subprocess.Popen(['git', 'pull', '--rebase'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with pull.stdout as pull_out, pull.stderr as pull_err:
            self._log_result(pull_out.read().decode('utf-8'), pull_err.read().decode('utf-8'))
        pull.wait()

    def _log_result(self, stdout: str, stderr: str):
        if stdout:
            self._logger.info(stdout[:-1])
        if stderr:
            self._logger.error(stderr[:-1])
