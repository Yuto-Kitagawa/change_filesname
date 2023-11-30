# 同じディレクトリにfilesファイルを作成し、その中に名前を変更したいファイルを入れてください

import glob
import os

# ファイル拡張子
# 変更前
change_before_file_type = "png"

# 変更後
change_after_file_type = "png"

# 変更前ファイル名(正規表現)
change_before_file_name_regex = "*"

# 変更後ファイル名(最後にインデックスが入ります)
change_after_file_name = "Azure-構築-"


path = './files/' + change_before_file_name_regex + '.' + change_before_file_type
i = 1

flist = glob.glob(path)

for file in flist:
    os.rename(file, './files/' + change_after_file_name + str(i) + '.' + change_after_file_type)
    i += 1
