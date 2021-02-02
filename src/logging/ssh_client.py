from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient


class SSHClientLogger:

    def __init__(self, env):
        self.__host = env.get('ssh_server')
        self.__user = env.get('ssh_user')
        self.__password = env.get('ssh_password')
        self.__port = 22
        self.__client = None

    def __enter__(self):
        self.__client = SSHClient()
        self.__client.set_missing_host_key_policy(AutoAddPolicy())
        self.__client.connect(hostname=self.__host, username=self.__user,
                              password=self.__password, port=self.__port)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.__client.close()

    def copy_log(self, filepath):
        remote_logs_path = 'larina'
        self.__client.exec_command(f'mkdir -p {remote_logs_path}')

        with SCPClient(self.__client.get_transport()) as scp:
            scp.put(filepath, remote_path=remote_logs_path)
