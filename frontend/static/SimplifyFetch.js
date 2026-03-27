async function sendTextToBackend() {
    const inputText = document.getElementById("inputArea").value;

    const { SERVER_SIMPLIFY_URL } = getconfgi();

    const response = await fetch(`${SERVER_SIMPLIFY_URL}/simplify`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    });

    const data = await response.json();

    document.getElementById("outputArea").textContent = data.simplified;
}