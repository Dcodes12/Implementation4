function getStars(ratingOutOf10) {
    const scaled = (ratingOutOf10 / 10) * 6;
    const fullStars = Math.floor(scaled);
    const hasHalfStar = (scaled % 1) >= 0.25;
    const totalStars = fullStars + (hasHalfStar ? 1 : 0);
    const emptyStars = 6 - totalStars;
  
    return (
      '<span class="star full">' + '⭐'.repeat(fullStars) + '</span>' +
      (hasHalfStar ? '<span class="star half">✰</span>' : '') +
      '<span class="star empty">' + '☆'.repeat(emptyStars) + '</span>'
    );
  }
  
  
  document.addEventListener("DOMContentLoaded", () => {
    const recList = document.querySelector(".recommendation-list");
    const storedData = localStorage.getItem("recommendations");
  
    if (!storedData) {
      recList.innerHTML = "<p>No recommendations available.</p>";
      return;
    }
  
    let recommendations = JSON.parse(storedData);
  
    // Shuffle and limit to 6
    recommendations = recommendations.sort(() => Math.random() - 0.5).slice(0, 6);
  
    recommendations.forEach(movie => {
      const card = document.createElement("div");
      card.className = "recommendation-card";
  
      const title = movie.title || "Untitled";
      const poster = movie.poster_url ? `<img src="${movie.poster_url}" alt="${title}" class="poster">` : "";
      const trailer = movie.trailer_url ? `<a href="${movie.trailer_url}" class="watch-trailer" target="_blank">▶ Watch Trailer</a>` : "";
      const rating = typeof movie.vote_average === "number" ? getStars(movie.vote_average) : "No rating available";
      const genre = movie.genre || "Unknown Genre";
      const description = movie.overview || "No description available.";

  
      card.innerHTML = `
        ${poster}
        <div class="details">
          <div class="movie-title">${title}</div>
          <div class="stars">${rating}</div>
          <div class="extra-info">
          <p><strong>Genre:</strong> ${genre}</p>
          <p class="description">${description}</p>
          </div>

          ${trailer}
        </div>
      `;
  
      recList.appendChild(card);
    });
  });
  