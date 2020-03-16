import os


IMAGE_DIR = 'faces'
for i in range(2,25):
    for root, subdirs, files in os.walk(IMAGE_DIR):
        for file in files:
            path = root + "/" + file
            if path.endswith('.'+ str(i) + '.jpg'):
                os.system('rm ' + path)
                print('Removed: ' + path)

