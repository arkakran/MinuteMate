
document.getElementById("start-btn").addEventListener("click", async () => {
  const resultsDiv = document.getElementById("results");
  resultsDiv.classList.add("hidden");

  try {
    const res = await fetch("http://127.0.0.1:5000/process", {
      method: "POST",
    });

    const data = await res.json();

    document.getElementById("summary").innerText = data.summary;

    const actionList = document.getElementById("action-items");
    actionList.innerHTML = "";
    data.action_items.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      actionList.appendChild(li);
    });

    const followUpList = document.getElementById("follow-ups");
    followUpList.innerHTML = "";
    data.follow_ups.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      followUpList.appendChild(li);
    });

    document.getElementById("transcript").innerText = data.transcript;

    resultsDiv.classList.remove("hidden");
  } catch (err) {
    alert("Something went wrong while processing the meeting.");
    console.error(err);
  }
});

document.getElementById("clear-btn").addEventListener("click", async () => {
  try {
    await fetch("http://127.0.0.1:5000/clear", {
      method: "POST",
    });

    document.getElementById("results").classList.add("hidden");
  } catch (err) {
    alert("Failed to clear data.");
    console.error(err);
  }
});
