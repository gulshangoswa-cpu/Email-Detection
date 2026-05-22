document.addEventListener('DOMContentLoaded', function() {
    
    // Prediction Form Handler
    const predictBtn = document.getElementById('predict-btn');
    const subjectInput = document.getElementById('subject-input');
    const loader = document.getElementById('loader');
    const resultDiv = document.getElementById('prediction-result');
    const categorySpan = document.getElementById('result-category');
    const confidenceSpan = document.getElementById('result-confidence');
    
    if (predictBtn && subjectInput) {
        predictBtn.addEventListener('click', async function() {
            const subject = subjectInput.value.trim();
            if (!subject) return;
            
            // Show loader, hide result
            loader.style.display = 'block';
            resultDiv.style.display = 'none';
            predictBtn.disabled = true;
            
            try {
                const response = await fetch('/api/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ subject: subject })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    categorySpan.textContent = data.category;
                    confidenceSpan.textContent = data.confidence;
                    
                    // Add some color coding based on category
                    categorySpan.className = 'badge rounded-pill fs-5 ';
                    if (data.category === 'Spam') {
                        categorySpan.classList.add('bg-danger');
                    } else if (data.category === 'Important') {
                        categorySpan.classList.add('bg-success');
                    } else if (data.category === 'Security' || data.category === 'OTP') {
                        categorySpan.classList.add('bg-warning', 'text-dark');
                    } else {
                        categorySpan.classList.add('bg-info', 'text-dark');
                    }
                    
                    resultDiv.style.display = 'block';
                } else {
                    alert(data.error || 'An error occurred');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Failed to connect to the server');
            } finally {
                loader.style.display = 'none';
                predictBtn.disabled = false;
            }
        });
    }
    
    // Initialize charts if on dashboard
    const accuracyChartCtx = document.getElementById('accuracyChart');
    if (accuracyChartCtx) {
        new Chart(accuracyChartCtx, {
            type: 'doughnut',
            data: {
                labels: ['Spam', 'Important', 'Updates', 'Others'],
                datasets: [{
                    data: [30, 20, 25, 25],
                    backgroundColor: [
                        '#ff4d4d',
                        '#00f3ff',
                        '#9d4edd',
                        '#4CAF50'
                    ],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { color: '#ffffff' }
                    }
                }
            }
        });
    }
});
