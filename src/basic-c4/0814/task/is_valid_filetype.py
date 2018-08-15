import re

pattern = r"\.txt$"
file_name = str(input("テキスト形式のファイル名を入力してください>> "))
if re.search(pattern, file_name):
    print(file_name, "は、拡張子が" '.txt' "のテキストファイルです。")
else:
    print(file_name, "は、拡張子が" '.txt' "のテキストファイルではありません。")
