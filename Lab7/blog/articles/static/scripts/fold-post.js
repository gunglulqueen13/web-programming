var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (e) {
        let parent = e.target.parentElement.parentElement
        if (parent.className == "one-post folded") {
            e.target.innerHTML = "свернуть";
            parent.className = "one-post";
        }
        else {
            e.target.innerHTML = "развернуть";
            parent.className = "one-post folded";
        }

    });
}
