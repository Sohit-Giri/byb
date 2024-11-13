// Object containing weather data for different cities
const cities = {
    'Kathmandu': {
        background: 'https://images.unsplash.com/photo-1605640840605-14ac1855827b?q=80&w=1200',
        temp: '23°C',
        humidity: '65%',
        wind: '2.5 km/h',
        pressure: '1015 hPa',
        description: 'Partly Cloudy',
        icon: '02d'
    },
    'Pokhara': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/6/66/Pokhara_and_Phewa_Lake.jpg',
        temp: '25°C',
        humidity: '70%',
        wind: '3.0 km/h',
        pressure: '1012 hPa',
        description: 'Clear Sky',
        icon: '01d'
    },
    'Bhaktapur': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/d/d9/Nyatpola_%26_Bhairav_Temple.jpg',
        temp: '22°C',
        humidity: '68%',
        wind: '2.2 km/h',
        pressure: '1014 hPa',
        description: 'Scattered Clouds',
        icon: '03d'
    },
    'Surkhet': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/6/6b/Ghantaghar%40surkhet.JPG',
        temp: '28°C',
        humidity: '60%',
        wind: '3.5 km/h',
        pressure: '1010 hPa',
        description: 'Clear Sky',
        icon: '01d'
    },
    'Chitwan': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/8/82/Chitwan_swamp.jpg',
        temp: '30°C',
        humidity: '75%',
        wind: '2.8 km/h',
        pressure: '1009 hPa',
        description: 'Mostly Clear',
        icon: '02d'
    },
    'Biratnagar': {
        background: 'https://nepaltourismhub.com/wp-content/uploads/2019/12/download-4.jpg',
        temp: '29°C',
        humidity: '72%',
        wind: '3.2 km/h',
        pressure: '1008 hPa',
        description: 'Partly Cloudy',
        icon: '02d'
    },
    'Butwal': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/c/c0/Butwal.jpg',
        temp: '27°C',
        humidity: '65%',
        wind: '2.9 km/h',
        pressure: '1011 hPa',
        description: 'Clear Sky',
        icon: '01d'
    },
    'Dharan': {
        background: 'https://web.nepalnews.com/storage/story/1024/DharanClocktower1611483852_1024.jpg',
        temp: '26°C',
        humidity: '70%',
        wind: '2.7 km/h',
        pressure: '1013 hPa',
        description: 'Scattered Clouds',
        icon: '03d'
    },
    'Nepalgunj': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/8/81/Bageshwori_Temple_Nepalgunj%2C_Banke.jpg',
        temp: '31°C',
        humidity: '58%',
        wind: '3.8 km/h',
        pressure: '1007 hPa',
        description: 'Clear Sky',
        icon: '01d'
    },
    'Ilam': {
        background: 'https://upload.wikimedia.org/wikipedia/commons/b/b8/Ilam_green.jpg',
        temp: '20°C',
        humidity: '78%',
        wind: '2.4 km/h',
        pressure: '1016 hPa',
        description: 'Light Rain',
        icon: '10d'
    }
};

// Select elements from the DOM
const searchInput = document.querySelector('.search-input'); // Search input field
const dropdown = document.querySelector('.dropdown'); // Dropdown container
const weatherCard = document.querySelector('.weather-card'); // Weather card container

// Function to update weather information based on selected city
function updateWeather(city) {
    const cityData = cities[city]; // Get weather data for the selected city
    if (!cityData) return; // Return if the city data is not found

    // Update background image with a fade effect
    document.body.style.opacity = '0'; // Fade out the current background
    setTimeout(() => {
        // Set the new background image for the body
        document.body.style.backgroundImage = `linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('${cityData.background}')`;
        document.body.style.backgroundSize = 'cover'; // Set background to cover the screen
        document.body.style.backgroundPosition = 'center'; // Center the background
        document.body.style.opacity = '1'; // Fade in the new background
    }, 300);

    // Update weather card with animation
    weatherCard.style.opacity = '0'; // Start with the weather card hidden
    weatherCard.style.transform = 'translateY(20px)'; // Apply downward translation

    setTimeout(() => {
        // Update weather icon using the city icon from data
        const weatherIcon = weatherCard.querySelector('.weather-icon');
        weatherIcon.src = `https://openweathermap.org/img/wn/${cityData.icon}@2x.png`; // Set icon URL

        // Update temperature
        const temperature = weatherCard.querySelector('.temperature');
        temperature.textContent = cityData.temp;

        // Update description
        const description = weatherCard.querySelector('.description');
        description.textContent = cityData.description;

        // Update weather details like humidity, wind, and pressure
        const details = weatherCard.querySelectorAll('.detail-item p');
        details[0].textContent = cityData.humidity; // Humidity
        details[1].textContent = cityData.wind; // Wind speed
        details[2].textContent = cityData.pressure; // Pressure

        // Show weather card with animation
        weatherCard.style.opacity = '1'; // Fade in the weather card
        weatherCard.style.transform = 'translateY(0)'; // Move the card to its original position
    }, 300);

    // Close dropdown
    dropdown.classList.remove('active');
}

// Function to filter cities based on the search input
function filterCities(searchTerm) {
    const filteredCities = Object.keys(cities).filter(city =>
        city.toLowerCase().includes(searchTerm.toLowerCase()) // Filter cities by name
    );

    // Clear previous dropdown items
    dropdown.innerHTML = '';

    if (filteredCities.length > 0) {
        // If there are filtered cities, create dropdown items
        filteredCities.forEach(city => {
            const dropdownItem = document.createElement('div');
            dropdownItem.classList.add('dropdown-item'); // Add class for styling
            dropdownItem.textContent = city;

            // Add click event to update the weather for selected city
            dropdownItem.addEventListener('click', () => {
                searchInput.value = city; // Set input value to selected city
                updateWeather(city); // Update weather for the selected city
            });

            dropdown.appendChild(dropdownItem); // Append item to the dropdown
        });

        dropdown.classList.add('active'); // Show the dropdown
    } else {
        dropdown.classList.remove('active'); // Hide dropdown if no matches
    }
}

// Event Listeners
searchInput.addEventListener('input', (e) => {
    filterCities(e.target.value); // Filter cities as user types
});

searchInput.addEventListener('focus', () => {
    if (searchInput.value) {
        filterCities(searchInput.value); // Filter cities when input is focused
    }
});

// Close dropdown when clicking outside the search input
document.addEventListener('click', (e) => {
    if (!searchInput.contains(e.target)) {
        dropdown.classList.remove('active'); // Hide dropdown if clicked outside
    }
});

// Initialize with default city ('Kathmandu')
updateWeather('Kathmandu');

// Add smooth transition for background changes
document.body.style.transition = 'opacity 0.3s ease';
weatherCard.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
