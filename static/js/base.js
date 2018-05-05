window.onload=function() {
    document.querySelectorAll('a[href^="#n_"]').forEach(anchor => {
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
}