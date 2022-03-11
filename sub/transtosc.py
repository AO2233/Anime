import argparse
import os
import opencc
from tqdm import tqdm

def t2s(i, use_new=0, mode='t2s'):
    ass_files = [name for name in os.listdir(i)
                 if (name.endswith('.ass') or name.endswith('.srt') or name.endswith('.ssa'))]
    bar = tqdm(range(len(ass_files)))
    for data in ass_files:
        old_data = i + '/' + data
        if use_new==1:
            new = (i + '/new')
            isExists = os.path.exists(new)
            if not isExists:
                os.mkdir(new)
        else:
            new = i
        try:
            f = open(old_data, 'rt', encoding='utf8')
            unicode = 'utf8'
            reader = f.read()
        except UnicodeDecodeError:
            try:
                f = open(old_data, 'rt', encoding='gbk')
                unicode = 'gbk'
                reader = f.read()
            except UnicodeDecodeError:
                f = open(old_data, 'rt', encoding='utf16')
                unicode = 'utf16'
                reader = f.read()
        tem = opencc.OpenCC(mode)
        new_data = new + '/' + data
        nf = open(new_data, 'wt', encoding=unicode)
        nf.write(tem.convert(reader))
        bar.update(1)
        bar.set_description("正在处理 %s" % data)


if __name__ == "__main__":
    parse = argparse.ArgumentParser("opencc 繁体转简体 简体转繁体", epilog='支持UTF-8,UTF-16,GBK编码')
    parse.add_argument('-p', nargs='*', default='', help="文件路径")
    parse.add_argument('-R', default=False,type=int,help="是否替换 0 or 1")
    parse.add_argument('-m', default='t2s', help="'t2s 繁转简 s2t 简转繁'")
    parse.format_help()
    arg = parse.parse_args()
    dic_all = []
    for i in arg.p:
        for root, sub, file in os.walk(i):
            dic_all.append(root)
    for i in dic_all:
        t2s(i, arg.R, arg.m)
