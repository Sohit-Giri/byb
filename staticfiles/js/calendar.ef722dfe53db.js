// Function to add a note for each day before Kartik 15
function addNote() {
    // Prompt the user to enter a note for the selected day
    const note = prompt("Enter your note for this day:");
    
    // If the user enters a note (i.e., note is not empty or null)
    if (note) {
        // Display a message that the note has been saved
        // This is just for demonstration; actual saving could involve saving to local storage or a backend
        alert("Your note has been saved: " + note);
    }
}
// Function to add a note for each day after Kartik 15
function addNoteToDay(button) {
    const dayElement = button.closest('.day'); // Get the closest day element
    const notesContainer = dayElement.querySelector('.notes'); // Find the notes section for this day
    
    // Prompt the user for a note
    const noteText = prompt("Enter your note:");
    if (noteText) {
        alert("Your note has been saved: " + note);
        const noteDiv = document.createElement("div"); // Create a new div for the note
        noteDiv.classList.add("note"); // Add class for styling
        noteDiv.textContent = noteText; // Set the text content to the user's input
        notesContainer.appendChild(noteDiv); // Append the note to the notes container
    }
}

// Function to toggle the visibility of details
function toggleDetails(detailsElement) {
    const moreDetails = detailsElement.querySelector('.more-details');
    const notesContainer = detailsElement.querySelector('.notes');
    
    // Toggle the display of the additional details and notes
    if (moreDetails.style.display === "none") {
        moreDetails.style.display = "block"; // Show more details
        notesContainer.style.display = "block"; // Show notes section
    } else {
        moreDetails.style.display = "none"; // Hide more details
        notesContainer.style.display = "none"; // Hide notes section
    }
}

function printPage() {
    window.print(); // This will trigger the print dialog to print the current page
}
// Initialize the calendar when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const calendar = new NepaliCalendar();
});