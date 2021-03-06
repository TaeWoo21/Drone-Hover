import threading
import degree_gyro_q_l
import numpy as np
import time
import sysv_ipc
share_acc_gyro_pitch = sysv_ipc.SharedMemory(1 , flags=01000,size=20 ,mode=0600)
share_ang_vel = sysv_ipc.SharedMemory( 21, flags=01000,size=20 ,mode=0600)
b = degree_gyro_q_l.acc()
                
timecheck_list = []
acc_gyro_pitch = gyro_pitch_degree = b.pitch()
                
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
			#acc_gyro_pitch = safeBoundary(acc_gyro_pitch)

 
                        #acc_gyro_pitch = np.sign(get_gyro_degree) * ((0.97 * abs(get_gyro_degree)) + (0.03 * abs(acc_pitch_degree)))
        #vari = share_acc_gyro_pitch.read()          
	#print(vari)     
	share_acc_gyro_pitch.write(str(acc_gyro_pitch))
