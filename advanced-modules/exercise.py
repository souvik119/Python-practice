import shutil #for unzippping file
import re
import os

# shutil.unpack_archive('unzip_me_for_instructions.zip', '', 'zip') #unzip to current location as extracted_content folder (default name)

def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()
    f.close()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

result = []
for folder,sub_folders,files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        full_path = folder+'\\'+f
        result.append(search(full_path))

for r in result:
    if r!= '':
        print(r.group())
