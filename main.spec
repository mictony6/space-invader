# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas += [('./images/bullet.png','C:/Users/Aira/space invader/images/bullet.png','Data'),('./images/icon.png','C:/Users/Aira/space invader/images/icon.png','Data'),('./images/player.png','C:/Users/Aira/space invader/images/player.png','Data'),('./images/background.png','C:/Users/Aira/space invader/images/background.png','Data'),('./images/enemy.png','C:/Users/Aira/space invader/images/enemy.png','Data'),('./sounds/shoo.wav','C:/Users/Aira/space invader/sounds/shoo.wav','Data'),('./sounds/space.wav','C:/Users/Aira/space invader/sounds/space.wav','Data'),('./sounds/hit.wav','C:/Users/Aira/space invader/sounds/hit.wav','Data'),('./segoe.ttf','C:/Users/Aira/space invader/segoe.ttf','Data')]
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon = './images/icon.ico'
)
