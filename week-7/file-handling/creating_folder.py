import os 



# if os.path.exists('test-folder'):
#     print('The folder exists....')
# else:
#     os.mkdir('test-folder')

if os.path.exists('brigette_folder'):
    os.rmdir('brigette_folder')
else:
    os.mkdir('brigette_folder')

