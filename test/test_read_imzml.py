# author liuyankai
# 2024年07月25日
from pyimzml.ImzMLParser import ImzMLParser

# 创建一个 ImzMLParser 对象
imzml_file = '../file/file14a05ee78de.imzML'
p = ImzMLParser(imzml_file)
print(p.intensityLengths)
# 获取图像尺寸
# x_size, y_size = p.shape
# print("Image size:", x_size, "x", y_size)
#
# # 获取所有质荷比（m/z）值
# # mz_list = p.getspectrum()
#
# # 打印前五个 m/z 值
# print("First five m/z values:", mz_list[:5])
#
# # 访问特定位置的光谱数据
# x = 50
# y = 50
# intensities, mz = p.getspectrum(x, y)
# print(f"Spectrum at ({x}, {y})")
# print("m/z:", mz)
# print("Intensities:", intensities)