print('  |  1  2  3  4  5  6  7  8  9 ') 
print("--+---------------------------")
for y in range(1,10):
    str_line = ''
    str_line = str(y).rjust(2)+'|'
    for x in range(1,10):
        str_line = str_line + str(x * y).rjust(3)
    print(str_line)
#１，２行目が使用を満たせてないですが、一応動作するプログラムになったので提出します。

'''

縦軸をx　横軸をy　と変数にする
九九表のような結果を出す
変数　STR_LINE　=　””
STR_LINE　=　STR_LINE　+　(””　*　２)
for y = rang(1,10)

2行目
STR_LINE　=　””
STR_LINE　=

3行目から

cross_result = 0
for x in range(1, 10):
    str_line = ""
    str_line + str(x).rjust(2)
    str_line + "1"

for y in range(1, 10):
    cross_result = y * x
    str_line = str_line + str(cross).rjust(3)
print(str_line)
'''


