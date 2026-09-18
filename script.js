function showContent(sectionId) {
    // Hide all content sections
    var sections = document.querySelectorAll('.content-section');
    sections.forEach(function(section) {
        section.style.display = 'none';
    });

    // Show the selected content section
    var selectedSection = document.getElementById(sectionId);
    selectedSection.style.display = 'block';
}

function nextTab(currentSectionId) {
    var menuItems = document.querySelectorAll('#sidebar-menu li a');
    for (var i = 0; i < menuItems.length; i++) {
        if (menuItems[i].getAttribute('href').substring(1) === currentSectionId) {
            var nextIndex = (i + 1) % menuItems.length;
            var nextSectionId = menuItems[nextIndex].getAttribute('href').substring(1);
            showContent(nextSectionId);
            break;
        }
    }
}

// Background Chip-like Animation
const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');

let width, height;
let particles = [];

function initCanvas() {
    if (!canvas) return;
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    particles = [];
    const numParticles = Math.floor((width * height) / 20000); 
    for (let i = 0; i < numParticles; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 0.6,
            vy: (Math.random() - 0.5) * 0.6,
            radius: Math.random() * 2 + 1.5
        });
    }
}

function animateCanvas() {
    if (!canvas) return;
    requestAnimationFrame(animateCanvas);
    ctx.clearRect(0, 0, width, height);
    
    ctx.fillStyle = '#60a5fa';
    ctx.lineWidth = 1;

    for (let i = 0; i < particles.length; i++) {
        let p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
            let p2 = particles[j];
            let dist = Math.sqrt(Math.pow(p.x - p2.x, 2) + Math.pow(p.y - p2.y, 2));
            
            if (dist < 150) {
                ctx.beginPath();
                ctx.strokeStyle = `rgba(96, 165, 250, ${0.5 * (1 - dist/150)})`;
                
                ctx.moveTo(p.x, p.y);
                if (Math.abs(p.x - p2.x) > Math.abs(p.y - p2.y)) {
                    ctx.lineTo(p2.x, p.y);
                } else {
                    ctx.lineTo(p.x, p2.y);
                }
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }
        }
    }
}

window.addEventListener('resize', initCanvas);
if (canvas) {
    initCanvas();
    animateCanvas();
}

// Typing Effect
const greetings = ["Hi!", "Bonjour!", "Hola!", "Namaste!", "Hello!"];
let currentGreetingIndex = 0;
let currentText = '';
let isDeleting = false;
let typeSpeed = 150;

function typeEffect() {
    const typingElement = document.getElementById('typing-text');
    if (!typingElement) return;

    const fullText = greetings[currentGreetingIndex];

    if (isDeleting) {
        currentText = fullText.substring(0, currentText.length - 1);
        typeSpeed = 100; // faster when deleting
    } else {
        currentText = fullText.substring(0, currentText.length + 1);
        typeSpeed = 150;
    }

    typingElement.textContent = currentText;

    if (!isDeleting && currentText === fullText) {
        typeSpeed = 2000; // wait before deleting
        isDeleting = true;
    } else if (isDeleting && currentText === '') {
        isDeleting = false;
        currentGreetingIndex = (currentGreetingIndex + 1) % greetings.length;
        typeSpeed = 500; // wait before typing next word
    }

    setTimeout(typeEffect, typeSpeed);
}

document.addEventListener('DOMContentLoaded', () => {
    typeEffect();
    if (document.getElementById('sidebar-canvas')) {
        initSidebarCanvas();
        animateSidebar();
    }
});

// Sidebar Circuit Animation
const sidebarCanvas = document.getElementById('sidebar-canvas');
let sCtx = null;
let sWidth = 0, sHeight = 0;
let stars = [];

if (sidebarCanvas) {
    sCtx = sidebarCanvas.getContext('2d');
}

function initSidebarCanvas() {
    if (!sidebarCanvas || !sCtx) return;
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;
    
    sWidth = sidebarCanvas.width = sidebar.clientWidth;
    sHeight = sidebarCanvas.height = sidebar.clientHeight;
    
    stars = [];
    // create fixed twinkling points
    for (let i = 0; i < 40; i++) {
        stars.push({
            x: Math.random() * sWidth,
            y: Math.random() * sHeight,
            radius: Math.random() * 1.5 + 0.5,
            phase: Math.random() * Math.PI * 2,
            speed: Math.random() * 0.03 + 0.01,
            color: Math.random() > 0.5 ? '#60a5fa' : '#38bdf8'
        });
    }
}

function animateSidebar() {
    if (!sidebarCanvas || !sCtx) return;
    requestAnimationFrame(animateSidebar);
    
    // Clear canvas entirely to preserve background transparency
    sCtx.clearRect(0, 0, sWidth, sHeight);
    
    stars.forEach(star => {
        // Calculate twinkle alpha
        const alpha = (Math.sin(star.phase) + 1) / 2; // oscillates between 0 and 1
        
        sCtx.beginPath();
        sCtx.shadowColor = star.color;
        sCtx.shadowBlur = 8;
        sCtx.fillStyle = star.color;
        sCtx.globalAlpha = alpha;
        
        sCtx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
        sCtx.fill();
        
        star.phase += star.speed;
    });
    sCtx.globalAlpha = 1;
}

window.addEventListener('resize', initSidebarCanvas);