# piCompressor 

将jpeg图片压缩到指定容量大小

基于python3.x和opencv

首先安装依赖包 
pip3 install opencv-python
用法
python3 piCompressor.py 【图片位置】 【压缩目标大小】
如：
    python3 piCompressor.py compress.jpg 512k
输出结果在 outPic\compressed.jpg

算法来自 https://cloud.tencent.com/developer/article/1113251 感谢。


