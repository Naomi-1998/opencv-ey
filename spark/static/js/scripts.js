document.addEventListener('DOMContentLoaded', () => {
    const countElement = document.getElementById('count');
    
    setInterval(() => {
        fetch(window.location.href)
            .then(r => r.text())
            .then(html => {
                const doc = new DOMParser().parseFromString(html, 'text/html');
                const newCount = doc.getElementById('count').innerText;
                
                if (countElement.innerText !== newCount) {
                    countElement.style.transform = 'scale(1.2)';
                    setTimeout(() => {
                        countElement.style.transform = 'scale(1)';
                    }, 300);
                }
                
                countElement.innerText = newCount;
            });
    }, 1000);
});
