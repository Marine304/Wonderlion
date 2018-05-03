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
    window.location.href = "https://99ce1693eebc4523ad15a8d2757fb5c7.vfs.cloud9.us-east-2.amazonaws.com/home/main/#" + target;
}
s