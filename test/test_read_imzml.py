# author liuyankai
# 2024年07月25日
from pyimzml.ImzMLParser import ImzMLParser

def read_imzml(file_path):

    imzml = ImzMLParser(file_path)
    # 读取所有质谱数据
    spectra = []
    for index, coord in enumerate(imzml.coordinates):
        mz, intensities = imzml.getspectrum(index)
        spectra.append((mz, intensities))
    # 文件路径
    metadata = imzml.filename
    polarity = imzml.polarity
    print(polarity)
    return spectra


if __name__ == '__main__':
    im = read_imzml('../test_data/colon.imzML')