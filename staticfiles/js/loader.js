// Function to show the loader
function showLoader() {
    document.getElementById('loader').style.display = 'flex';
}

// Function to hide the loader
function hideLoader() {
    document.getElementById('loader').style.display = 'none';
}

// Show loader when navigating to a new page
document.addEventListener('DOMContentLoaded', function () {
    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', function (event) {
            // Ensure it is not an external link
            if (!link.target || link.target === '_self') {
                showLoader();
            }
        });
    });

    // Hide loader once the current page is fully loaded
    window.onload = hideLoader;
});
