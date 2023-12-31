var likeCounter = 0;
var dislikeCounter = 0;
function likeCount(){
    likeCounter = likeCounter+1;
    document.querySelector("#like").classList.add("fill-red-600");
    document.querySelector("#heartCount").innerHTML=likeCounter;
    document.querySelector("#heartinput").value=likeCounter;
}

function dislikeCount(){
    dislikeCounter = dislikeCounter+1;
    document.querySelector("#dislike").classList.add("fill-red-600");
    document.querySelector("#brockCount").innerHTML=dislikeCounter;
    document.querySelector("#brockinput").value=dislikeCounter;
}

function userProfile(e) {
    if (e.name == "close"){
    document.querySelector("#userProfileUl").classList.remove("hidden")
    e.name = "open"
    }else{
        
    document.querySelector("#userProfileUl").classList.add("hidden")
    e.name = "close"
}
}
  