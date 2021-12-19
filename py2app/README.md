1、进入工程目录下面： 
    cd ProjectDirctory
2、生成 setup.py 文件： 
    py2applet --make-setup MyApplication.py
3、清空以前生成的编译文件： 
    rm -rf build dist
4、生成mac下的应用： 
    python setup.py py2app 
5、生成的应用在dist目录下面
