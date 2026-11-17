function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    const output = document.getElementById("system_response");

    if (!textToAnalyze) {
        output.textContent = "Please enter some text to analyze.";
        return;
    }

    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze))
        .then(async (response) => {
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.error || "Unable to analyze this text.");
            }
            output.textContent =
                "Dominant emotion: " + data.dominant_emotion +
                " | Anger: " + data.anger +
                " | Disgust: " + data.disgust +
                " | Fear: " + data.fear +
                " | Joy: " + data.joy +
                " | Sadness: " + data.sadness;
        })
        .catch((error) => {
            output.textContent = error.message;
        });
}
