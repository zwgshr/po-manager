# 清理Odoo中多余语言包

```
du -d 1 -h
21M	    ./doc
640K	./setup
12K	    ./.github
32K	    ./.tx
112K	./debian
8.8M	./odoo
8.0K	./tmp
383M	./pobak
115M	./addons
527M	.
```

从github上下载odoo11源码并解压，可以看到占用527M空间
其中po文件的总大小达到了383M！而 odoo+addons 才占用了123.8M...
对于大多数开发人员和客户来说，最多只会用到两三个语言包。
**我们可以移走多余的语言包，等需要的时候再导入**

将 po_manager.py 放在项目的根目录，并根据自己的需要修改 WHITE_LIST

```
BAKDIR = 'pobak' #备份目录

WHITE_LIST = [
    'zh_CN.po',
    # 'zh_TW.po',
]   # 需要保留的 po 文件
```

使用`python po_manager.py`运行代码

代码功能：
- 将不在 WHITE_LIST 中的po文件移动到 pobak 文件夹下
- 将 WHITE_LIST 中的po文件从pobak中恢复到原来的位置


~~***pobak文件夹完全可以删除掉！***~~
~~***IDE打开速度提升300%***~~
~~***服务器上传代码速度提升300%***~~
~~***2333***~~