// Toggle between converters
function showConverter(type) {
    // Hide all converter sections
    document.querySelectorAll('.converter-section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Remove the 'active' class from all selection buttons
    document.querySelectorAll('.selection-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show the selected converter section by adding 'active' class
    document.getElementById(type).classList.add('active');
    
    // Highlight the selected button by adding 'active' class
    event.target.classList.add('active');
}
// Conversion logic
function convertDate(type) {
    // Check if conversion is BS to AD
    if (type === 'bs-to-ad') {
        // Get user inputs for BS year, month, and day
        const year = parseInt(document.getElementById('bsYear').value);
        const month = parseInt(document.getElementById('bsMonth').value);
        const day = parseInt(document.getElementById('bsDay').value);
        
        // Basic BS to AD conversion logic (simplified, may not be exact)
        let adYear = year - 57; // Adjust year difference
        let adMonth = month;
        let adDay = day;
        // Adjust month and day based on BS to AD conversion rules
        if (month <= 9) {
            // For months Baisakh to Ashwin (first half of BS year)
            adMonth += 4;
            if (day > 15) {
                adDay -= 15;
            } else {
                adMonth--;
                adDay += 15;
            }
        } else {
            // For months Kartik to Chaitra (second half of BS year)
            adMonth -= 10;
            adYear++;
            if (day > 15) {
                adDay -= 15;
            } else {
                adMonth--;
                adDay += 15;
            }
        }
        // Array of month names in AD
        const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                      'July', 'August', 'September', 'October', 'November', 'December'];
        
        // Format and display the result in AD format
        const result = `${months[adMonth-1]} ${adDay}, ${adYear} AD`;
        document.getElementById('bs-to-ad-result').innerText = result;
        document.getElementById('bs-to-ad-result').style.display = 'block'; // Show result section
    } else {
        // Get user inputs for AD year, month, and day
        const year = parseInt(document.getElementById('adYear').value);
        const month = parseInt(document.getElementById('adMonth').value);
        const day = parseInt(document.getElementById('adDay').value);
        
        // Basic AD to BS conversion logic (simplified, may not be exact)
        let bsYear = year + 57; // Adjust year difference
        let bsMonth = month;
        let bsDay = day;
        // Adjust month and day based on AD to BS conversion rules
        if (month <= 4) {
            // For months January to April (first part of AD year)
            bsMonth += 9;
            bsYear--;
            if (day > 15) {
                bsDay -= 15;
            } else {
                bsMonth--;
                bsDay += 15;
            }
        } else {
            // For months May to December (second part of AD year)
            bsMonth -= 3;
            if (day > 15) {
                bsDay -= 15;
            } else {
                bsMonth--;
                bsDay += 15;
            }
        }
        // Array of month names in BS
        const months = ['Baisakh', 'Jestha', 'Ashadh', 'Shrawan', 'Bhadra', 'Ashwin',
                      'Kartik', 'Mangsir', 'Poush', 'Magh', 'Falgun', 'Chaitra'];
        
        // Format and display the result in BS format
        const result = `${months[bsMonth-1]} ${bsDay}, ${bsYear} BS`;
        document.getElementById('ad-to-bs-result').innerText = result;
        document.getElementById('ad-to-bs-result').style.display = 'block'; // Show result section
    }
}
