function signUp(){
    document.querySelector("#loginForm").classList.add("hidden")
    document.querySelector("#signupForm").classList.remove("hidden")
    document.querySelector("#headLogin").classList.add("hidden")
    document.querySelector("#headSignup").classList.remove("hidden")

}
function creatorPage(){
    document.querySelector("#CreatorLogin").classList.remove("hidden")
    document.querySelector("#loginForm").classList.add("hidden")
    document.querySelector("#headCreator").classList.remove("hidden")
    document.querySelector("#headLogin").classList.add("hidden")
}