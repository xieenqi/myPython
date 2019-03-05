#脚本
import os
import time
# 1. The files and directories to be backed up are specified in a list.
# 要备份的文件和目录在列表中指定  /Users/dgg2/juno/WX
source = ['/Users/dgg2/juno/WX', '/Users/dgg2/juno/IdeaProjects']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backup directory 备份必须存储在主备份目录中
target_dir = '/Users/dgg2/juno/Flutter/NDN'
# Remember to change this to what you will be using
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# Run the backup
if os.system(zip_command) == 0:
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')