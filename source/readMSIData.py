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
              parse_only=False):
    pass


def readAnalyze(file):
    pass


def getCardinalNChunks():
    pass
