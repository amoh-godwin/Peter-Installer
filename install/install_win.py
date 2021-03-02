# Thank you Heavenly Father

import subprocess
from urllib.request import urlopen
import threading
from time import sleep
import os
import base64

from recursive_size import get_size





class Install():


    """
    """


    def __init__(self):
        super.__init__
        self.destination = 'C:/Deuteronomy Works/Peter/'
        self.path = ['', '', '', 'bin', '', 'bin/mysql', 'bin/php']
        self.server_path = os.path.join(self.destination, 'bin')
        self.php_path = os.path.join(self.server_path, 'php')
        self.mysql_path = os.path.join(self.server_path, 'mysql')
        main_path = os.getcwd()
        self.main = os.path.join(main_path, '..', 'Cargo')
        SERVER_SIZE = get_size(
                        os.path.join(self.main, 'server'))
        PHP_SIZE = get_size(
                        os.path.join(self.main, 'php'))
        MYSQL_SIZE = get_size(
                        os.path.join(self.main, 'mysql'))
        self.folder_size = [0, 0, 0, SERVER_SIZE, 0, MYSQL_SIZE, PHP_SIZE, 6]
        self.curr_folder_size = [0, 0, 0, 0, 0, 0, 0, 0]
        self.curr_copying_file = ["", "", "", "", "", "", "", ""]
        self.folder_conts = [[], [], [], [], [], [], [], []]

        self.passcode = ''
        self.server_port = 0
        self.mysql_port = 3336
        self.settings = [{'parent_folder': "",
                          "settings_file": "3ddb429e2f446edae3406bb9d0799eed7bddda600d9a05fe01d3baaa.settings",
                          "passcode": ""},
                         [{"index": 0, "name": "Peter Web Server",
                           "path": "bin/PeterWebServer",
                           "default_port": 80, "port": 7773,
                           "status": "Stopped"},
                       {"index": 1, "name": "MySQL Database",
                        "path": "bin/mysql/bin/",
                        "status": "Stopped"}]]
        self.mysqld_proc = None
        self.copy_server_proc = None
        self.copy_myqld_proc = None
        self.copy_php_proc = None
        self.init_mysql_proc = None

        #self.init_mysql()
        #self.start_mysqld()
        #self.set_pass()

        # self._create_file()

    def copy_server_files(self):

        #cmd1 = 'xcopy ' + self.main + '\\base_files "' + self.server_destination + '"'

        # call watcher
        self.watcher('server')
    
        # make folders
        if not os.path.exists(self.server_path):
            os.makedirs(self.server_path)

        cmd = 'xcopy ' + self.main + '\\server "' + self.forward_slash(self.server_path) + '" /E /Y'
        print(cmd)

        self.copy_server_proc = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True)

        return self.copy_server_proc

    def write_ports(self):
        try:
            req = urlopen("http://localhost:80")
            self.server_port = 7773
            self.mysql_port = 3336
        except:
            self.server_port = 80
            self.mysql_port = 3306

    def write_php_ini_file(self):

        ini_path = os.path.join(self.php_path, 'php.ini')
        with open(ini_path, encoding='utf-8') as ini_file:
            contents = ini_file.read()

        # Port change
        contents = contents.replace("mysqli.default_port = 3306",
                                    "mysqli.default_port = "+str(self.mysql_port))
        # Dir change
        contents = contents.replace("C:/Test", 
                                    self.forward_slash(self.php_path))

        # Save
        with open(ini_path, mode='w', encoding='utf-8') as o_ini_file:
            o_ini_file.write(contents)

    def copy_php_files(self):

        # call watcher
        self.watcher('php')

        # Create the folder
        os.makedirs(self.php_path)
        cmd = 'xcopy ' + self.main + '\\php "' + self.forward_slash(self.php_path) + '" /E /Y'

        self.copy_php_proc = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True)
        return self.copy_php_proc

    def copy_mysql_files(self):

        # call watcher
        self.watcher('mysql')
        
        # Create the folder
        os.makedirs(self.mysql_path)
        cmd = 'xcopy ' + self.main + '\\mysql "' + self.forward_slash(self.mysql_path) + '" /E /Y'

        self.copy_mysqld_proc = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True)

        return self.copy_mysqld_proc

    def watcher(self, kind):
        watch_thread = threading.Thread(target=self._watcher, args=[kind])
        watch_thread.daemon = True
        watch_thread.start()

    def _watcher(self, kind):
        no = 0
        if kind == 'server':
            while True:
                no += 1
                sleep(0.1)
                if self.copy_server_proc:
                    for cont in self.copy_server_proc.stdout:
                        fn = str(cont, 'utf-8').strip()
                        self.curr_copying_file[3] = fn
                        self.curr_folder_size[3] += get_size(fn)
                        self.folder_conts[3].append(fn)
                        if ' copied' in fn:
                            break
                    if self.curr_folder_size[3] == self.folder_size[3]:
                        break

        elif kind == 'php':
            while True:
                no += 1
                sleep(0.1)
                if self.copy_php_proc:
                    for cont in self.copy_php_proc.stdout:
                        fn = str(cont, 'utf-8').strip()
                        self.curr_copying_file[6] = fn
                        self.curr_folder_size[6] += get_size(fn)
                        self.folder_conts[6].append(fn)
                        if ' copied' in fn:
                            break
                    if self.curr_folder_size[6] == self.folder_size[6]:
                        break

        elif kind == 'mysql':
            while True:
                no += 1
                sleep(0.1)
                if self.copy_mysqld_proc:
                    for cont in self.copy_mysqld_proc.stdout:
                        fn = str(cont, 'utf-8').strip()
                        self.curr_copying_file[5] = fn
                        self.curr_folder_size[5] += get_size(fn)
                        self.folder_conts[5].append(fn)
                        if ' copied' in fn:
                            break
                    if self.curr_folder_size[5] == self.folder_size[5]:
                        break

        elif kind == 'fini':
            while True:
                no += 1
                sleep(0.1)
                if self.init_mysql_proc:
                    out = self.init_mysql_proc.stdout.readline()
                    conts = out
                    self.curr_copying_file[7] = str(conts, 'utf-8')
                    self.curr_folder_size[7] += 1
                    self.folder_conts[7].append(conts)
                    if self.curr_folder_size[7] > 5:
                        break

    def _create_sets_file(self):
 
        self.settings[0]['parent_folder'] = self.destination
        self.settings[0]['passcode'] = self.passcode

        file_path = os.path.join(self.server_path,
                                 self.settings[0]["settings_file"])

        with open(file_path, mode="wb") as sets_file:
            encoded_data = self._encrypt(self.settings)
            sets_file.write(encoded_data)

    def _encrypt(self, data):
        return base64.b64encode(bytes(str(data), 'ascii'))

    def write_my_ini_file(self):

        ini_path = os.path.join(self.mysql_path, 'my.ini')
        with open(ini_path, encoding='utf-8') as ini_file:
            contents = ini_file.read()

        # Port change
        contents = contents.replace("port=3306", "port="+str(self.mysql_port))
        # Dir change
        contents = contents.replace("basedir=C:/Test/mysql", 
                                    'basedir="'+ \
                                    self.forward_slash(self.mysql_path) + '"')
        contents = contents.replace("datadir=C:/Test/mysql/data", 
                                    'datadir="' + \
                                    self.forward_slash(self.mysql_path) + \
                                    '/data"')
        contents = contents.replace("C:/Test",
                                    self.forward_slash(self.server_path))

        # Save
        with open(ini_path, mode='w', encoding='utf-8') as o_ini_file:
            o_ini_file.write(contents)

    def init_mysql(self):

        self.watcher('fini')

        os.makedirs(os.path.join(self.mysql_path, 'data'))
        
        self.init_mysql_proc = subprocess.Popen(
                [os.path.join(self.mysql_path, 'bin/mysqld'), 
                 "--console",
                 "--initialize-insecure",
                 "--explicit_defaults_for_timestamp"],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.STDOUT,
                 shell=True)

    def install_mysql_serv(self):

        cmd = self.destination + \
        '\\\\mysql\\\\bin\\\\mysqld --install MySQL573 --defaults-file="'+ \
        self.destination + '\\\\mysql\\\\my.ini' + '"'
        out1 = subprocess.check_output(cmd, shell=True)

    def start_mysqld(self):
        mysqld_thread = threading.Thread(target=self._start_mysqld)
        mysqld_thread.daemon = True
        mysqld_thread.start()

        sleep(3)

    def _start_mysqld(self):
        self.mysqld_proc = subprocess.Popen(
                [os.path.join(self.mysql_path, 'bin/mysqld')],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=False)

    def set_pass(self):

        cmd = f'ALTER USER "root"@"localhost" IDENTIFIED BY "{self.passcode}"'

        out = subprocess.Popen([os.path.join(self.mysql_path, 'bin\\mysql.exe'),
                                '-u','root'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               shell=False)

        # out.wait()
        out1 = out.communicate(input=bytes(cmd, 'utf-8'))
        out.kill()
        self._stop_mysqld()

    def _stop_mysqld(self):

        #sleep(7)
        self.mysqld_proc.kill()

    def prepare_location(self, location):
        # Prepare location
        # add the bin and server
        bin_path = os.path.join(location, 'bin')
        server_path = os.path.join(location, 'Server')
        if not os.path.exists(bin_path):
            os.makedirs(bin_path)
        if not os.path.exists(server_path):
            os.makedirs(server_path)

        return location

    def forward_slash(self, ln):
        if "\\\\" in ln:
            fixed = ln.replace("\\\\", "/")
        else:
            fixed = ln.replace("\\", "/")
        return fixed

