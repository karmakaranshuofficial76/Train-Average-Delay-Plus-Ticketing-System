import os
lst = list(os.listdir())
if 'model.json' not in lst or 'model.h5' not in lst:
    print('File not Found')
    raise SystemError
read = "\nimport os\nlst = list(os.listdir())\n#print(lst)\nif(not 'model.json' in lst or not 'model.h5' in lst):\n    print('File not Found')\n    raise(SystemError)\nelse:\n    pass\n    #print('Everything is fine')\n\n"
