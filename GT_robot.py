from fairino import Robot
import subprocess

def main():
    robot = Robot.RPC('192.168.58.2')
    
    GTlocate = list(map(float,robot.GetRobotTeachingPoint("GTlocate")[1][6:12]))
    GTpickup = list(map(float,robot.GetRobotTeachingPoint("GTpickup")[1][6:12]))
    GTpostlocate = list(map(float,robot.GetRobotTeachingPoint("GTpostlocate")[1][6:12]))
    GTpreplace = list(map(float,robot.GetRobotTeachingPoint("GTpreplace")[1][6:12]))
    GTprerotate = list(map(float,robot.GetRobotTeachingPoint("GTprerotate")[1][6:12]))
    GTpushto = list(map(float,robot.GetRobotTeachingPoint("GTpushto")[1][6:12]))
    GTplace = list(map(float,robot.GetRobotTeachingPoint("GTplace")[1][6:12]))
    GTpostplace = list(map(float,robot.GetRobotTeachingPoint("GTpostplace")[1][6:12]))
    GTlocate2 = list(map(float,robot.GetRobotTeachingPoint("GTlocate2")[1][6:12]))
    GTpickup2 = list(map(float,robot.GetRobotTeachingPoint("GTpickup2")[1][6:12]))

    while True:
        i = 0
        robot.MoveJ(GTpreplace, 0, 0, vel=40)
        while i < 2:
            robot.SetDO(0,1)
            robot.WaitMs(500)
            if i == 0:
                robot.MoveJ(GTlocate, 0, 0, vel=40)
                robot.MoveJ(GTpickup, 0, 0, vel=40)
                robot.SetDO(0,0)
                robot.WaitMs(1500)
                robot.MoveJ(GTlocate, 0, 0, vel=40)
            elif i == 1:
                robot.MoveJ(GTlocate2, 0, 0, vel=40)
                robot.MoveJ(GTpickup2, 0, 0, vel=40)
                robot.SetDO(0,0)
                robot.WaitMs(1500)
                robot.MoveJ(GTlocate2, 0, 0, vel=40)
            robot.MoveJ(GTpostlocate, 0, 0, vel=40)
            robot.MoveJ(GTpreplace, 0, 0, vel=40)
            robot.MoveJ(GTprerotate, 0, 0, vel=40)
            robot.MoveJ(GTplace, 0, 0, vel=40)
            robot.SetDO(0,1)
            robot.WaitMs(1000)
            robot.MoveJ(GTpushto, 0, 0)
            robot.WaitMs(1000)
            robot.MoveJ(GTplace, 0, 0)
            robot.WaitMs(1000)
            robot.MoveJ(GTpreplace, 0, 0, vel=40)
            #robot.WaitMs(2000)
            #Running job
            print("Job started.")
            process = subprocess.Popen(['./venv/Scripts/python.exe', './job_queue.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()  # This waits for the process to complete
            print(f"Job ended. {stdout} {stderr}")


            robot.MoveJ(GTprerotate, 0, 0, vel=40)
            robot.MoveJ(GTpushto, 0, 0, vel=40)
            robot.SetDO(0,0)
            robot.WaitMs(1000)
            robot.MoveJ(GTpostplace, 0, 0, vel=40)
            robot.MoveJ(GTpreplace, 0, 0, vel=40)
            if i == 0:
                robot.MoveJ(GTlocate, 0, 0, vel=40)
                robot.MoveJ(GTpickup, 0, 0, vel=40)
                robot.SetDO(0,1)
                robot.WaitMs(1500)
                robot.MoveJ(GTlocate, 0, 0, vel=40)
            elif i == 1:
                robot.MoveJ(GTpostlocate, 0, 0, vel=40)
                robot.MoveJ(GTlocate2, 0, 0, vel=40)
                robot.MoveJ(GTpickup2, 0, 0, vel=40)
                robot.SetDO(0,1)
                robot.WaitMs(1500)
                robot.MoveJ(GTlocate2, 0, 0, vel=40)
            i += 1
if __name__ == "__main__":
    main()