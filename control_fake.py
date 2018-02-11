#from pynput.keyboard import Key, Controller
import subprocess
import time
#keyboard = Controller()

def xdotool(command):
	subprocess.Popen(command, shell = True)
	#process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE)

#xdotool keydown alt key Tab; sleep 2; xdotool keyup alt

def release():
	bashCommand = "xdotool keyup Left Right Up Down Return"
	xdotool(bashCommand)
	"""
	keyboard.release(Key.left)
	keyboard.release(Key.right)
	keyboard.release(Key.up)
	keyboard.release(Key.down)
	keyboard.release(Key.enter)
	"""

# def stay(press_time):
# 	release()
# 	time.sleep(press_time) 

# def continu(press_time):
# 	# release()
# 	time.sleep(press_time) 

def left_s(press_time):
	bashCommand = "xdotool keyup Right; xdotool keydown Left"
	xdotool(bashCommand)
	#keyboard.release(Key.right)
	# release()	
	#keyboard.press(Key.left)
	# time.sleep(press_time)   

def left_e(press_time):
	bashCommand = "xdotool keyup Left"
	xdotool(bashCommand)
	#keyboard.release(Key.left)

def right_s(press_time):
	bashCommand = "xdotool keyup Left; xdotool keydown Right"
	xdotool(bashCommand)
	#keyboard.release(Key.left)
	# release()	
	#keyboard.press(Key.right)
	# time.sleep(press_time)    

def right_e(press_time):	
	bashCommand = "xdotool keyup Right"
	xdotool(bashCommand)
	#keyboard.release(Key.right)

def up(press_time):
	bashCommand = "xdotool keydown Up; sleep "+str(press_time)+"; xdotool keyup Up"
	xdotool(bashCommand)
	# release()
	#keyboard.press(Key.up)
	#time.sleep(press_time)    
	#keyboard.release(Key.up)

def p(press_time):
	bashCommand = "xdotool keydown Return; sleep "+str(press_time)+"; xdotool keyup Return"
	xdotool(bashCommand)
	# release()
	#keyboard.press(Key.enter)
	#time.sleep(press_time)    
	#keyboard.release(Key.enter)

def p_down(press_time):
	bashCommand = "xdotool keydown Down+Return; sleep "+str(press_time)+"; xdotool keyup Down+Return"
	xdotool(bashCommand)
	# release()	
	#with keyboard.pressed(Key.down):
	#	keyboard.press(Key.enter)
	#	time.sleep(press_time)    
	#	keyboard.release(Key.enter)
	#keyboard.release(Key.down)

# def down(press_time):
# 	# release()
# 	keyboard.press(Key.down)
# 	# time.sleep(press_time)    
# 	# keyboard.release(Key.down)

# def p_left(press_time):
# 	# release()
# 	with keyboard.pressed(Key.left):
# 		keyboard.press(Key.enter)
# 		time.sleep(press_time)    
# 		# keyboard.release(Key.enter)

# def p_right(press_time):
# 	# release()	
# 	with keyboard.pressed(Key.right):
# 		keyboard.press(Key.enter)
# 		time.sleep(press_time)    
# 		# keyboard.release(Key.enter)

# def p_up(press_time):
# 	# release()
# 	with keyboard.pressed(Key.up):
# 		keyboard.press(Key.enter)
# 		time.sleep(press_time)    
# 		# keyboard.release(Key.enter)


