# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[r'C:\Users\ali\PycharmProjects\examifier'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('imageedit1.jpg',r'D:\coding\imageedit1.jpg', "DATA"),('imageedit2.jpg',r'D:\coding\imageedit2.jpg', "DATA"),('imageedit5.jpg',r'D:\coding\imageedit5.jpg', "DATA"),('coveryear9.pdf',r'D:\coding\coveryear9.pdf', "DATA"),('coverolevel.pdf',r'D:\coding\coverolevel.pdf', "DATA"),('coveraslevel.pdf',r'D:\coding\coveraslevel.pdf', "DATA"),('covera2level.pdf',r'D:\coding\covera2level.pdf', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Name of your program',
          debug=False,
          strip=False,
          upx=True,
          console=False)
