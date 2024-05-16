async function downloadYTVideo() {
    document.getElementById("vidInfo").classList.add("d-none");
    document.getElementById("loadSpinner").classList.remove("d-none");
    document.getElementById("loadSpinner").classList.add("d-block");
    url = document.getElementById("url").value;
    res = document.getElementById("quality").value;
    await eel.downloadYTVideo(url, res);
    document.getElementById("vidInfo").classList.remove("d-none");
    document.getElementById("loadSpinner").classList.add("d-none");
}

async function getVidInfo() {
    document.getElementById("vidInfo").classList.add("d-none");
    document.getElementById("loadSpinner").classList.remove("d-none");
    document.getElementById("loadSpinner").classList.add("d-block");
    url = document.getElementById("url").value;

    if (url !== undefined && url !== "") {

        vidInfo = await eel.getVidInfo(url)();
        vidInfo = JSON.parse(vidInfo);

        select = document.getElementById("quality");
        while (select.hasChildNodes()) {
            select.removeChild(select.firstChild);
        }

        for (i in vidInfo.resolutions) {
            opt = document.createElement("option");
            res = vidInfo.resolutions[i] + "p";
            opt.value = res;
            opt.innerHTML = res;
            select.appendChild(opt);
        }

        document.getElementById("thumbnail").src = vidInfo.thumbnailURL;
        document.getElementById("title").innerText = vidInfo.title;
        document.getElementById("views").innerText = vidInfo.views;
        document.getElementById("author").innerText = vidInfo.author;
        document.getElementById("vidInfo").classList.remove("d-none");
        document.getElementById("loadSpinner").classList.add("d-none");

    } else {
        document.getElementById("vidInfo").classList.add("d-none");
    }
}