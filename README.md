# MxEduOL
- Basic educational website wrote in Win10x64
- The website main part is finished
- Need to deploy on the server with nginx and uwsgi

## guest account
(As the ALiCloud has baned the 25 port, so it would not send any register email.So...)
- username: guest
- password: qweasdzxc


The tools I used as follows:

tools | version
----- | -----
Pycharm Pro|2017.1
MySQL |5.6.35
Workbench|6.3CE
Navicat|11.0.10

Then is the packages for Environmental dependence Version:

<img src="https://github.com/zsdostar/MxEduOL/raw/master/image/PackagesVersion.png" />


extra:

django-pure-pagination

django-simple-captcha

20171116 - CentOS7下部署的时候发现刷不出来验证码，后把Pillow从4.3.0降级到4.2.1，遂正常
