# Master-art-punk
 Make your master artistic punk avatar through machine learning world famous paintings
 通过机器学习世界名画制作属于你的大师级艺术朋克头像
 
## 使用说明：
>1.安装要求：
>> 1.更改Get_color_model.py的第17行，填入你自己的图片训练集路径，例如，打开./data/monet看到图片类似。（类似方法制作数据集，默认png格式）
>> 2.安装numpy和pypng:pip install numpy / pip install pypng
>2.训练：
>> 1.python Get_color_model.py / 运行 Get_color_model.py （等待时间跟图片数目有关）
>> 2.运行后，可发现colordistance.csv更新（需修改名字在Get_color_model.py的第16行修改）
>> 3.接着打开Generate-crypto-punk.py 第65行选择模组类型（内置模型可在Image_stickers.py，Image_subject.py中查看），第66行设置生成数量，第68行设置输出文件路径。
>> 4.运行Generate-crypto-punk.py
>> 5.output中有已生成的朋克头像。（最好选择一个作家的风格，例如，我选择了莫奈）