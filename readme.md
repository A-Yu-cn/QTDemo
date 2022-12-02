
# 一个小的熟悉PyQT的练习
学习的教程网址为https://maicss.gitbook.io/pyqt-chinese-tutoral/
大致熟悉一下就ok啦

安装环境主要：
1. pip install PyQt5 -i https://pypi.douban.com/simple
2. pip install PyQt5-tools -i https://pypi.douban.com/simple
3. 环境变量配置： QT_QPA_PLATFORM_PLUGIN_PATH => D:\language\python38\Lib\site-packages\PyQt5\Qt5\plugins（变量值根据安装位置来定）
4. 环境变量：path=>D:\language\python38\Lib\site-packages\PyQt5\Qt5\plugins（变量值根据安装位置来定）
5. pycharm 设置=>工具=>外部工具=>添加QtDesigner和PyGUI
* 程序：D:\language\python38\Lib\site-packages\qt5_applications\Qt\bin\designer.exe（看自己的designer.exe 文件的位置）
* 工作目录：$ProjectFileDir$
* 程序：python.exe 的文件位置
* 实参：$FileName$ -o $FileNameWithoutExtension$.py
* 工作目录：$ProjectFileDir$

安装教程 https://blog.csdn.net/m0_53324526/article/details/126612220