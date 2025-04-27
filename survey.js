document.querySelector(".submit-button").addEventListener("click", function(event) {
    event.preventDefault(); // Prevent form reload

    let selectedGenres = [];
    document.querySelectorAll("input[name='genre']:checked").forEach((checkbox) => {
        selectedGenres.push(checkbox.value);
    });

    if (selectedGenres.length === 0) {
        alert("Please select at least one genre.");
        return;
    }

    fetch("http://127.0.0.1:5000/get_recommendations", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ genres: selectedGenres })
    })
    .then(response => response.json())
    .then(data => {
        localStorage.setItem("recommendations", JSON.stringify(data.recommendations));
        window.location.href = "recommendations.html"; // Redirect to recommendations page
    })
    .catch(error => console.error("Error:", error));
});
