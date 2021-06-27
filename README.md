# dessin-scale

# Features
絵の練習のためのデッサンスケールのような画像を作るためのスクリプトです。
指定された画像の上に縦横に等分した赤い枠線を書いた画像を作成します。

# Requirement
* Pillow 8.2.0

# Installation

```bash
pip install git+https://github.com/emittam/dessin-scale
```

# Usage

## 基本的な使い方
```bash
dessin-scale -g [縦横のグリッド数] [画像のPath]
```
`[指定された画像の名前]_grid.[拡張子](例 a_grid.png)`という名前の画像が、指定された画像と同じディレクトリに作成されます。

`-g` を指定しない場合のデフォルト値は3です。


## 画像の拡縮
```bash
dessin-scale -g [縦横のグリッド数] -s [倍率(1より大きければ拡大、小さければ縮小)] [画像のPath]
```
`-s [倍率] (例 -s 1.5)` と指定することで元の画像を拡大、縮小して枠線を引いた画像を出力します。

## 枠線のみの画像の出力
```bash
dessin-scale -t -g [縦横のグリッド数] [画像のPath]
```
イラストソフトのレイヤーとして読み込むための画像を作成します。

`-t` と指定することで元の画像と同じサイズの透明画像の上に枠線を引いた画像を作成します。

`-s` と組み合わせるとサイズを変化させることができます。

## 出力先の指定
```bash
dessin-scale -g [縦横のグリッド数] -o [出力先のPath] [画像のPath]
```

# Author
* emittam
* dev@emittam.net

# License
"dessin-scale" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).