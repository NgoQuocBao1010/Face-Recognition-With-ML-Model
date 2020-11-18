import os
import  shutil
dataPath = "data"

def readFile():
	with open('file.txt', 'r+') as f:
		lines = f.readlines()

	for line in lines:
		name = line[0:-1]
		folder = line.split("-")[0]

# 	folderPath = os.path.join(dataPath, folder)

# 	for img in os.listdir(folderPath):
# 		if name in img:
# 			imgPath = os.path.join(folderPath, img)
# 			os.remove(imgPath)

def deleteEmptyFolder():
	for folder in os.listdir(dataPath):
		if len(os.listdir(dataPath + f"\\{folder}")) == 0:
			shutil.rmtree(dataPath + f"\\{folder}")

# for i in range(1, 50):
# 	if i == 12:
# 		continue

# 	os.makedirs('data/' + str(i))

deleteEmptyFolder()