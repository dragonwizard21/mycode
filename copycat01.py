#!/usr/bin/env python3
import shutil
import os
##This script will create a backup file and backup directory of 5g_research & sdn_network.txt
os.chdir("/home/student/mycode/")

#copy file to from the source to the destination
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#shutil.copytree will copy an entire folder and all of the nested contents.
shutil.copytree("5g_research/", "5g_research_backup/")

