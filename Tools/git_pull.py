from pathlib import Path
import subprocess

from util.logger import MyLogger

PULL_CACHE = {}


def git_pull(path: Path, branch: str):
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
    def __init__(self, repo_path: Path):
        """
        :param repo_path: path of local root repository
        """
        self._repo_path = repo_path
        self._logger = MyLogger(repo_path.name.upper())

    def pull(self, branch: str):
        """
        git pull from remote repository
        :param branch: branch to checkout
        """

        current_branch = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
                                        cwd=self._repo_path,
                                        stdout=subprocess.PIPE,
                                        universal_newlines=True).stdout.strip()
        if current_branch == branch:
            self.run_command('git', 'pull', '--rebase')
        else:
            self._logger.info(f'Current branch is {current_branch}, target branch is {branch}.')
            self.run_command('git', 'stash')
            self.run_command('git', 'checkout', branch, show_out=False)
            self.run_command('git', 'pull', '--rebase')
            self.run_command('git', 'checkout', current_branch, show_out=False)
            self.run_command('git', 'stash', 'pop', show_out=False)

    def run_command(self, *command, show_out=True, show_err=True):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self._repo_path)
        with process.stdout as stdout, process.stderr as stderr:
            if show_out:
                stdout = stdout.read().decode('utf-8')
                if stdout:
                    self._logger.info(stdout)
            if show_err:
                stderr = stderr.read().decode('utf-8')
                if stderr:
                    self._logger.error(stderr)
        process.wait()
