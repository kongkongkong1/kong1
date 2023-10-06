from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import shutil
from cvimerge import *
import numpy as np
var1=True
var2=""
ttt = Tk()  


text_var = StringVar()
text_var.set("2x2.已启用")
default_number = IntVar(value=0)
default_number1 = IntVar(value=0)
xinzeng_var = StringVar()
xinzeng_var.set("")


#default_number2 = DoubleVar(value=1.0)浮点型 
default_number2 = StringVar(value=1.0)  
class ImageMerger:
    def __init__(self, zhuchuangkou):

        self.master = zhuchuangkou
        zhuchuangkou.title("图标批处理3.0 如有问题请联系QQ2383379923")
        #self.text_varbg = StringVar()
        #self.text_varicon = StringVar()

        self.y_pi = 0
        self.x_pi = 0
        self.suofang = 1
        self.entey1 = Entry(zhuchuangkou,textvariable = default_number)
        self.entey2 = Entry(zhuchuangkou,textvariable = default_number1)
        self.entey3 = Entry(zhuchuangkou,textvariable = default_number2) #只能text

        self.icon_button = Button(zhuchuangkou, text="请选泽目标文件夹", command=self.select_icon)
        self.bg_button = Button(zhuchuangkou, text="请选泽背景文件夹", command=self.select_bg)
        self.vivo2x_button = Button(zhuchuangkou, textvariable=text_var, command=self.fangda_2x)
        self.merge_button = Button(zhuchuangkou, text="开始合并", command=self.merge_images)
       # self.text_varicon = ''
        #self.bg_path = ''
        self.xpianyi_label = Label(zhuchuangkou, text="x偏移:")
        self.ypianyi_label = Label(zhuchuangkou, text="y偏移:")
        self.suofang_label = Label(zhuchuangkou, text="缩放:")

        self.bg_entry = Entry(zhuchuangkou,width=50)
        self.icon_entry = Entry(zhuchuangkou,width=50)
        self.vivo2x_label = Label(zhuchuangkou, text="2x2背景2倍图标")
       
#==========================================================以上初始化方法=============================================================================


#button  laber排列 
        # Display buttons and labels grid()结构管理器的参数 column 列  row行 padx x方向的外部填充 pady  y方向的外部填充   columnspan 合并单元格
        self.bg_button.grid(row=0, column=0, padx=10, pady=10)
        #self.bg_entry.insert(0, " " * 520) 
        self.bg_entry.grid(row=0, column=1, padx=10, pady=20)
        self.icon_button.grid(row=1, column=0, padx=10, pady=10)
        self.icon_entry.grid(row=1, column=1, padx=10, pady=20 )

        self.xpianyi_label.grid(row=2, column=0, padx=10, pady=10)
        self.entey1.grid(row=2, column=1, padx=10, pady=10)
        self.ypianyi_label.grid(row=2, column=2, padx=10, pady=10)
        self.entey2.grid(row=2, column=3, padx=10, pady=10)
        self.suofang_label.grid(row=2, column=4, padx=10, pady=10)
        self.entey3.grid(row=2, column=5, padx=10, pady=10)

        self.vivo2x_button.grid(row=3, column=0, padx=10, pady=10)
        self.vivo2x_label.grid(row=3 ,column=1, padx=10, pady=10)


        self.merge_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)




    def fangda_2x(self):
        global var1
        if var1==True :
           var1=False
           text_var.set("2x2.已关闭")
        else :
           var1=True
           text_var.set("2x2.已启用")
        # 方法：选择icon文件夹位置；名字绑定  
    def select_icon(self):
        self.text_varicon = filedialog.askdirectory()
        #self.icon_label.config(text=self.text_varicon)
        # 方法：选择目标背景图的文件夹位置；名字绑定
    def select_bg(self):
        selected_directory = filedialog.askdirectory()
        if selected_directory:
           self.bg_entry.insert(0,selected_directory)

        #print(self.text_varbg)
        #self.bg_label.config(text=self.text_varbg)
    def select_icon(self):
        selected_directory1 = filedialog.askdirectory()
        if selected_directory1:
           self.icon_entry.insert(0,selected_directory1)
      # 方法：合并
    def merge_images(self):

        global var2
        self.text_varicon = self.icon_entry.get()
        self.text_varbg = self.bg_entry.get()
        # 路径不存在
        if not self.text_varicon or not self.text_varbg:
            return
        dangqian = os.getcwd()
        print("工作路径",dangqian)
        print("输入的bg路径",self.text_varbg)
        path_dir = os.path.dirname(self.text_varbg)
        print("输入的bg路径上",path_dir)
        path_new = os.path.join(path_dir,"final")
        print("输出",path_new)
        try :
         os.mkdir(path_new) 
         print("建立文件夹")
        except  Exception as e :
         print(f"创建失败{str(e)}")
         pass


        for bgimagename in os.listdir(self.text_varbg):  #遍历bg目录下所有文件
         self.x_pi = int(self.entey1.get())
         self.y_pi = int(self.entey2.get())
         #self.entey3.insert(0,str(default_number2))
         self.suofang = float(self.entey3.get())
