var likeCount = Number(document.querySelector("#heartCount").innerText);
var dislikeCount = Number(document.querySelector("#brockCount").innerText);
console.log(typeof likeCount)

var liker = document.querySelector("#like");
var attribName = liker.attributes[1];
liker.addEventListener('click',function(){
    if (attribDis !== "nodislike"){
        if (attribName == "nolike"){
            liker.setAttribute("fill","white");
            likeCount = likeCount-1;
            document.querySelector("#heartCount").innerText = likeCount;
            document.querySelector("#heartinput").value = likeCount;
            attribName = 'like';
        }else{
            liker.setAttribute("fill","red");
            likeCount = likeCount+1;
            document.querySelector("#heartCount").innerText = likeCount;
            document.querySelector("#heartinput").value = likeCount;
            attribName = "nolike";
        }
}else{
    disliker.setAttribute("fill","white")
        dislikeCount = dislikeCount-1
        document.querySelector("#brockCount").innerText = dislikeCount;
        document.querySelector("#brockinput").value = dislikeCount;
        attribDis = 'dislike';
        liker.setAttribute("fill","red");
        likeCount = likeCount+1;
        document.querySelector("#heartCount").innerText = likeCount;
        document.querySelector("#heartinput").value = likeCount;
        attribName = "nolike";
}
})
var disliker = document.querySelector("#dislike");
var attribDis = disliker.attributes[1];
disliker.addEventListener('click',function(){
    if (attribName !== "nolike"){
        if (attribDis == "nodislike"){
        disliker.setAttribute("fill","white")
        dislikeCount = dislikeCount-1
         document.querySelector("#brockCount").innerText = dislikeCount;
        document.querySelector("#brockinput").value = dislikeCount;
        attribDis = 'dislike';
    }else {
        disliker.setAttribute("fill","red")
        dislikeCount = dislikeCount+1
         document.querySelector("#brockCount").innerText = dislikeCount;
        document.querySelector("#brockinput").value = dislikeCount;
        attribDis = 'nodislike';
        }
}else{
     liker.setAttribute("fill","white");
    likeCount = likeCount-1;
    document.querySelector("#heartCount").innerText = likeCount;
    document.querySelector("#heartinput").value = likeCount;
    attribName = 'like';
    disliker.setAttribute("fill","red")
    dislikeCount = dislikeCount+1
    document.querySelector("#brockCount").innerText = dislikeCount;
    document.querySelector("#brockinput").value = dislikeCount;
    attribDis = 'nodislike';
}
})

function userProfile(e) {
    if (e.name == "close"){
    document.querySelector("#userProfileUl").classList.remove("hidden")
    e.name = "open"
    }else{
        
    document.querySelector("#userProfileUl").classList.add("hidden")
    e.name = "close"
}
}


//like comments updates

var like = document.querySelector("#like");
var dislike = document.querySelector("#dislike");

$(document).ready(function(){
    $('#like').click(function(){
        var formData = $('#updateForm').serialize();

        $.ajax({
            type : "POST",
            url : "/update/",
            data : formData,
            success :function(data){
                console.log(data)
                var like = data.current_likes
                console.log(like)
                $('#heartCount').text(JSON.stringify(like)); 
            },
            error: function(error){
                console.log(error)
            }
        });
    });
    $('#dislike').click(function(){
        var formData = $('#updateForm').serialize();

        $.ajax({
            type : "POST",
            url : "/update/",
            data : formData,
            success :function(data){
                console.log(data)
                var dislike = data.current_dislikes
                $('#brockCount').text(JSON.stringify(dislike)); 
            },
            error: function(error){
                console.log(error)
            }
        });
    });
});
