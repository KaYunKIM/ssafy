#!/bin/bash
app_name='vuejs-app'
image_name='cafesns-vuejs'
docker stop ${app_name}
docker rmi ${image_name}

repository_name='s03p12a203'

if [ -d ${repository_name} ]; then
	rm -rf ${repository_name}
fi

git clone -b frontend --single-branch https://lab.ssafy.com/s03-webmobile2-sub2/${repository_name}.git && cd ${repository_name}/vue_front/cafesns
docker build -t ${image_name} . && docker run -d -it -p 8080:80 --rm --name ${app_name} ${image_name}
