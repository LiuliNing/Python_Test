#!/usr/bin/bash
red_col="\e[1;31m"
reset_col="\e[0m"

#工作目录
export Root_Current_Dir=$(cd `dirname $0`;pwd)
cd $Root_Current_Dir
source ${Root_Current_Dir}/conf/sif_env_config.conf
#
# 导入字体颜色
#

bold=$(tput bold)
underline=$(tput sgr 0 1)
reset=$(tput sgr0)

red=$(tput setaf 1)
green=$(tput setaf 76)
white=$(tput setaf 7)
tan=$(tput setaf 202)
blue=$(tput setaf 25)
#
# 设置样式
#

underline() { printf "${underline}${bold}%s${reset}\n" "$@"
}
h1() { printf "\n${underline}${bold}${blue}%s${reset}\n" "$@"
}
h2() { printf "\n${underline}${bold}${white}%s${reset}\n" "$@"
}
debug() { printf "${white}%s${reset}\n" "$@"
}
info() { printf "${white}➜ %s${reset}\n" "$@"
}
success() { printf "${green}✔ %s${reset}\n" "$@"
}
error() { printf "${red}✖ %s${reset}\n" "$@"
}
warn() { printf "${tan}➜ %s${reset}\n" "$@"
}
bold() { printf "${bold}%s${reset}\n" "$@"
}
note() { printf "\n${underline}${bold}${blue}Note:${reset} ${blue}%s${reset}\n" "$@"
}



#node 1.
function caidan() {
  cat <<YanKaI
+------------------------------------------------+
|       欢迎使用SinfCloud集群安装程序            |
| ____  _        __  ____ _                 _    |
|/ ___|(_)_ __  / _|/ ___| | ___  _   _  __| |   |
|\___ \| |  _ \| |_| |   | |/ _ \| | | |/ _  |   |
| ___) | | | | |  _| |___| | (_) | |_| | (_| |   |
||____/|_|_| |_|_|  \____|_|\___/ \__,_|\__,_|   |
|                                                |
|这是一个引导页面请输入以下参数进行执行          |
|###################环境检测#################### |
|00.版本检测                                     |
|                                                |
|###################基础操作#################### |
|20.创建基础网络                                 |
|50.基础服务启动/更新                            |
|51.基础服务启动/更新(测试)						 |
|55.应用服务启动/更新	                         |
|999.退出此安装程序                              |
+------------------------------------------------+
YanKaI
}
caidan
#启动
startupsinfcloud() {
	#export $(egrep -v '^#' ${Root_Current_Dir}/conf/sif_env_config.env | xargs)
	##export TAG="$TAG"
	#info "$TAG"
	##export EUREKA_SERVERS="$EUREKA_SERVERS"
	#info "$EUREKA_SERVERS"
	##export HUB_URL="$HUB_URL"
	#info "$HUB_URL"
	#info "postgresql配置中心数据源"
	##export DATASOURCE_DRIVER="$DATASOURCE_DRIVER"
	#info "$DATASOURCE_DRIVER"
	##export DATASOURCE_URL="$DATASOURCE_URL"
	#info "$DATASOURCE_URL"
	##export DATASOURCE_USERNAME="$DATASOURCE_USERNAME"
	#info "$DATASOURCE_USERNAME"
	##export DATASOURCE_PASSWORD="$DATASOURCE_PASSWORD"
	#info "$DATASOURCE_PASSWORD"
	##export DATASOURCE_DIALECT="$DATASOURCE_DIALECT"
	#info "$DATASOURCE_DIALECT"
	#info "#MONGO数据库IP"
	##export SINFCLOUD_MONGO="$SINFCLOUD_MONGO"
	#info "$SINFCLOUD_MONGO"
	#info "REDIS数据库IP"
	##export SINFCLOUD_REDIS="$SINFCLOUD_REDIS"
	#info "$SINFCLOUD_REDIS"
	#info "POSTGRES数据库IP"
	##export SINFCLOUD_POSTGRES="$SINFCLOUD_POSTGRES"
	#info "$SINFCLOUD_POSTGRES"
	#info "Rabbitmq IP"
	##export SINFCLOUD_RABBITMQ="$SINFCLOUD_RABBITMQ"
	#info "$SINFCLOUD_RABBITMQ"
	#info "Collabora IP"
	##export SINFCLOUD_COLLABORA="$SINFCLOUD_COLLABORA"
	#info "$SINFCLOUD_COLLABORA"
	
	#export TAG=1.8.5
	#export EUREKA_SERVERS=http://sinfcloud:supermap1234@discovery1:7001/eureka/,http://sinfcloud:supermap1234@discovery2:7002/eureka/,http://sinfcloud:supermap1234@discovery3:7003/eureka/
	#export HUB_URL=172.16.101.19
	##postgresql配置中心数据源
	#export DATASOURCE_DRIVER=org.postgresql.Driver
	#export DATASOURCE_URL=jdbc:postgresql://sinfcloud-postgres:5432/postgres?currentSchema=sinf_admin
	#export DATASOURCE_USERNAME=postgres
	#export DATASOURCE_PASSWORD=postgres
	#export DATASOURCE_DIALECT=org.hibernate.dialect.PostgreSQLDialect
	##MONGO数据库IP
	#export SINFCLOUD_MONGO=127.0.0.1
	##REDIS数据库IP
	#export SINFCLOUD_REDIS=172.16.101.37
	##POSTGRES数据库IP
	#export SINFCLOUD_POSTGRES=172.16.101.57
	##Rabbitmq IP
	#export SINFCLOUD_RABBITMQ=172.16.101.63
	##Collabora IP
	#export SINFCLOUD_COLLABORA=127.0.0.1
	#export $(egrep -v '^#' ${Root_Current_Dir}/conf/sif_env_config.env | xargs)
	docker stack deploy -c ${Root_Current_Dir}/services-deploy.yml --with-registry-auth sinfcloud
}

