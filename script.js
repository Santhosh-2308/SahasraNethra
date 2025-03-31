document.addEventListener('DOMContentLoaded', function () {
  console.log("SahasraNethra Website Loaded");

  // Login Form Handling
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const username = document.getElementById('username').value;
      const password = document.getElementById('password').value;
      
      // Dummy authentication check
      if (username === "admin" && password === "password") {
        alert("Login successful!");
        window.location.href = "index.html";
      } else {
        document.getElementById('loginMessage').innerText = "Invalid username or password.";
      }
    });
  }

  // Fetch Real-time Disaster Alerts (Replace with real API)
  const alertContainer = document.getElementById('alertContainer');
  if (alertContainer) {
    fetch('https://api.example.com/alerts') // Replace with actual API
      .then(response => response.json())
      .then(data => {
        alertContainer.innerHTML = "";
        data.forEach(alert => {
          let alertDiv = document.createElement('div');
          alertDiv.innerHTML = `<strong>${alert.type}</strong>: ${alert.message}`;
          alertContainer.appendChild(alertDiv);
        });
      })
      .catch(() => {
        alertContainer.innerHTML = "Error loading alerts. Please try again.";
      });
  }

  // Hazard Detection Map (Only for hazards.html)
  const hazardMapElement = document.getElementById('hazardMap');
  if (hazardMapElement) {
    setTimeout(() => {  // Ensuring map loads after DOM is fully ready
      var map = L.map('hazardMap').setView([20.5937, 78.9629], 5);

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(map);

      // Sample hazard locations
      const hazards = [
        { lat: 19.0760, lng: 72.8777, type: 'Earthquake' },
        { lat: 28.7041, lng: 77.1025, type: 'Flood' },
        { lat: 13.0827, lng: 80.2707, type: 'Tsunami' }
      ];

      hazards.forEach(hazard => {
        L.marker([hazard.lat, hazard.lng]).addTo(map)
          .bindPopup(`<b>Hazard:</b> ${hazard.type}`);
      });
    }, 500);
  }
});
