# author liuyankai
# 2024年07月26日
from pyimzml.ImzMLParser import ImzMLParser

def read_imzml(file_path):

    imzml = ImzMLParser(file_path)
    # 读取所有质谱数据
    spectra = []
    for index, coord in enumerate(imzml.coordinates):
        mz, intensities = imzml.getspectrum(index)
        spectra.append((mz, intensities))

    # print(spectra)
    return spectra
