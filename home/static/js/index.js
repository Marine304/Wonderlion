window.onload=function() {
    var wonderful = document.getElementById("main_nav");
    console.log(wonderful);
    if (wonderful) {
      wonderful.addEventListener("mouseover", function(event) {
          event.target.style.color = "#e85757";
          setTimeout(function() {
            event.target.style.color = "white";
          }, 500);
        }, false);
    }
}
