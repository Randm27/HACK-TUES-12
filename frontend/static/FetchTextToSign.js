;

async function turnTextIntoImage(){
    const text = document.getElementById("text-input").value;
    const { SERVER_SIMPLIFY_URL } = getConfig();

    const response = await fetch(`${SERVER_SIMPLIFY_URL}/text-to-sign`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    const container = document.getElementById("output-video");
    container.innerHTML = "";

    data.frames.forEach(frame => {
        const img = document.createElement("img");
        img.src = frame; 
        img.style.maxWidth = "150px";
        img.style.margin = "5px";
        img.style.borderRadius = "10px";
        container.appendChild(img);
    });

}