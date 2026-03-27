async function sendTextToBackend() {
    const inputText = document.getElementById("inputArea").value;

    const response = await fetch("http://127.0.0.1:8000/simplify", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    });

    const data = await response.json();

    document.getElementById("outputArea").textContent = data.simplified;
}