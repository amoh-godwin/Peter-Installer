# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:59:52 2019

@author: Ampofo
"""
import os
import threading
from time import sleep
import platform
import socket

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from settings import Setts

if platform.system().lower() == 'windows':
    from install import install_win as install_mod


class Connector(QObject):


    def __init__(self):
        QObject.__init__(self)
        # Call the Installer Class
        self.installer = install_mod.Install()
        self.home = self.installer.destination

        # Settings class
        self.setts = Setts()

        self.install_location = self.home
        self.current_size = 0
        self.processes = [None, None, None, None, None, None, None, None]
        self.passcode = ''

    log = pyqtSignal(str, arguments=['logger'])
    update = pyqtSignal(int, arguments=['updater'])
    updateLocation = pyqtSignal(str, arguments=['updateLoc'])
    done = pyqtSignal(int, arguments=['doner'])

    def logger(self, message):
        self.log.emit(message)

    def updater(self, percent):
        self.update.emit(percent)

    def updateLoc(self, location):
        self.updateLocation.emit(location)
        return location

    def waiter(self, stage):
        w_thread = threading.Thread(target=self._waiter, args=[stage])
        w_thread.daemon = True
        w_thread.start()

    def _waiter(self, stage):

        percent = 100 / self.installer.folder_size[stage]
        no = 0
        while True:
            no += 1
            sleep(0.2)
            self.current_size = self.installer.curr_folder_size[stage]
            if self.current_size == self.installer.folder_size[stage]:
                self.doner(stage)
                break
            else:
                self.logger(self.installer.curr_copying_file[stage])
                self.updater(self.current_size * percent)

    def doner(self, stage):
        self.done.emit(stage)

    @pyqtSlot(int)
    def rollback(self, stage):
        rollback_thread = threading.Thread(target=self._rollback, args=[stage])
        rollback_thread.daemon = True
        rollback_thread.start()

    def _rollback(self, stage):
        if stage == 3:
            self.stop_server_install()

    @pyqtSlot()
    def use_default_path(self):
        def_path_thread = threading.Thread(target=self._use_default_path)
        def_path_thread.daemon = True
        def_path_thread.start()

    def _use_default_path(self):
        self.updateLoc(self.home)

    @pyqtSlot(str)
    def save_location(self, location):
        slocation_thread = threading.Thread(target=self._save_location,
                                            args=[location])
        slocation_thread.daemon = True
        slocation_thread.start()

    def _save_location(self, location):
        self.installer.prepare_location(location)
        self.install_location = location
        # save to db
        self.setts.create_general_table(location)

    @pyqtSlot()
    def start_server_install(self):
        start_server_thread = threading.Thread(target=self._start_server_install)
        start_server_thread.daemon = True
        start_server_thread.start()

    def _start_server_install(self):
        # stage 3

        # check which port to be used
        port = self.setts.check_port(80)
        self.installer.server_port = port

        # start copying
        self.processes[3] = self.installer.copy_server_files()
        self.waiter(3)

        upath = os.path.join(self.home, 'bin', 'Peterd')
        self.setts.create_server_table(0, '127.0.0.1',
         'localhost', upath, 80, port, 'Stopped')
        self.setts.create_server_processes_table()

    # @pyqtSlot()
    def stop_server_install(self):
        stop_server_thread = threading.Thread(target=self._stop_server_install)
        stop_server_thread.daemon = True
        stop_server_thread.start()

    def _stop_server_install(self):
        self.processes[3].kill()
        self.setts.drop_table('Servers')

    @pyqtSlot(str)
    def save_auth(self, passcode):
        save_auth_thread = threading.Thread(target=self._save_auth,
                                            args=[passcode])
        save_auth_thread.daemon = True
        save_auth_thread.start()

    def _save_auth(self, passcode):
        self.passcode = passcode
        self.installer.passcode = self.passcode

    @pyqtSlot()
    def start_mysql_install(self):
        start_mysql_thread = threading.Thread(target=self._start_mysql_install)
        start_mysql_thread.daemon = True
        start_mysql_thread.start()

    def _start_mysql_install(self):
        # stage 5

        # check which port to be used
        port = self.setts.check_port(3306, 'mysql')
        self.installer.mysql_port = port

        upath = os.path.join(self.home, 'bin/mysql')
        self.setts.create_database_table(self.passcode, upath, port)
        self.setts.create_database_processes_table()

        self.waiter(5)
        self.processes[5] = self.installer.copy_mysql_files()

    @pyqtSlot()
    def stop_mysql_install(self):
        stop_mysql_thread = threading.Thread(target=self._stop_mysql)
        stop_mysql_thread.daemon = True
        stop_mysql_thread.start()

    def _stop_mysql(self):
        self.processes[5].kill()
        self.setts.drop_table('Databases')

    @pyqtSlot()
    def start_php_install(self):
        start_php_thread = threading.Thread(target=self._start_php_install)
        start_php_thread.daemon = True
        start_php_thread.start()

    def _start_php_install(self):
        # stage = 6
        self.processes[6] = self.installer.copy_php_files()
        self.waiter(6)

    @pyqtSlot()
    def stop_php_install(self):
        stop_php_thread = threading.Thread(target=self._stop_php_install)
        stop_php_thread.daemon = True
        stop_php_thread.start()

    def _stop_php_install(self):
        self.processes[6].kill()

    def _fini_watcher(self, stage):

        percent = 100 / self.installer.folder_size[stage]
        while True:
                sleep(0.2)
                self.current_size = self.installer.curr_folder_size[stage]
                if self.current_size == self.installer.folder_size[stage]:
                    break
                else:
                    real_size = self.current_size * percent * 0.9
                    self.updater(real_size)

    @pyqtSlot()
    def start_finalising(self):
        start_finalising_thread = threading.Thread(target=self._start_finalising)
        start_finalising_thread.daemon = True
        start_finalising_thread.start()

    def _start_finalising(self):
        # stage = 7

        self.installer.write_my_ini_file()
        self.installer.write_php_ini_file()
        self.updater(10)
        self.updater(20)

        # init mysql
        self.installer.init_mysql()
        self._fini_watcher(7)
        self.updater(45)
        self.installer.start_mysqld()
        self.updater(85)
        self.installer.set_pass()
        self.updater(90)
        self.updater(100)
        self.doner(7)
        # self.waiter(7)

    @pyqtSlot()
    def stop_finalising(self):
        stop_finalising_thread = threading.Thread(target=self._stop_finalising)
        stop_finalising_thread.daemon = True
        stop_finalising_thread.start()

    def _stop_finalising(self):
        self.processes[7].kill()

    @pyqtSlot()
    def launch_application(self):
        launch_app_thread = threading.Thread(target=self._launch_application)
        launch_app_thread.daemon = True
        launch_app_thread.start()

    def _launch_application(self):
        pass
