# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:16:42 2019

@author: Ampofo
"""
import sys
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

from install import install_win

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Peter")
settings = QSettings()

app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon(""))

win_installer = install_win.WinInstall()

engine = QQmlApplicationEngine()
engine.rootContext().setContextProperty()
engine.load("UI/qml/main.qml")
engine.quit.connect(app.quit)

sys.exit(app.exec_())
