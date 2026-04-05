// dashboard.js

// Medicine reminder display
function displayMedicineReminder(medicineName, dosage) {
    console.log(`Reminder: Take ${dosage} of ${medicineName}`);
}

// Stock indicator updates
function updateStockIndicator(medicineName, quantity) {
    console.log(`Stock for ${medicineName}: ${quantity}`);
}

// Countdown timer calculation
function startCountdown(duration) {
    let timer = duration, hours, minutes, seconds;
    const interval = setInterval(function () {
        hours = parseInt(timer / 3600, 10);
        minutes = parseInt((timer % 3600) / 60, 10);
        seconds = parseInt(timer % 60, 10);

        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        console.log(`${hours}:${minutes}:${seconds}`);

        if (--timer < 0) {
            clearInterval(interval);
            console.log('Time is up!');
        }
    }, 1000);
}

// Floating action button interaction
function setupFabInteraction() {
    const fab = document.getElementById('fab');
    fab.addEventListener('click', () => {
        console.log('FAB clicked!');
        // Add your interaction logic here
    });
}

// Real-time notifications
function showNotification(message) {
    console.log(`Notification: ${message}`);
}

// Example usage
displayMedicineReminder('Paracetamol', '500mg');
updateStockIndicator('Paracetamol', 20);
startCountdown(3600); // 1 hour countdown
setupFabInteraction();
showNotification('Your medicine is due!');
