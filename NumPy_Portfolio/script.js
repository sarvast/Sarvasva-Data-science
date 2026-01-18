document.addEventListener('DOMContentLoaded', () => {

    // --- Mobile Nav Toggle ---
    const navToggle = document.getElementById('nav-toggle');
    const sidebar = document.getElementById('sidebar');

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            sidebar.classList.toggle('active');
            navToggle.innerHTML = sidebar.classList.contains('active') ? '✕' : '☰';
        });

        // Close when clicking a link
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 1024) {
                    sidebar.classList.remove('active');
                    navToggle.innerHTML = '☰';
                }
            });
        });
    }

    // --- Run Button Simulation ---
    document.querySelectorAll('.run-btn').forEach(btn => {
        btn.addEventListener('click', function () {
            const cell = this.closest('.cell');
            const outputBlock = cell.querySelector('.output-block');
            const hiddenText = outputBlock.getAttribute('data-output');

            // Visual reset
            outputBlock.textContent = '';
            outputBlock.style.color = 'var(--text-primary)';

            // Typing effect
            let i = 0;
            const type = () => {
                if (i < hiddenText.length) {
                    outputBlock.textContent += hiddenText.charAt(i);
                    i++;
                    setTimeout(type, 5); // Fast typing
                }
            };

            // Mock latency
            outputBlock.textContent = 'Running...';
            setTimeout(() => {
                outputBlock.textContent = '';
                type();
            }, 300);
        });
    });

    // --- MCQ Logic ---
    window.checkMcq = function (btn, isCorrect) {
        const card = btn.closest('.mcq-card');
        const explanation = card.querySelector('.explanation');
        const allOptions = card.querySelectorAll('.option-btn');

        // Disable all buttons in this card
        allOptions.forEach(opt => {
            opt.style.pointerEvents = 'none';
            if (opt === btn) {
                // Style selected
                opt.classList.add(isCorrect ? 'correct' : 'wrong');
            } else if (opt.getAttribute('onclick').includes('true')) {
                // Highlight the correct one if they missed it
                if (!isCorrect) opt.classList.add('correct');
            }
        });

        // Show Explanation
        explanation.classList.add('show');
    };
});