#背景文件夹循环处理
         if bgimagename.endswith('.jpg') or bgimagename.endswith('.jpeg') or bgimagename.endswith('.png'):
           # Create folder with image name
            bgfolder_name = os.path.splitext(bgimagename)[0]    #filename[0] 去掉后缀的名字
            bgfolder_path = os.path.join(self.text_varbg, bgfolder_name)   #文件夹的路径+名字
            if "1x2" in bgfolder_name or "240_480" in bgfolder_name :
              
              var2="_1x2"
            else : 
              pass
            if "2x1" in bgfolder_name or "480_240" in bgfolder_name :
              var2="_2x1"
            else : 
              pass
            if "2x2" in bgfolder_name or "480_480" in bgfolder_name :
              var2="_2x2"
            else : 
              pass
            print(xinzeng_var)
            if os.path.exists(bgfolder_path):
              pass  

            else:
              os.mkdir(bgfolder_path)       
   #中心文件夹循环处理

            for filename in os.listdir(self.text_varicon):    #遍历目标icon目录下所有文件print("")
                if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                        bg_image = Image.open(os.path.join(self.text_varbg, bgimagename)) #打开对应背景图
                        icon_image = Image.open(os.path.join(self.text_varicon, filename))#打开对应icoN
                        width, height = icon_image.size   
                        icon_image = icon_image.resize((int(width*self.suofang), int(height*self.suofang)))
                        if ("2x2" in bgimagename or "480_480" in bgimagename)  and var1 == True :
                          
                          icon_image = icon_image.resize((int(width*self.suofang*2), int(height*self.suofang*2)))
                          self.x_pi = 2*int(self.entey1.get())
                          self.y_pi = 2*int(self.entey2.get())
                        else:
                            pass
                          #先缩放倍数，在判断2x，再偏移
                        x = (bg_image.size[0]-icon_image.size[0]) // 2 + self.x_pi
                        y = (bg_image.size[1]-icon_image.size[1]) // 2 + self.y_pi

                        icon_image1 = Image.new("RGBA", bg_image.size) 
                        # icon_image1.paste(icon_image,(x,y),icon_image) 造成icon周围黑边且本身透明度变化
                        icon_image1.paste(icon_image,(x,y))
                        

                        bg_image=geshi(bg_image)
                        icon_image1=geshi(icon_image1)
                        bg_image=cv2.cvtColor(bg_image,cv2.COLOR_RGBA2BGRA)
                        icon_image1=cv2.cvtColor(icon_image1,cv2.COLOR_RGBA2BGRA)

                        result1 = overlay_with_transparency(bg_image, icon_image1, xmin = 0, ymin = 0,trans_percent = 1)
                        result12 = Image.fromarray(np.uint8(result1))
                        filename_list = filename.split(".png")
                        filename_list_without_extension = filename_list [0]
                        filename1 = "{}{}.png".format(filename_list_without_extension,var2)
                        aa_filename = os.path.join(bgfolder_path, filename1)   #保存路径和名字
                        result12.save(aa_filename) 
                        result12.close() and icon_image1.close() and  bg_image.close() 
                        print("已完成：",filename)
         var2 = ""
         shutil.move(bgfolder_path, path_new)    #移动到图标文件夹

# ttt = Tk() 
my_gui1111 = ImageMerger(ttt)   #mggui是图片合并类 的一个实例对象 参数是ttt
ttt.mainloop()