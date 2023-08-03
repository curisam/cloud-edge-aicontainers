<?php
# Initialize the session
session_start();

# If user is not logged in then redirect him to login page
if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== TRUE) {
  echo "<script>" . "window.location.href='./login.php';" . "</script>";
  exit;
}
?>
    
<!DOCTYPE html>
<html>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

    <head>
        <!-- tab ui -->
        <link href="./css/style.css" rel="stylesheet" type="text/css">

        <!-- login -->
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
        <link rel="stylesheet" href="./css/main.css">
        <link rel="shortcut icon" href="./img/favicon-16x16.png" type="image/x-icon">
    </head>

    <body>
        <table width="100%" style="text-align:center; border:none">
            <tr>
                <td colspan="2" style="background-color:lightgrey"> <h2> EVC</h2> </td>
            </tr>
            
            <tr>
                <td style="background-color:gray; color:white; width:20%">
                    <div class="container">
                        <!-- 로그인 인증 -->
                        <div class="alert alert-success my-5">
                            Welcome ! You are now signed in to your account.
                        </div>

                        <!-- User profile -->
                        <div class="row justify-content-center">
                            <div class="col-lg-5 text-center">
                                <img src="./img/blank-avatar.jpg" class="img-fluid rounded" alt="User avatar" width="180">
                                <h4 class="my-4">Hello, <?= htmlspecialchars($_SESSION["username"]); ?></h4>
                                <a href="./logout.php" class="btn btn-primary">Log Out</a>
                            </div>
                        </div>
                        
                        <br/><br/>
                        <!-- 메뉴 -->
                        <ul class="list-group">
                            <li class="list-group-item"> <a href='page_newdevice.php'> 신규 에지 장치 등록 </a> </li>
                            <li class="list-group-item"> <a href='page_admin.php'> 관리자 UI </a> </li>
                            <li class="list-group-item">A third item</li>
                            <li class="list-group-item">A fourth item</li>
                            <li class="list-group-item">And a fifth one</li>
                        </ul>
    
                    </div>
                </td>

                <td style="color:white; text-align:left">
                    <div class="container">
                        <div class="tabs">
                            <div class="tabby-tab">
                                <input type="radio" id="tab-1" name="tabby-tabs" checked>
                                <label for="tab-1">new edge</label>
                                <div class="tabby-content">

                                  <p> <font color = "black"> 😊 1. EVC를 통해 서비스 하려는 에지장치(edge device)에 터미널로 진입합니다.</font> </p>


                                  <p> <font color = "black"> 😊 2. 아래 명령어를 sudo 권한으로 실행하여 sshd 서버를 설치하고, EVC가 제공하는 공개키를 에지장치에 등록합니다.</font> </p>

                                  <blockquote><p> <font color = "blue"> $ wget http://evc.re.kr/newedge.sh -O newedge.sh</font> </p></blockquote>
                                  <blockquote><p> <font color = "blue"> $ bash newedge.sh </font> </p></blockquote>


                                  <p> <font color = "black"> 😊 3. 에지 장치를 EVC에 등록하기 위한 설정을 수행합니다.</font> </p>

                                  <blockquote><p> <font color = "blue"> $ wget http://evc.re.kr/joinedge.sh -O joinedge.sh</font> </p></blockquote>
                                  <blockquote><p> <font color = "blue"> $ bash joinedge.sh </font> </p></blockquote>

                                  <p> <font color = "gray">                     
            📌 주의 및 참고 : 
            EVC와 연동하기 위해서는 적절한 사용자 계정이 있어야 합니다.
            단, 사용자 계정의 권한 설정은 매우 신중해야 합니다.
            에지 디바이스의 특정 사용자 계정이 정상적으로 EVC에 등록되면, EVC는 사용자 계정이 가진 시스템 권한 만큼 에지 디바이스를 제어할 수 있습니다.
            예컨데, 에지 디바이스의 root 권한을 가진 사용자 정보를 EVC에 제공한다면, EVC는 에지 디바이스의 root 권한을 위임 받게 됩니다. 혹은 일반 권한을 가진 사용자 정보를 EVC에 제공한다면, EVC는 시스템을 최신 상태로 업데이트 하거나 필요한 패키지를 설치하지 못할 수 있습니다.
            따라서 어떤 권한을 EVC에 제공할지는 EVC 프레임워크 기술을 사용하려는 사용자의 선택에 달려 있습니다.
            시스템을 제어할 수 있는 권한이 강할수록 EVC는 다양한 기능을 제공하고 사용자는 편리하게 자신의 에지 디바이스를 클러스터 구성원으로 활용할 수 있습니다. 다만 에지 디바이스를 등록한 사용자 입장에서는 시스템의 보안 측면에서 염려도 커질 수 있습니다.
            반대로 보안을 우려하여 제한된 권한을 가진 사용자 정보를 제공한다면, 그 만큼 사용상의 제한이 따르게 됩니다. 📌 
                                      </font> </p>

                                  <img src='imgs/newedge.jpg' width=600 align =bottom>
                                </div>
                            </div>                

                            <div class="tabby-tab">
                                <input type="radio" id="tab-2" name="tabby-tabs">
                                <label for="tab-2">device api</label>
                                <div class="tabby-content">
                                    <iframe src="http://deepcase.mynetgear.com:28004/docs" width=100% height=100%> </iframe>
                                </div>
                            </div>

                            <div class="tabby-tab">
                                <input type="radio" id="tab-3" name="tabby-tabs">
                                <label for="tab-3">cluster</label>
                                <div class="tabby-content">
                                    <p>
                                    <a href="http://ketiabcs.iptime.org:39080/d/yr9KziTVk/edgeframework_admin?orgId=1&from=1686731955352&to=1686753555352" target="_blank"> cluster UI
                                    </a>
                                    </p>
                                    <p> <font color = "black"> - 집접 연결 </font> </p>
                                    <p> <font color = "black"> - Container 기반 연결 </font> </p>
                                    <p> <font color = "black"> - k3s 클러스터 연결 : 초경량 에지 지향 </font> </p>
                                    <p> <font color = "black"> - k8s 클러스터 연결 : 고성능 에지 지향 </font> </p>

                                </div>
                            </div>

                        </div>
                    </div>
                </td>   
            </tr>
                    
            <tr>
                <td colspan="2" style="background-color:#FFCC00"><h5>Footer 영역</h5></td>
            </tr>
        </table>

    </body>
</html>
