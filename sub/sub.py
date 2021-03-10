import os
import sys

helpstr = ('\n'
           'help\n'
           '本python脚本用来处理字幕格式问题\n'
           )


def extxt(i,old,new_str):
    ass_files = [name for name in os.listdir(i)
                 if (name.endswith('.ass') or name.endswith('.srt') or name.endswith('.ssa'))]
    for data in ass_files:
        old_data = i + '/' + data
        new = (i + '/new')
        isExists = os.path.exists(new)
        if not isExists:
            os.mkdir(new)
            print("目录不存在 创建新目录")
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
        fin=reader.replace(old,new_str)
        new_data = new + '/' + data
        nf = open(new_data, 'wt',encoding=unicode)
        nf.write(fin)
        print(old_data + "处理完毕")


if __name__ == "__main__":
    if sys.argv[1] == "-h" or sys.argv[1] == "--help" :
        print(helpstr)
        exit()
    print("输入需要替换的旧字符")
    old = input()
    print(("输入需要成的字符"))
    new = input()
    num = 0
    for i in sys.argv:
        if num != 0:
            extxt(i,old,new)
        num = num + 1