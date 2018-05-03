window.onload = function() {
    var wonderful = document.getElementById("main_nav");

    if (wonderful) {
      wonderful.addEventListener("mouseover", function(event) {
          event.target.style.color = "#e85757";
          setTimeout(function() {
            event.target.style.color = "white";
          }, 500);
        }, false);
    }

}

function movePage(target) { 
    window.location.href = "http://wonderful.ap-northeast-2.elasticbeanstalk.com/home/main/#" + target;
    // window.location.href = "http://www.localhost:8000/home/main/#" + target;
}
