import pickle
import matplotlib.pyplot as plt
SIGN_TYPE = 'aparadinha'

if __name__ == "__main__":
    with open(f'decodedData/{SIGN_TYPE}/1.pkl', 'rb') as input:
        readings = pickle.load(input)
    

    imusFullData = []
    timestamps = []
    for reading in readings:
        imusData = []
        for i in range(5):
            imusData.append(reading.imus[i].accel[0])
            imusData.append(reading.imus[i].accel[1])
            imusData.append(reading.imus[i].accel[2])
            imusData.append(reading.imus[i].gyro[0])
            imusData.append(reading.imus[i].gyro[1])
            imusData.append(reading.imus[i].gyro[2])
        imusFullData.append(imusData)
        timestamps.append((reading.timestamp-(readings[0].timestamp)))

    for i in range(5):
        x_acc = list(zip(*imusFullData))[i*6]
        avg = sum(x_acc[-int(len(x_acc)/3):]) / int(len(x_acc)/3)
        var = sum((x-avg)**2 for x in x_acc[-int(len(x_acc)/3):])/(int(len(x_acc)/3)+1)
        print(f"avg {i+1} = {avg}")
        print(f"var = {var}")
        plt.plot(timestamps[-int(len(timestamps)/3):], x_acc[-int(len(x_acc)/3):], label = f"accel x {i+1} imu")
        # plt.plot(timestamps, list(zip(*imusFullData))[i*6+1], label = f"accel y {i+1} imu")
        # plt.plot(timestamps, list(zip(*imusFullData))[i*6+2], label = f"accel z {i+1} imu")

    plt.legend()
    plt.show() 
    pass