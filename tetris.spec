# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['tetris.py'],
             pathex=['I:\\projects\\Tetris'],
             binaries=[],
             datas=[('asteroid.ico', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [('bg.png','I:\\projects\\Tetris\\bg.png', "DATA"),
    ('bg2.png','I:\\projects\\Tetris\\bg2.png', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Tetris',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=None,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='space.ico')