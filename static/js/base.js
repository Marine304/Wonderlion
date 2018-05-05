window.onload=function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener("click", function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute("href")).scrollIntoView({
                behavior: "smooth",
                block: "start",
            });
        });
    });


    $(".navbar-collapse a").click(function() {
      $(".navbar-collapse").collapse("hide");
    });

    $(".lineup_img").bind("touchstart touchend", function(e) {
      $(this).attr("src", $(this).data("hover"));
    });
}