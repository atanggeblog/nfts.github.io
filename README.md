# Master-art-punk
##### Make your master artistic punk avatar through machine learning world famous paintings.
##### 通过机器学习世界名画制作属于你的大师级艺术朋克头像
##### Nowadays, NFT is becoming popular in the world, and various trading platforms like opensea have developed rapidly, and cryptopunks have even sold tens of millions of dollars.
##### 如今，NFT在世界上正流行起来，各种交易平台像opensea等，快速发展了起来，像cryptopunks甚至卖出了上千万美金。
##### This project will help you to know in general how these NFT pictures are made, and try to make your own NFT.
![punk1](https://raw.fastgit.org/philipjhc/Master-art-punk/main/Master-art-punk/cover_photo/example.png)
![punk2](https://raw.fastgit.org/philipjhc/Master-art-punk/main/Master-art-punk/cover_photo/example2.png)
##### 这个项目将有助于你大体知道这些NFT的图片是如何制作的，并尝试制作自己的NFT。
##### This project uses the K-Means algorithm to acquire and learn the color matching of world famous paintings in the data set, and imitate its color style to color the model.
##### 本项目运用了K-Means算法对数据集中世界名画的色彩搭配进行获取和学习，并模仿其色彩风格给模型上色,展示如下：
![NFT1](https://raw.fastgit.org/philipjhc/Master-art-punk/main/Master-art-punk/cover_photo/NFT1.png)
![NFT1](https://raw.fastgit.org/philipjhc/Master-art-punk/main/Master-art-punk/cover_photo/NFT4.png)
## 使用说明：
### 1.安装要求：
#### 1.更改settings.py的第8行，填入你自己的图片训练集路径，例如，打开./data/monet看到图片类似。（类似方法制作数据集，默认png格式）
#### 2.安装numpy和pypng:pip install numpy / pip install pypng
### 2.训练：
#### 1.python model.py / 运行 model.py （等待时间跟图片数目有关）
#### 2.运行后，可发现colordistance.csv更新（需修改名字在setting.py的color_distance_filepath修改）
#### 3.接着打开app.py 第12行选择模组类型（内置模型可在imageData下的stickers.py，subject.py中查看），第10行设置生成数量，第68行设置输出文件路径。
#### 4.app.py
#### 5.output对应文件夹下中有已生成的朋克头像。（最好选择一个作家的风格，例如，我选择了莫奈）