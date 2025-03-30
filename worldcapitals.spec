
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main_visual_final_installer_ready.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('countries_all_sample.json', '.'),
        ('backgroundsound.mp3', '.'),
        ('correct.wav', '.'),
        ('wrong.wav', '.'),
        ('mapa.webp', '.'),
        ('Virus DS logo_.png', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='WorldCapitals',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='app_icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='WorldCapitals'
)
