# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:59:52 2019

@author: Ampofo
"""
import threading
from time import sleep

import platform

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

if platform.system() == 'Windows':
    from install import install_win
    installer = install_win.WinInstall()

class Connector(QObject):


    def __init__(self):
        QObject.__init__(self)
        self.home = 'C:/Deuteronomy Works/Peter/'
        self.install_location = ''
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

    def doner(self, stage):
        self.done.emit(stage)

    @pyqtSlot(int)
    def rollback(self, stage):
        rollback_thread = threading.Thread(target=self._rollback)
        rollback_thread.daemon = True
        rollback_thread.start()

    def _rollback(self, stage):
        pass

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
        print('installing server to: ', self.install_location)
        sleep(3)
        print('done')
        self.doner(3)

    @pyqtSlot()
    def stop_server_install(self):
        stop_server_thread = threading.Thread(target=self._stop_server_install)
        stop_server_thread.daemon = True
        stop_server_thread.start()

    def _stop_server_install(self):
        pass

    @pyqtSlot(str)
    def save_auth(self, passcode):
        save_auth_thread = threading.Thread(target=self._save_auth,
                                            args=[passcode])
        save_auth_thread.daemon = True
        save_auth_thread.start()

    def _save_auth(self, passcode):
        self.passcode = passcode
        print(self.passcode)

    @pyqtSlot()
    def start_mysql_install(self):
        start_mysql_thread = threading.Thread(target=self._start_mysql_install)
        start_mysql_thread.daemon = True
        start_mysql_thread.start()

    def _start_mysql_install(self):
        # stage 5
        print('installing mysql to: ', self.install_location)
        sleep(3)
        print('done')
        self.doner(5)

    @pyqtSlot()
    def stop_mysql_install(self):
        stop_mysql_thread = threading.Thread(target=self._stop_mysql)
        stop_mysql_thread.daemon = True
        stop_mysql_thread.start()

    def _stop_mysql(self):
        pass

    @pyqtSlot()
    def start_php_install(self):
        start_php_thread = threading.Thread(target=self._start_php_install)
        start_php_thread.daemon = True
        start_php_thread.start()

    def _start_php_install(self):
        # stage = 6
        print('installing php to: ', self.install_location)
        sleep(3)
        print('done')
        self.doner(6)

    @pyqtSlot()
    def stop_php_install(self):
        stop_php_thread = threading.Thread(target=self._stop_php_install)
        stop_php_thread.daemon = True
        stop_php_thread.start()

    def _stop_php_install(self):
        pass

    @pyqtSlot()
    def start_finalising(self):
        start_finalising_thread = threading.Thread(target=self._start_finalising)
        start_finalising_thread.daemon = True
        start_finalising_thread.start()

    def _start_finalising(self):
        # stage = 7
        print('Finalising: ', self.install_location)
        sleep(3)
        print('done')
        self.doner(7)

    @pyqtSlot()
    def stop_finalising(self):
        stop_finalising_thread = threading.Thread(target=self._stop_finalising)
        stop_finalising_thread.daemon = True
        stop_finalising_thread.start()

    def _stop_finalising(self):
        pass

    @pyqtSlot()
    def launch_application(self):
        launch_app_thread = threading.Thread(target=self._launch_application)
        launch_app_thread.daemon = True
        launch_app_thread.start()

    def _launch_application(self):
        pass
