//menu
function userProfile(e) {
    if (e.name == "close"){
    document.querySelector("#userProfileUl").classList.remove("hidden")
    e.name = "open"
    }else{
        
    document.querySelector("#userProfileUl").classList.add("hidden")
    e.name = "close"
}
}
  
  //Trending Scroll
  
  document.addEventListener('DOMContentLoaded', function () {
    const carouselItems = document.querySelectorAll('[data-carousel-item]');
    const prevButton = document.querySelector('[data-carousel-prev]');
    const nextButton = document.querySelector('[data-carousel-next]');
    let currentIndex = 0;

    function showItem(index) {
      carouselItems.forEach((item, i) => {
        item.classList.toggle('hidden', i !== index);
      });
    }

    function showNextItem() {
      currentIndex = (currentIndex + 1) % carouselItems.length;
      showItem(currentIndex);
    }

    function showPrevItem() {
      currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length;
      showItem(currentIndex);
    }
    showItem(currentIndex);
    prevButton.addEventListener('click', showPrevItem);
    nextButton.addEventListener('click', showNextItem);
  });

