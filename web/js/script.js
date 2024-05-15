async function saludar() {
    document.getElementById("prueba").innerText = await eel.Saludar()();
}

function download_yt_video() {
    url = document.getElementById("url").value
    folder = document.getElementById("folder")
    eel.download_yt_video(url, folder);
}