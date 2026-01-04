import random

import pyxel


class LastWarClone:
    def __init__(self):
        pyxel.init(120, 160, title="Pyxel Last War")
        pyxel.load("../my_resource.pyxres")  # リソースの読み込み

        self.player_x = 60
        self.count = 1
        self.objects = []  # [y, x, type, value]
        pyxel.run(self.update, self.draw)

    def update(self):
        # 左右移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(10, self.player_x - 2)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(110, self.player_x + 2)

        # 30フレームごとに生成
        if pyxel.frame_count % 5 == 0:
            # 修正：種類を"gate_plus"に限定し、数値を1に固定
            self.objects.append([0, 110, "gate_plus", 1])

        # 移動と当たり判定
        for obj in self.objects[:]:
            obj[0] += 2
            if abs(obj[0] - 140) < 8 and abs(obj[1] - self.player_x) < 12:
                # 修正：プラスゲートの加算処理のみ実行
                self.count += obj[3]
                self.objects.remove(obj)
            elif obj[0] > 160:
                self.objects.remove(obj)

    def draw(self):
        pyxel.cls(7)
        pyxel.circ(self.player_x, 140, 5, 1)
        pyxel.text(self.player_x - 5, 130, f"x{self.count}", 0)

        for obj in self.objects:
            # 修正：プラスゲートの画像（座標 0, 0）のみを表示
            pyxel.blt(obj[1] - 8, obj[0], 0, 0, 0, 16, 16)


LastWarClone()
