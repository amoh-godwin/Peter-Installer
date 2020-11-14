# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:16:42 2019

@author: Ampofo
"""
import sys
import os
import re
from PyQt5.QtCore import QCoreApplication, QSettings, QResource
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtQml import QQmlApplicationEngine

from connector import Connector

QCoreApplication.setOrganizationName("Deuteronomy Works")
QCoreApplication.setApplicationName("Peter Server | Installer")
settings = QSettings()

QResource.registerResource("installer.rcc")

os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Universal'
app = QGuiApplication(sys.argv)
app.setWindowIcon(QIcon("UI/images/logo.png"))

connect = Connector()

with open('UI/license.txt', mode='r') as lic:
    license_text = lic.read()

engine = QQmlApplicationEngine()
engine.load("UI/qml/main.qml")
engine.rootObjects()[0].setProperty('connector', connect)
engine.rootObjects()[0].setProperty('license_text', license_text)
engine.quit.connect(app.quit)

sys.exit(app.exec_())
