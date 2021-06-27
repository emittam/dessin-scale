#!/usr/bin/env python3
import argparse
import sys
import os
from PIL import Image, ImageDraw, UnidentifiedImageError


def parse_option():
    parser = argparse.ArgumentParser(description="グリッド模写用画像生成スクリプト")
    parser.add_argument('file_path', help='グリッド画像を作成する元ファイルのPath')
    parser.add_argument('-g', "--grid_size", help='グリッドの分割数', type=int, default=3)
    parser.add_argument('-s', '--scale', help='元画像を基準にした出力画像の拡大率 0.0から10.0まで0.01刻み', default=1.0, type=float)
    parser.add_argument('-t', '--transparent', help='出力画像の元画像を透明にしてグリッド線だけの画像を出力', action="store_true")
    parser.add_argument('-o', '--output_path', help='出力画像の出力先パス', default=None)

    return parser.parse_args()


def load_image_file(path: str) -> Image.Image:
    try:
        return Image.open(path)
    except FileNotFoundError:
        print('指定されたファイルが存在しません', file=sys.stderr)
        sys.exit(1)
    except UnidentifiedImageError:
        print('指定したファイルをロードできませんでした。破損しているか画像ファイルではない可能性があります。', file=sys.stderr)
        sys.exit(2)


def draw_grid(image: Image.Image, grid: int, scale: float, transparent: bool) -> Image.Image:
    scaled_width = round(image.width * scale)
    scaled_height = round(image.height * scale)
    if transparent:
        draw_image = Image.new('RGBA', (scaled_width, scaled_height), 0)
        draw_image.putalpha(0)
    else:
        if image.width != scaled_width or image.height != scaled_height:
            draw_image = image.resize((scaled_width, scaled_height))
        else:
            draw_image = image.copy()

    grid_width = scaled_width // grid
    grid_height = scaled_height // grid

    draw = ImageDraw.Draw(draw_image)
    for i in range(1, grid):
        draw.line([(grid_width * i, 0), (grid_width * i, scaled_height)], fill='red', width=1)
        draw.line([(0, grid_height * i), (scaled_width, grid_height * i)], fill='red', width=1)

    return draw_image


def get_save_file_path(out_path: str, origin_path: str):
    if out_path is None:
        ext_split = os.path.splitext(os.path.basename(origin_path))
        out_path = os.path.dirname(os.path.abspath(origin_path)) + '/' + ext_split[0] + '_grid' + ext_split[1]
    return out_path


def save_grid_image(image: Image.Image, out_path: str):
    try:
        image.save(out_path)
    except ValueError:
        print("ファイル出力形式エラー", file=sys.stderr)
        sys.exit(3)
    except OSError:
        print("ファイル作成エラー", file=sys.stderr)
        sys.exit(4)

def main():
    args = parse_option()
    img = load_image_file(args.file_path)
    img = draw_grid(img, args.grid_size, args.scale, args.transparent)
    save_grid_image(img, get_save_file_path(args.output_path, args.file_path))


if __name__ == '__main__':
    main()