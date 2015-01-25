# smartvim
A python script that can makes vim to accept a grep style output file name
For example: if you tap: vim AndroidManifest.xml:100: , then :
the AndroidManifest.xml will opened by vim and go to line 100.

Steps:
1. Give the script executable permission.
2. Edit the ~/.bashrc , add one line: alias vim='smartvim.py' , and copy the smartvim.py to your $PATH directory.
   OR edit the ~/.bashrc , add one line: alias vim=(The absolute path of your smartvim.py)
