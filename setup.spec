# -*- mode: python -*-

block_cipher = None


a = Analysis(['H:\\GitHub\\Peter-Installer\\setup.py'],
             pathex=['H:\\GitHub\\Peter-Installer'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          exclude_binaries=True,
          name='Setup',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon="H:\\GitHub\\Peter-Installer\\UI\\images\\logo.ico",
          console=False )

coll = COLLECT(exe,
               name='Setup')