startupsinfcloudtest() {
    docker stack deploy -c ${Root_Current_Dir}/services-deploy-sinfcloud.yml --with-registry-auth sinfcloud
}

startupapplication() {
    docker stack deploy -c ${Root_Current_Dir}/services-deploy-announcement.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-duty.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-geohazard.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-knowledge.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-sms.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-suap.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-wechat.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-enterprisecredit.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-geodisasterproject.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-geodisasterprojectstatics.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-minerestore.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-fundsupervision.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-news.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-fx.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-fwgl.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-dataprocessor.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-adminmapmanage.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-mapserver.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-querydisaster.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-warningscheduling.yml --with-registry-auth application
	#docker stack deploy -c ${Root_Current_Dir}/application-mapgatewayserver.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-risk.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-ias.yml --with-registry-auth application
	docker stack deploy -c ${Root_Current_Dir}/services-deploy-slope.yml --with-registry-auth application
}

#node 2.
function panduan() {
  read -p "请您输入安装选项:" NUM
  expr $NUM + 1 &>/dev/null
  if [ "$?" -ne 0 ]; then
    warn "请输入数字!"
  elif [[ "$NUM" == 0 ]]; then
    warn"请输入比0大的数字!"
  fi
}

#版本检测
dockerversion() {
  if [ ! -f "${Root_Current_Dir}/conf/sif_env_config.env" ]; then
    error "未检测到环境变量文件[.env]"
  else
    success "当前应用版本："
    cat ${Root_Current_Dir}/conf/sif_env_config.env | grep TAG
    check_docker;
    check_dockercompose;
  fi
}

#创建自定义网络
createnetworkcustom() {
	info "自定义网络端是110.150.0.0/16 overlay"
	docker network create --driver overlay --subnet=10.250.0.0/16 --gateway=10.250.0.1 sinfcloud_net
}
function check_docker {
	if ! docker --version &> /dev/null
	then
		error "需要先安装docker（17.06.0+）并再次运行此脚本"
		exit 1
	fi

	# docker has been installed and check its version
	if [[ $(docker --version) =~ (([0-9]+)\.([0-9]+)([\.0-9]*)) ]]
	then
		docker_version=${BASH_REMATCH[1]}
		docker_version_part1=${BASH_REMATCH[2]}
		docker_version_part2=${BASH_REMATCH[3]}

		note "docker version: $docker_version"
		# the version of docker does not meet the requirement
		if [ "$docker_version_part1" -lt 17 ] || ([ "$docker_version_part1" -eq 17 ] && [ "$docker_version_part2" -lt 6 ])
		then
			error "需要升级docker软件包 to 17.06.0+.以上版本"
			exit 1
		fi
	else
		error "无法分析docker版本"
		exit 1
	fi
}

function check_dockercompose {
	if ! docker-compose --version &> /dev/null
	then
		error "需要先自己安装docker compose（1.18.0+）并再次运行此脚本"
		exit 1
	fi

	# docker-compose has been installed, check its version
	if [[ $(docker-compose --version) =~ (([0-9]+)\.([0-9]+)([\.0-9]*)) ]]
	then
		docker_compose_version=${BASH_REMATCH[1]}
		docker_compose_version_part1=${BASH_REMATCH[2]}
		docker_compose_version_part2=${BASH_REMATCH[3]}

		note "docker-compose version: $docker_compose_version"
		# the version of docker-compose does not meet the requirement
		if [ "$docker_compose_version_part1" -lt 1 ] || ([ "$docker_compose_version_part1" -eq 1 ] && [ "$docker_compose_version_part2" -lt 18 ])
		then
			error "无法分析docker_compose版本"
			exit 1
		fi
	else
		error ""
		exit 1
	fi
}



function menudo (){
  case $1 in
    00)
      dockerversion
      ;;
    20)
      createnetworkcustom
      ;;
    50)
      startupsinfcloud
      ;;
    51)
      startupsinfcloudtest
      ;;
	55)
      startupapplication
      ;;	  
    1000)
      caidan
      ;;
    esac
}
# 判定是否有参数传入
inputstr="params:$1"
str="params:"
if [ $inputstr == $str ];then
  # 无参数执行原逻辑
  function zong() {
    while :; do
      panduan
      menudo $NUM
    done
  }
  zong
else
  # 有参数传入直接执行完成推出
  menudo $1
  exit 0
fi
