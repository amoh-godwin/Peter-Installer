# -*- mode: python -*-
import os

block_cipher = None


wd = os.path.realpath('.')
icon_path = os.path.join(wd, "UI", "images", "logo.ico")

a = Analysis(['main.py'],
             pathex=[wd],
             binaries=[],
             datas=[(os.path.join(wd, "installer.rcc"), "."),
             (os.path.join(wd, 'license.txt'), '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='installer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon=icon_path,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='installer')
