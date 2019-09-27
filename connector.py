# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:59:52 2019

@author: Ampofo
"""
import os
import threading
from time import sleep
import platform

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

if platform.system() == 'Windows':
    from install import install_win as install_mod

class Connector(QObject):


    def __init__(self):
        QObject.__init__(self)
        self.home = 'C:/Deuteronomy Works/Peter/'
        self.install_location = "C:/Deuteronomy Works/Peter"
        self.current_size = 0
        # Send to the  Installer Class
        self.installer = install_mod.Install(self.install_location)
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
        if stage != 6:
            while True:
                no += 1
                sleep(1)
                self.current_size = len(os.listdir(os.path.join(self.install_location,
                                                         self.installer.path[stage])))
                print(no, ':', self.current_size, '/', self.installer.folder_size[stage])
                if self.current_size == self.installer.folder_size[stage]:
                    self.doner(stage)
                    break
                else:
                    self.updater(self.current_size * percent)
        else:
            while True:
                no += 1
                sleep(1)
                self.current_size = self.installer.curr_folder_size[stage]
                print(no, ':', self.current_size, '/', self.installer.folder_size[stage])
                if self.current_size == self.installer.folder_size[stage]:
                    self.doner(stage)
                    break
                else:
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
        self.install_location = location

    @pyqtSlot()
    def start_server_install(self):
        start_server_thread = threading.Thread(target=self._start_server_install)
        start_server_thread.daemon = True
        start_server_thread.start()

    def _start_server_install(self):
        # stage 3
        self.processes[3] = self.installer.copy_server_files()
        self.waiter(3)

    # @pyqtSlot()
    def stop_server_install(self):
        stop_server_thread = threading.Thread(target=self._stop_server_install)
        stop_server_thread.daemon = True
        stop_server_thread.start()

    def _stop_server_install(self):
        self.processes[3].kill()

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
        print('here 5')
        self.doner(5)
        #self.waiter(5)
        #self.processes[5] = self.installer.copy_mysql_files()

    @pyqtSlot()
    def stop_mysql_install(self):
        stop_mysql_thread = threading.Thread(target=self._stop_mysql)
        stop_mysql_thread.daemon = True
        stop_mysql_thread.start()

    def _stop_mysql(self):
        self.processes[5].kill()

    @pyqtSlot()
    def start_php_install(self):
        start_php_thread = threading.Thread(target=self._start_php_install)
        start_php_thread.daemon = True
        start_php_thread.start()

    def _start_php_install(self):
        # stage = 6
        print('here 6')
        self.processes[6] = self.installer.copy_php_files()
        # self.doner(6)
        self.waiter(6)

    @pyqtSlot()
    def stop_php_install(self):
        stop_php_thread = threading.Thread(target=self._stop_php_install)
        stop_php_thread.daemon = True
        stop_php_thread.start()

    def _stop_php_install(self):
        self.processes[6].kill()

    @pyqtSlot()
    def start_finalising(self):
        start_finalising_thread = threading.Thread(target=self._start_finalising)
        start_finalising_thread.daemon = True
        start_finalising_thread.start()

    def _start_finalising(self):
        # stage = 7
        #self.installer.write_ports()
        #self.installer.write_my_ini_file()
        #self.installer.write_php_ini_file()
        #self.processes[7] = self.installer._create_sets_file()
        
        # init mysql
        #self.installer.init_mysql()
        #self.installer.start_mysqld()
        #self.installer.set_pass()
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
