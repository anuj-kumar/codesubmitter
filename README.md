Code Submitter for Hackrerrank.com
==================================

A plugin to compile and test the code on hackerrank.com directly from the gedit browser.

Usage Instructions:

1. install gedit
2. enable external tools plugin in gedit from edit->preferences->plugins
3. go to tools->manage external tools->run command
4. replace the script with this:

#!/bin/sh

#TODO: use "gconftool-2 -g /desktop/gnome/applications/terminal/exec"
#eval $(zenity --entry --title="Run Command - gedit" --text="Command to run:")
eval python /home/anuj/coding/httprequest.py $(zenity --entry --title="Test Code - gedit" --text="problem name:") $(zenity --entry --title="Test Code" --text="File name:")

5. assign a shortcut key as per your convenience
6. go to the editor and use the shortcut key you assigned earlier to start the plugin
7. enter the problem name and file name as prompted
8. wait for the result to appear on the console pane