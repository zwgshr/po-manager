import os
import platform
import shutil

BAKDIR = 'pobak' #备份目录

WHITE_LIST = [
    'zh_CN.po',
    # 'zh_TW.po',
]  # 需要保留的 po 文件

root_path = os.getcwd()


def get_all_po():
    if platform.system() == 'Linux':
        # output = os.popen('find ./ -name "*.po" |grep i18n')
        output = os.popen('find {} -name "*.po" |grep i18n'.format(root_path))
        allfile = output.read().split('\n')
        return allfile
    else:
        addons_path = []

        for name in os.listdir(root_path):
            if name.startswith('addons'):
                addons_path.append(os.path.join(root_path, name))

        for name in os.listdir('{}/odoo'.format(root_path)):
            if name.startswith('addons'):
                addons_path.append(os.path.join(root_path, 'odoo', name))

        print(addons_path)

        res = []
        for apath in addons_path:
            for dirpath, dirnames, filenames in os.walk(apath):
                for dirname in dirnames:
                    i18n = os.path.join(dirpath, dirname, 'i18n')
                    if os.path.isdir(i18n):
                        for x in os.listdir(i18n):
                            if x.endswith('.po'):
                                res.append(os.path.join(i18n, x))

        return res


def backup():
    files = get_all_po()
    if not os.path.isdir(BAKDIR):
        os.mkdir(BAKDIR)

    for file in files:
        inwhite = False
        for white in WHITE_LIST:
            if file.endswith(white):
                inwhite = True

        if inwhite: continue
        if not file: continue

        filename = file.replace(root_path, '')[1:]
        dirname = os.path.dirname(filename)

        if not os.path.isdir(os.path.join(BAKDIR, dirname)):
            os.makedirs(os.path.join(BAKDIR, dirname))

        print(file)
        shutil.move(file, os.path.join(BAKDIR, '{}.bak'.format(filename)))


def get_all_pobak():
    if platform.system() == 'Linux':
        output = os.popen('find {} -name "*.po.bak" |grep i18n'.format(root_path))
        allfile = output.read().split('\n')
        return allfile
    else:
        res = []
        for dirpath, dirnames, filenames in os.walk(os.path.join(root_path, BAKDIR)):
            for dirname in dirnames:
                i18n = os.path.join(dirpath, dirname, 'i18n')
                if os.path.isdir(i18n):
                    xx = os.listdir(i18n)
                    for x in xx:
                        if x.endswith('.po.bak'):
                            res.append(os.path.join(i18n, x))
        return res


def restore():
    files = get_all_pobak()
    for file in files:
        inwhite = False
        for white in WHITE_LIST:
            if file.endswith('{}.bak'.format(white)):
                inwhite = True
        if not inwhite: continue

        filename = file.replace(os.path.join(root_path, BAKDIR), '')[1:]

        print(filename)
        shutil.move(file, filename[:-4])


if __name__ == '__main__':
    backup()
    restore()
