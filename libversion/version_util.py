import os
import subprocess

class VersionUtil:
    @staticmethod
    def get_version():
        '''
        Tries to get library version from files. If that fails,
        gets library version from Git
        '''
        version = VersionUtil.get_version_from_file()
        if not version:
            version = VersionUtil.get_version_from_git()
        return version

    @staticmethod
    def get_version_from_file():
        '''
        Get library version from file.
        '''
        version_file = os.path.join(os.path.dirname(__file__), 'version.txt')
        with open(version_file, 'r') as file:
            version = file.read().strip()
        return version

    @staticmethod
    def get_version_from_git():
        '''
        Get library version from Git.
        '''
        try:
            tag = subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode().strip()
            version = tag.lstrip('v')
        except (subprocess.CalledProcessError, OSError):
            version = None
        return version