import struct
class send_data:
    def __init__(self,buffer,size):
        self.struct_fmt  =str.format('f',size)
        self.struct_len = struct.calcsize(self.struct_fmt)


        if buffer != None:
            unpacked = struct.unpack(self.struct_fmt, buffer)


            self.acc_gyro = unpacked[0]


    def GetBytes(self):
            return struct.pack(self.struct_fmt,self.acc_gyro,self.acc_pitch,self.p_ang_vel )

    def GetSize(self):
        return self.struct_len
