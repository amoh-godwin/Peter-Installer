# -*- mode: python -*-

block_cipher = None


a = Analysis(['H:\\GitHub\\Peter-Installer\\main.py'],
             pathex=['H:\\GitHub\\Peter-Installer'],
             binaries=[],
             datas=[("H:\\GitHub\\Peter-Installer\\installer.rcc", "."),
             ('H:\\GitHub\\Peter-Installer\\license.txt', '.')],
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
          icon="H:\\GitHub\\Peter-Installer\\UI\\images\\logo.ico",
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='installer')
