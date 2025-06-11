 document.getElementById('addWordForm').addEventListener('submit', function(e){
  e.preventDefault();

  const formData = new FormData(this);

  fetch('/add_word/', {
    method: 'POST',
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    const msgDiv = document.getElementById('message');
    if(data.success){
      msgDiv.textContent = `სიტყვა "${data.word}" დაემატა დონეზე "${data.level}"`;
      this.reset();
    } else if(data.error){
      msgDiv.textContent = `შეცდომა: ${data.error}`;
    }
  })
  .catch(() => {
    document.getElementById('message').textContent = 'შეცდომა მოთხოვნის შესრულებისას';
  });
});

