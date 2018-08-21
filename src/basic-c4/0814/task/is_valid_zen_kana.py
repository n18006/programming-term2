import re

input_str = input("全角カナの文字を入力してください>>")
pattern = r"[ァ-ン]"
zen_kana = re.match(pattern, input_str)
print(zen_kana)
if not zen_kana is None:
    print(input_str,"は、全角カタカナである")
else:
    print(input_str,"は全角カタカナではない")
