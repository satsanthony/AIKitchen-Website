// Hamburger menu for mobile
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');
if (hamburger) {
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Interactive robot arm animation
const robotArm = document.getElementById('robotArm');
if (robotArm) {
    robotArm.addEventListener('click', () => {
        robotArm.style.transform = 'rotate(-20deg) scale(1.1)';
        setTimeout(() => {
            robotArm.style.transform = 'rotate(0deg) scale(1)';
        }, 600);
        alert('The RoboKitchen arm is ready to cook your favorite meal!');
    });
}