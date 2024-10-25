function runCode() {
    const code = document.getElementById("codeInput").value;
    const output = document.getElementById("output");

    fetch("/run-python", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code })
    })
    .then(response => response.json())
    .then(data => {
        output.textContent = data.output;
    })
    .catch(error => {
        output.textContent = "حدث خطأ أثناء تشغيل الكود.";
        console.error("Error:", error);
    });
}
