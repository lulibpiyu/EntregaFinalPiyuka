const slider = document.querySelector('.game-slider');
const nextBtn = document.getElementById('nextBtn');
const prevBtn = document.getElementById('prevBtn');

nextBtn.addEventListener('click', () => {
    slider.scrollBy({ left: 300, behavior: 'smooth' });
});

prevBtn.addEventListener('click', () => {
    slider.scrollBy({ left: -300, behavior: 'smooth' });
});
