# 同じディレクトリにbeforeファイルを作成し、
# その中に名前を変更したいファイルを入れてください

import glob
import os
import shutil

# ファイル拡張子
# 変更前
change_before_file_type = "png"

# 変更後
change_after_file_type = "png"

# 変更前ファイル名(正規表現)
change_before_file_name_regex = "*"

# 変更後ファイル名(最後にインデックスが入ります)
change_after_file_name = "Azure-構築-"

## afterディレクトリ(変更後ディレクトリ)がなければ作成
os.makedirs("./after", exist_ok=True)

for p in glob.glob('after/*', recursive=True):
    if os.path.isfile(p):
        os.remove(p)


path = './before/' + change_before_file_name_regex + '.' + change_before_file_type
i = 1

flist = sorted(glob.glob(path),key=os.path.getmtime,reverse=False)

for file in flist:
    os.rename(file, './after/' + change_after_file_name + str(i) + '.' + change_after_file_type)
    i += 1
