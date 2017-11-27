import degree_gyro_q_l
import numpy as np
import time
import sysv_ipc

np_degree_data = np.array([[0, 0, 0, 0]])

def safeBoundary(value):
	## <boundary value change> Degree -180 ~ +180 		
	if (value >= -180 and value <= 180):
		pass
	elif (value < -180):
		value = 360 + value	## x = 180 - ( abs(x) - 180 )	 	
	else: 	## (pitch_gyro >= 180)
		value = -360 + value
	
	return value 


def main():
	global np_degree_data
	
	share_acc_gyro_pitch = sysv_ipc.SharedMemory(600, flags=01000, size=20 ,mode=0600)
	share_p_ang_vel = sysv_ipc.SharedMemory(1024, flags=01000,size=20 ,mode=0600)
	share_acc_pitch_degree = sysv_ipc.SharedMemory(256, flags=01000,size=20 ,mode=0600)
	smp1 = sysv_ipc.Semaphore(128, flags=01000, mode=0600,initial_value = 1)
	#share_acc_gyro_pitch = sysv_ipc.SharedMemory(1234, flags=0, size=20, mode=0600)
	#share_p_ang_vel = sysv_ipc.SharedMemory(12345, flags=0)

	b = degree_gyro_q_l.acc()
                
	timecheck_list = []
	acc_gyro_pitch = gyro_pitch_degree = b.pitch()
	np_degree_data = np.array([[0, acc_gyro_pitch, b.pitch(), gyro_pitch_degree]])
	
	start_time = time.time()
	timecheck_list.append(start_time)
	while(True):
		acc_pitch_degree = b.pitch()
		timecheck_list.append(time.time())
		loop_time = timecheck_list[1] - timecheck_list[0]
		timecheck_list.pop(0)
                      
		gyro_pitch_degree, _ = b.gyro_pitch(loop_time, gyro_pitch_degree)
		get_gyro_degree, p_ang_vel = b.gyro_pitch(loop_time, acc_gyro_pitch)
			
		degree_sign = np.sign(get_gyro_degree)
		if((degree_sign * np.sign(acc_pitch_degree)) == 1):
       			acc_gyro_pitch = 0.97 * get_gyro_degree + 0.03 * acc_pitch_degree
		else:
			if(get_gyro_degree < 90 and get_gyro_degree > -90):
				acc_gyro_pitch = 0.97 * get_gyro_degree + 0.03 * acc_pitch_degree
			else:
				acc_gyro_pitch = degree_sign * ((0.97 * abs(get_gyro_degree)) + (0.03 * (360 - abs(acc_pitch_degree))))
				acc_gyro_pitch = safeBoundary(acc_gyro_pitch)
		
		data_time = time.time() - start_time
		np_degree_data = np.append(np_degree_data, [[data_time, acc_gyro_pitch, acc_pitch_degree, gyro_pitch_degree]], axis=0)
                		#acc_gyro_pitch = np.sign(get_gyro_degree) * ((0.97 * abs(get_gyro_degree)) + (0.03 * abs(acc_pitch_degree)))
        	#vari = share_acc_gyro_pitch.read()          
		#print(vari)     
		
		smp1.acquire(10)
		#print acc_gyro_pitch
		share_acc_pitch_degree.write(str("%0.1f" % acc_pitch_degree).ljust(19," "))
		share_acc_gyro_pitch.write(str("%0.1f" % acc_gyro_pitch).ljust(19," "))
		share_p_ang_vel.write(str("%0.1f" % p_ang_vel).ljust(19," "))
		smp1.release()		
		
		time.sleep(0.01)
if __name__ == '__main__':
	try:
		main()
	except:
		np.save('degree_Data', np_degree_data)
		print "\n<degree_Data.npy is saved>"
