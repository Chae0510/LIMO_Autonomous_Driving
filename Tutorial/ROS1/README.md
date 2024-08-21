# ROS Programming

## Environment Setting
Using environments:
- Ubuntu 18.04 LTS
- ROS1 melodic

### Create ROS workspace
```
source ~/catkin_ws/devel/setup.bash
echo $ROS_PACKAGE_PATH
```
### Create catkin package
새로운 패키지 생성
```
cd ~/catkin_ws/src
catkin_create_pkg my_package std_msgs rospy roscpp
```
새로운 패키지 빌드 및 소싱
```
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```
rospack 명령어 통한 패키지 종속성 확인
```
rospack depends1 my_package
```
### bashrc에 alias 명령어 정의
```
gedit ~/.bashrc
```
단축어 추가
```
alias eb='gedit ~/.bashrc'
alias vb='vim ~/.bashrc'
alias sb='source ~/.bashrc'
alias cw='cd ~/catkin_ws'
alias cs='cd ~/catkin_ws/src'
alias cm='cd ~/catkin_ws && catkin_make'
alias sai='sudo apt install -y'
alias saup='sudo apt update -y && sudo apt upgrade -y'
alias rb='sudo reboot'
alias sdn='sudo shutdown now'
alias rd='sudo rdate time.bora.net'
```
```
source `/.bashrc
```



### Reference
https://github.com/cmin87394/LIMO_basic_tutorial
