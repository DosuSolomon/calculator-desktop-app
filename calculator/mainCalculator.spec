# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mainCalculator.py'],
             pathex=['C:\\Users\\lastbourne\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\lastbourne\\PycharmProjects\\PYTHON\\myCalculator\\calculator'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mainCalculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
