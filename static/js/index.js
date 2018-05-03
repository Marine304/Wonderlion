window.onload = function() {
    var wonderful = document.getElementById("wonderful");

    if (wonderful) {
      wonderful.addEventListener("click", function(event) {
          window.location.href = "http://wonderful.ap-northeast-2.elasticbeanstalk.com/home/main/";
        }, false);
    }

}

function movePage(target) { 
    window.location.href = "http://wonderful.ap-northeast-2.elasticbeanstalk.com/home/main/#" + target;
    // window.location.href = "http://www.localhost:8000/home/main/#" + target;
}
