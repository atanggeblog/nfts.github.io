from colors import merges, generate
from imageData.subject import canvas, cattle

if __name__ == '__main__':
    stickers = [canvas, cattle]  # 设置模组已经内置mouse和cattle
    for amount in range(0, 10):  # 设置生成数量
        pixel = merges(stickers)
        generate(pixel, 'cattle-output/cattle' + str(amount))
