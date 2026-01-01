import pyxel

# 画像を表示するだけの基本的な処理

# 表示画面のサイズを設定
WINDOW_H = 120
WINDOW_W = 160
# 猫画像のサイズを設定
CAT_H = 16
CAT_W = 16

"""
基本的にはPythonスクリプト内では大きく4つの役割に分けてコードを記述します
 ※ラップして記述することが推奨されている
    ・ 初期化
    ・ フレームの更新処理(update)
    ・ 描画処理(draw)
    ・ アプリケーションの実行(run)
"""


class App:
    # コンストラクタ
    # 表示画面の設定と画像のロード(読み込める画像の数は最大3つ)
    def __init__(self):
        pyxel.init(WINDOW_W, WINDOW_H, title="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/cat_16x16.png")

        # Pyxel アプリケーションの実行
        # →フレーム更新処理を行うupdate関数と、描画処理を行うdraw関数を指定
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        # 表示画面の引数の値(カラーキー)でクリアする(0は黒)
        pyxel.cls(10)
        # pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        """
            blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])
            イメージバンクimg(0-2) の (u, v) からサイズ (w, h) の領域を (x, y) にコピーします。
            w、hそれぞれに負の値を設定すると水平、垂直方向に反転します。
            colkeyに色を指定すると透明色として扱われます。
            rotate(度:Degree)、scale(1.0=100%)、またはその両方を指定すると対応する変換が適用されます。
        """
        # 表示画面を基準に(x,y)=(60,65)(引数1,2)の位置に画像を配置
        # また、セットする画像は0番目の画像(引数3)の原点(0,0)(引数4,5)から幅38,高さ16(引数6,7)を切り取ったものを配置する
        pyxel.blt(60, 65, 0, 0, 0, 38, 16)
        # 仮に CAT_W を -CAT_W にするとy軸を基準に画像が反転する
        pyxel.blt(75, 45, 1, 0, 0, CAT_W, CAT_H, 5)


App()
