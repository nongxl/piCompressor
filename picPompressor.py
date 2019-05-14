#参考https://cloud.tencent.com/developer/article/1113251
import cv2 as cv
import os,math,sys

resize_path = 'outPic\compressed.jpg'
#outPath = 'outPic\compress.jpg'

#获得文件大小。get_doc_size 函数返回图片的文档大小，单位为 MB 。
def get_doc_size(path):
    try:
        size = os.path.getsize(path)
        return get_mb_size(size)
    except Exception as err:
        print(err)

def get_mb_size(bytes):
    bytes = float(bytes)
    mb = bytes / 1024 / 1024
    return mb

#删除文件。由于我们需要删除压缩过程中产生的中间文件，所以需要调用 delete_file 方法删除之。
def delete_file(path):
    if file_exist(path):
        os.remove(path)
        print('removed temp file:%s' % path)
    else:
        print('no such file:%s' % path)

def file_exist(path):
    return os.path.exists(path)

#其中 filesize 表示压缩目标值， path 表示原始文件路径， resize_path 表示压缩后存放路径， resize_rate 表示上述按比例压缩方法，定义如下：
def resize_rate(picPath, resize_path, fx, fy):
    image = read_image(picPath)
    im_resize = cv.resize(image, None, fx=fx, fy=fy)
    delete_file(resize_path)
    save_image(resize_path, im_resize)

def save_image(path, image):
    cv.imwrite(path, image)
    print('写入图片%s' % path)

def read_image(path):
    return cv.imread(path)


if len(sys.argv) < 3:
    print("Usage: python demo.py <picPath> <outSize>")
    print("Example: python demo.py d:\picture.jpeg 512k")
else:
    picPath = sys.argv[1]
    outSize = float(sys.argv[2])
    print('输入 %s %s' % (picPath,outSize))
    # 读取文件
    image = cv.imread(picPath)
    # 压缩文件
    size = get_doc_size(picPath)
    while size > outSize:
        #优化
        rate = math.ceil((size / outSize) * 10) / 10 + 0.1
        rate = math.sqrt(rate)
        rate = 1.0 / rate
        if file_exist(resize_path):
            resize_rate(resize_path, resize_path, rate, rate)
        else:
            resize_rate(picPath, resize_path, rate, rate)
        size = get_doc_size(resize_path)
        print('处理后的大小%s'%size)