import opencc
import os
import sys
from tqdm import tqdm

helpstr = ('\n'
           'help\n'
           '本python脚本用来处理字幕繁简转换问题\n'
           '使用示例：\n'
           'python3 transtosc.py \'放有字幕的path_1\' \'放有字幕的path_2\'\n'
           '本脚本只读取 srt ass ssa 后缀文件\n'
           '转换完毕的文件会放置在下级目录的new之中\n'
           'PS:\n'
           '本脚本只读取一层目录 AND 只支持 UTF-8,GBK等编码\n')


def t2s(i):
    ass_files = [name for name in os.listdir(i)
                 if (name.endswith('.ass') or name.endswith('.srt') or name.endswith('.ssa'))]
    bar = tqdm(range(len(ass_files)))
    for data in ass_files:
        old_data = i + '/' + data
        new = (i + '/new')
        isExists = os.path.exists(new)
        if not isExists:
            os.mkdir(new)

        try:
            f = open(old_data, 'rt',encoding='utf8')
            unicode='utf8'
            reader = f.read()
        except UnicodeDecodeError:
            try:
                f = open(old_data, 'rt', encoding='gbk')
                unicode='gbk'
                reader = f.read()
            except UnicodeDecodeError:
                f = open(old_data, 'rt', encoding='utf16')
                unicode='utf16'
                reader = f.read()
        tem = opencc.OpenCC('t2s')
        new_data = new + '/' + data
        nf = open(new_data, 'wt',encoding=unicode)
        nf.write(tem.convert(reader))
        bar.update(1)
        bar.set_description("正在处理 %s" % data)


if __name__ == "__main__":
    if sys.argv[1] == "-h" or sys.argv[1] == "--help" :
        print(helpstr)
        exit()

    for i in tqdm(sys.argv[1:]):
            t2s(i)
