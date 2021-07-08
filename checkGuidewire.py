import os, sys
import pandas as pd
import numpy as np
from PIL import Image

path = r'C:\Users\Mimi\Documents\aigt\DeepLearnLive\Datasets\Unet data'
fileList = os.listdir(path)

allGuidewire = []
allNonGuidewire = []
files = []

for item in fileList:
	location = os.path.join(path,item, 'Ultrasound')
	dirs = os.listdir(location)

	ult = []
	seg = []
	guidewire = 0
	nonguide = 0

	for file in dirs:
		if 'ultrasound' in file:
			ult.append(file)
		else:
			imgPath = os.path.join(location, file)
			image = Image.open(imgPath)
			data = np.asarray_chkfinite(image)
			present = np.max(data)
			if present == 0:
				nonguide += 1
			else:
				guidewire += 1
			seg.append(file)

	files.append(item)
	allGuidewire.append(guidewire)
	allNonGuidewire.append(nonguide)

data = {'FileName': files,
		'NumGuidewireFrame': allGuidewire,
		'NumNonGuidewireFrame': allNonGuidewire}

df = pd.DataFrame(data, columns = ['FileName', 'NumGuidewireFrame', 'NumNonGuidewireFrame'])

df.to_csv(path + '.csv', index=True, header=True)
# data = {'FileName': ult,
# 	'Guidewire_Segmentation': seg}

# df = pd.DataFrame(data, columns = ["FileName", "Guidewire_Segmentation"])

# # spie = r'c:\Users\Mimi\Desktop\SPIE'
# out = r'C:\Users\Mimi\Documents\aigt\DeepLearnLive\Datasets\Unet data'
# # exportPath = os.path.join(spie, item)
# exportPath = os.path.join(out, item)
# df.to_csv(exportPath + '_Ultrasound_Labels.csv', index = True, header = True)

# path = r'C:\Users\Mimi\Desktop\SPIE\Guidewire_segmentation'

# dirs = os.listdir(path)

# ult = []
# seg = []
# guidewire = []

# for file in dirs:
# 		if 'ultrasound' in file:
# 				ult.append(file)
# 		else:
# 				imgPath = os.path.join(path,file)
# 				image = Image.open(imgPath)
# 				data = np.asarray_chkfinite(image)
# 				present = np.max(data)
# 				guidewire.append(present)
# 				seg.append(file)

# print(guidewire)

# # data = {'FileName': ult,
# # 		'Guidewire_Segmentation': seg}

# # df = pd.DataFrame(data, columns = ["FileName", "Guidewire_Segmentation"])

# # # spie = r'c:\Users\Mimi\Desktop\SPIE'
# # out = r'C:\Users\Mimi\Documents\aigt\DeepLearnLive\Datasets\Unet data'
# # # exportPath = os.path.join(spie, item)
# # exportPath = os.path.join(out, item)
# # df.to_csv(exportPath + '_Ultrasound_Labels.csv', index = True, header = True)