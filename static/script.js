document.getElementById('recommendForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const movie = document.getElementById('movieInput').value;
  
    fetch('/recommend', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `movie=${encodeURIComponent(movie)}`
    })
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById('resultList');
      list.innerHTML = '';
      data.forEach(movie => {
        const li = document.createElement('li');
        li.innerText = movie;
        list.appendChild(li);
      });
    });
  });
  