import Servo
import degree_add_gyro 
import threading
import time

## Initialize
count = 1
pwm_1 = 1.1
pwm_2 = 1.22
f = open("data.txt", 'w')

## Using threading Timer
def every5sec() :
    	b = degree_add_gyro.acc()
    
    	global pwm_1
    	pwm_1 += 0.01
    
    	#print "pwm_v1 = %s pwm_v2 = %s degree = %s \n" % (pwm_1, pwm_2, b.pitch())
    	print "\n\n\n\n\n\n\n\n\n---------------------motor up---------------------\n"
	threading.Timer(5, every5sec).start()

def every1sec() :
	global count
	global f
	
	data = "%s sensor data / sec \n" % count
	f.write(data)
	count = 1
	print "\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!! 1sec over !!!!!!!!!!!!!!!!!!!!!\n"

	threading.Timer(1, every1sec).start()

def main() :
    	pitch_aver = 180
	a = Servo.servo()
    	b = degree_add_gyro.acc()
	global count    	

	#f = open("data.txt", 'w')
    	
	que = []
	#timecheck_list = []    	
		
#	every5sec()
	every1sec()
	
	#timecheck_list.append(time.time())
    	while(True):
		
		#a.servo_1(pwm_1)
        	#a.servo_2(pwm_2)
	
		#print "pwm_v1 = %s pwm_v2 = %s degree = %s ---- count : %s" % (pwm_1, pwm_2, b.pitch(), count)
		#timecheck_list.append(time.time())
		#print "loop time : %s" % (timecheck_list[1] - timecheck_list[0])
		#timecheck_list.pop(0)
			
		#count += 1		

		"""
		data = "pwm_v1 = %s pwm_v2 = %s degree = %s \n" % (pwm_1, pwm_2, b.pitch())
        	f.write(data)
		"""

		que.append(b.pitch())
		if(len(que) == 10):
			pitch_aver = sum(que,0.0)/len(que)
    			print "pwm_v1 = %s pwm_v2 = %s degree = %s ---- count : %s" % (pwm_1, pwm_2, pitch_aver, count)
			count += 1
			que.pop(0)
		if(pitch_aver <=180 and pitch_aver >0):
			a.servo_1(1.2)
			a.servo_2(pwm_2)
			print "180down"
		elif(pitch_aver >180 and pitch_aver < 360):
			a.servo_1(pwm_1)
			a.servo_2(1.3)
			print "180up"
		else:
	        	a.servo_1(pwm_1)
                       	a.servo_2(pwm_2)		
if __name__ == '__main__':
    main()
