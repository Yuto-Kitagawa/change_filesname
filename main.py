#同じディレクトリにfilesファイルを作成し、その中に名前を変更したいファイルを入れてください

import glob
import os

# ファイル名
path = './files/*.jpg'
i = 1

flist = glob.glob(path)

# したい名前にする
name = "carousel"

for file in flist:
    # ファイル名
    os.rename(file, './files/' + name + str(i) + '.jpg')
    i += 1
