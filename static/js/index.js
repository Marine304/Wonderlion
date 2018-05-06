window.onload = function() {
    var wonderful = document.getElementById("wonderful");

    if (wonderful) {
      wonderful.addEventListener("click", function(event) {
          window.location.href = "//wonderlion.me/home/main/";
        }, false);
    }

}

function movePage(target) { 
    window.location.href = "//wonderlion.me/home/main/#" + target;

}
