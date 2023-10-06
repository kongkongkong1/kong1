import cv2
import numpy as np
# fgimg = Image.open('F:/图标测试\\测试2\\3/58同城.png')
# bgimg = Image.open('F:/图标测试\测试2/3/底/第三方背景12x2.png') 
import PIL 
from PIL import Image
import numpy 
import os





# 将PIL图片转换为OpenCV格式
def geshi(imm):
    imm = cv2.cvtColor(numpy.array(imm), cv2.COLOR_RGBA2BGRA)
    return imm


def img_float32(img):  
    return img.copy() if img.dtype != 'uint8' else (img/255.).astype('float32')   #mg_float32函数获取一个输入图像img，如果其数据类型不是uint8，则返回该图像的副本。如果数据类型是uint8，它会将所有像素值除以255，从而将图像转换为float32格式。

def over(fgimg, bgimg):
    fgimg, bgimg = img_float32(fgimg),img_float32(bgimg)
    (fb,fg,fr,fa),(bb,bg,br,ba) = cv2.split(fgimg),cv2.split(bgimg) #提取rgba
    color_fg, color_bg = cv2.merge((fb,fg,fr)), cv2.merge((bb,bg,br))  #合并rgb 
    alpha_fg, alpha_bg = np.expand_dims(fa, axis=-1), np.expand_dims(ba, axis=-1)  #np.expand_dims  扩散数组形状

    color_fg[fa==0]=[0,0,0]
    color_bg[ba==0]=[0,0,0]
    #color_fg和color_bg分别是fgmg和bgmg的颜色通道
    a = fa + ba * (1-fa)  #最终的alpha通道
    a[a==0]=np.NaN
    color_over = (color_fg * alpha_fg + color_bg * alpha_bg * (1-alpha_fg)) / np.expand_dims(a, axis=-1)
    color_over = np.clip(color_over,0,1)
    color_over[a==0] = [0,0,0]

    result_float32 = np.append(color_over, np.expand_dims(a, axis=-1), axis = -1)
    return (result_float32*255).astype('uint8')
#color_over是alpha合成后的结果颜色。然后，该函数将生成的颜色值剪裁到[0，1]范围，并将透明像素的颜色设置为黑色。
#最后，over函数将color_over和a通道连接起来，创建一个四通道图像，将像素值缩放回[0255]范围，并返回结果图像
def overlay_with_transparency(bgimg, fgimg, xmin = 0, ymin = 0,trans_percent = 1):
    '''
    bgimg: a 4 channel image, use as background
    fgimg: a 4 channel image, use as foreground
    xmin, ymin: a corrdinate in bgimg. from where the fgimg will be put  放置位置
    trans_percent: transparency of fgimg. [0.0,1.0]  背景图的透明度
    '''
    #we assume all the input image has 4 channels  假定所有都是4通道
    assert(bgimg.shape[-1] == 4 and fgimg.shape[-1] == 4)     #shape函数是numpy.core.fromnumeric的函数 功能是读取矩阵长度
    #1.assert函数 断言函数assert 表达式: 当表达式为真时,程序继续往下执行,只是判断,不做任何处理; 当表达式为假时,抛出AssertionError错误,并将 [参数] 输出
    fgimg = fgimg.copy()
    roi = bgimg[ymin:ymin+fgimg.shape[0], xmin:xmin+fgimg.shape[1]].copy()

    b,g,r,a = cv2.split(fgimg)

    fgimg = cv2.merge((b,g,r,(a*trans_percent).astype(fgimg.dtype)))

    roi_over = over(fgimg,roi)  #调用over函数 底层背景用roi替换了

    result = bgimg.copy()
    result[ymin:ymin+fgimg.shape[0], xmin:xmin+fgimg.shape[1]] = roi_over
    return result
#overlay_with_transparency函数使用over函数来计算bgimg的ROI上降低的不透明度fgimg的alpha合成。然后，它返回bgimg的副本，其中alpha合成的fgimg覆盖在ROI的顶部。

if __name__ == '__main__':
    print(111)

