# author liuyankai
# 2024年07月28日
from pyimzml.ImzMLParser import ImzMLParser
class IMZData:
    def __init__(self,file_path):
        imzml = ImzMLParser(file_path)
        # 读取所有质谱数据
        spectra = []
        for index, coord in enumerate(imzml.coordinates):
            mz, intensities = imzml.getspectrum(index)
            spectra.append((mz, intensities))

