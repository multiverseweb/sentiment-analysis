async function analyzeSentiment() {
    const comment = document.getElementById('comment').value;

    // Send the comment to the server for analysis
    const response = await fetch('/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ comment })
    });

    const result = await response.json();
    document.getElementById('result').innerText = `Sentiment: ${result.sentiment}`;
  }