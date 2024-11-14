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
function printPage() {
    window.print(); // This will trigger the print dialog to print the current page
}
// Initialize the calendar when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const calendar = new NepaliCalendar();
});