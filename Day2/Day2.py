import random

import pyxel


class LastWarClone:
    def __init__(self):
        # 1. ゲーム画面の初期化
        pyxel.init(120, 160, title="Pyxel Last War")

        # --- 追加部分：リソースの読み込み ---
        # 作成した画像や音のデータを読み込みます。
        # ファイル名が違う場合はここを変更してください。
        pyxel.load("my_resource.pyxres")
        # ---------------------------------

        # 2. 変数の準備
        self.player_x = 60  # プレイヤーの横位置
        self.count = 1  # 兵士の数
        self.objects = []  # 画面上の物体リスト [y, x, type, value]

        # 3. ゲーム開始
        pyxel.run(self.update, self.draw)

    def update(self):
        """計算や操作など、中身の動きを更新する処理 (変更なし)"""

        # 左右移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player_x = max(10, self.player_x - 2)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x = min(110, self.player_x + 2)

        # 30フレームごとに生成
        if pyxel.frame_count % 30 == 0:
            obj_type = random.choice(["gate_plus", "gate_minus", "enemy"])
            self.objects.append(
                [0, random.randint(20, 100), obj_type, random.randint(1, 10)]
            )

        # 移動と当たり判定
        for obj in self.objects[:]:
            obj[0] += 2
            if (
                abs(obj[0] - 140) < 8 and abs(obj[1] - self.player_x) < 12
            ):  # 判定を少し調整
                if obj[2] == "gate_plus":
                    self.count += obj[3]
                elif obj[2] == "gate_minus":
                    self.count = max(0, self.count - obj[3])
                elif obj[2] == "enemy":
                    self.count = max(0, self.count - 5)
                self.objects.remove(obj)
            elif obj[0] > 160:
                self.objects.remove(obj)

    def draw(self):
        """画面を描画する処理 (ここを大きく変更)"""

        pyxel.cls(7)  # 画面クリア

        # プレイヤー描画 (仮の円)
        pyxel.circ(self.player_x, 140, 5, 1)
        pyxel.text(self.player_x - 5, 130, f"x{self.count}", 0)

        # 全ての物体を描画
        for obj in self.objects:
            # obj の中身は [y座標, x座標, 種類, 数値]

            # --- 変更部分：画像表示 (blt関数) ---
            if obj[2] == "gate_plus":
                # 増加ゲートの画像を表示
                # blt(表示X, 表示Y, バンクNo, 画像U, 画像V, 幅, 高さ, 透過色)
                # x座標を少しずらして(obj[1]-8)中心を合わせています
                # 透明色の指定はしない
                pyxel.blt(obj[1] - 8, obj[0], 0, 0, 0, 16, 16)

            elif obj[2] == "gate_minus":
                # 減少ゲートの画像を表示 (U座標を16ずらす)
                pyxel.blt(obj[1] - 8, obj[0], 0, 16, 0, 16, 16)

            # --- 数値の重ね書き ---
            # 画像の上に数値を描画します（白い文字で見やすく）
            if "gate" in obj[2]:
                sign = "+" if "plus" in obj[2] else "-"
                # 画像の中心付近に文字が来るように調整
                pyxel.text(obj[1] - 6, obj[0] + 5, f"{sign}{obj[3]}", 7)


# プログラムの実行
LastWarClone()
