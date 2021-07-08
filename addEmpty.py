import os, sys
import pandas as pd
import numpy as np
from PIL import Image

path = r'C:\Users\Mimi\Documents\aigt\DeepLearnLive\Datasets\Unet data'
fileList = os.listdir(path)

for item in fileList:
        location = os.path.join(path,item, 'Ultrasound')
        dirs = os.listdir(location)

        ult = []
        seg = []
        emp = []

        for file in dirs:
                if 'ultrasound' in file:
                        ult.append(file)
                        imgPath = os.path.join(location, file)
                        image = Image.open(imgPath)
                        data = np.asarray_chkfinite(image)
                        cropped = data[100:400, 0:450]
                        if np.mean(cropped) <= 9:
                                emp.append(0)
                        else:
                                emp.append(1)
                else:
                        seg.append(file)
                
        data = {'FileName': ult,
                'EmptyFrame': emp,
                'Guidewire_Segmentation': seg}

        df = pd.DataFrame(data, columns = ["FileName", "EmptyFrame", "Guidewire_Segmentation"])

        out = r'C:\Users\Mimi\Documents\aigt\DeepLearnLive\Datasets\Unet data'
        exportPath = os.path.join(out, item)
        df.to_csv(exportPath + '_Ultrasound_Labels.csv', index = True, header = True)