#クラスの定義
class HumanName:
    '''人を表すクラス'''
    def setName(self, name):
        '''名前を設定するめそっど'''
        self.name - name

    def getName(self):
        '''名前を習得するメソッド'''
        return self.name

# インスタンをを作成
taro = HumanName()
taro.setName("Taro")
print(taro.getName())

jiro = HumanName()
jiro.setName("jiro")
print(jiro.getName())

print(jiro.name)
