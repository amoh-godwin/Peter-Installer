# Thank you Heavenly Father

import subprocess
import threading
from time import sleep
import os
import base64

class WinInstall():


    """
    """


    def __init__(self):
        super.__init__
        self.destination = "H:\\\\GitHub\\\\Peter"
        main_path = os.getcwd()
        self.passcode = 'ampofo1'
        self.main = main_path.replace('\\install', '')
        self.settings = [{'parent_folder': "",
                          "settings_file": "3ddb429e2f446edae3406bb9d0799eed7bddda600d9a05fe01d3baaa.settings",
                          "passcode": ""},
                         [{"index": 0, "name": "Peter Web Server",
                           "path": "PeterWebServer",
                           "port": 7773, "status": "Stopped"},
                       {"index": 1, "name": "MySQL Database",
                        "path": "mysql\\bin\\",
                        "status": "Stopped"}]]
        self.mysqld_proc = None
        # self.copy_files()
        self.init_mysql()
        self.start_mysqld()
        self._set_pass()
        # self.install_mysql_serv()
        
        self._create_file()


    def copy_files(self):

        cmd1 = 'xcopy ' + self.main + '\\php' + ' ' + self.destination + '\\php\\'
        cmd2 = 'xcopy ' + self.main + '\\mysql' + ' ' + self.destination + '\\mysql\\'
        
        print(cmd1, cmd2)

        out1 = check_output(cmd1 + ' /E /Y', shell=True)
        out2 = check_output(cmd2 + ' /E /Y', shell=True)

    def _create_file(self):
 
        self.settings[0]['parent_folder'] = self.destination
        self.settings[0]['passcode'] = self.passcode

        file_path = os.path.join(self.destination,
                                 self.settings[0]["settings_file"])

        with open(file_path, mode="wb") as sets_file:
            encoded_data = self._encrypt(self.settings)
            sets_file.write(encoded_data)

    def _encrypt(self, data):
        return base64.b64encode(bytes(str(data), 'ascii'))

    def init_mysql(self):

        out1 = subprocess.Popen(["H:\\GitHub\\Peter\\mysql\\bin\\mysqld.exe",
                                 "--console",
                                 "--initialize-insecure",
                                 "--explicit_defaults_for_timestamp",],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT,
                                shell=True)
        out1.wait()
        print(str(out1.stdout.read(), 'utf-8'))

    def install_mysql_serv(self):

        cmd = self.destination + \
        '\\\\mysql\\\\bin\\\\mysqld --install MySQL573 --defaults-file="'+ \
        self.destination + '\\\\mysql\\\\my.ini' + '"'
        out1 = subprocess.check_output(cmd, shell=True)
        print(out1)

    def start_mysqld(self):
        mysqld_thread = threading.Thread(target=self._start_mysqld)
        mysqld_thread.daemon = True
        mysqld_thread.start()
        
        sleep(3)


    def _start_mysqld(self):
        print('preparing mysql')
        self.mysqld_proc = subprocess.Popen(["H:\\GitHub\\Peter\\mysql\\bin\\mysqld.exe"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=False)

        print(self.mysqld_proc.stdout.read())
        print('help')

    def _set_pass(self):

        print('sleeping')
        print("yea")

        cmd = 'ALTER USER "root"@"localhost" IDENTIFIED BY "'+self.passcode+'"'
        out = subprocess.Popen(['H:\\GitHub\\Peter\\mysql\\bin\\mysql.exe',
                                '-u','root'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=False)
        # print(str(out.stdout.read(), 'utf-8'))
        print('sick')
        out1 = out.communicate(input=bytes(cmd, 'utf-8'))
        print('very sick')
        print(out1[0])
        out.kill()
        print('terminate')
        self._stop_mysqld()

    def _stop_mysqld(self):
        print('sleeping')
        #sleep(7)
        self.mysqld_proc.kill()
        print(str(self.mysqld_proc.stdout.read(), 'utf-8'))


WinInstall()
