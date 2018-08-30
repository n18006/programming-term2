
#!/usr/bin/env python3

import cgi
import cgitb
import os.path
import html

# ブラウザでのデバッグを有効にする
cgitb.enable()

# 全体の表示
FILE_LOG = "test-record.txt"


# HTMLを画面に出力する
def print_html(style, sum_score, ave_score, table_list):
    # ヘッダを出力
    print("Content-Type: text/html; charset=utf-8")
    print("")
    # HTMLを出力
    print("""
<html>
<head><meta charset="utf-8">
<title>成績表一覧</title>
<style>
{0}
</style>
</head>
<body>
<h1>成績表一覧</h1>
<div><form>
名前: <input type="text" name="name" size="20">
点数: <input type="text" name="score" size="12">
<input type="submit" value="追加">
<input type="hidden" name="mode" value="write">
</form></div><hr>
<p>合計点 {1}</p>
<p>平均点 {2}</p>
<table>
<tr><th>名前</th><th>点数</th><th>差</th></tr>
{3}
</table>
</body>
</html>
    """.format(style, sum_score, ave_score, table_list))



###途中までを一先ず提出###





#メイン処理
def main():



if __name__ == "__main__":
main()
