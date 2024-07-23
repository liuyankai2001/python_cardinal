# author liuyankai
# 2024年07月23日
import os


# 读取各种质谱成像数据
def readMSIData(file):
    base, ext = os.path.splitext(file)
    if (ext.lower() in ['ibd', 'imzml']):
        readImzML(file)
    elif (ext.lower() in ['img', 'dfr', 't2m']):
        readAnalyze(file)
    else:
        raise ValueError("can't recognize file extension: ", ext)


# 读取符合IMZML（Imaging Mass Spectrometry Markup Language）标准的数据文件
def readImzML(file, memory=False, check=False, range=None, resoluion=None, units=['ppm', 'mz'], max=1000, out='auto',
              parse_only=False, **kwargs):
    # 获取file文件路径和后缀
    base, ext = os.path.splitext(file)
    if 'name' in kwargs.keys():
        Deprecated(old='name', new='file')
    if 'folder' in kwargs.keys():
        Deprecated(old='folder', new='file')
    if ext != '':
        path = normalizePath(file, mustWork=True)
    else:
        if ('folder' in kwargs.keys()):
            path = normalizePath(file.path(kwargs['folder'], os.path.join(file, ".imzML")))
        else:
            path = normalizePath(os.path.join(file, ".imzML"))
    pass


def readAnalyze(file):
    pass


def getCardinalNChunks():
    pass


def Deprecated(old, new):
    pass


def normalizePath(file, mustWork, *args):
    pass
