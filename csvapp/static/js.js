document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('addWordForm').addEventListener('submit', function(e){
    e.preventDefault();

    const formData = new FormData(this);

    fetch('/add_btwo/', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      const msgDiv = document.getElementById('message');
      if(data.success){
        msgDiv.textContent = `სიტყვა "${data.word}" დაემატა დონეზე "${data.level}"\nფაილი: ${data.path}`;
        this.reset();
      } else if(data.error){
        msgDiv.textContent = `შეცდომა: ${data.error}\nფაილი: ${data.path || 'unknown'}`;
      }
    })
    .catch(() => {
      document.getElementById('message').textContent = 'შეცდომა მოთხოვნის შესრულებისას';
    });
  });
});




document.addEventListener('DOMContentLoaded', function() {
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
        msgDiv.textContent = `სიტყვა "${data.word}" დაემატა დონეზე "${data.level}"\nფაილი: ${data.path}`;
        this.reset();
      } else if(data.error){
        msgDiv.textContent = `შეცდომა: ${data.error}\nფაილი: ${data.path || 'unknown'}`;
      }
    })
    .catch(() => {
      document.getElementById('message').textContent = 'შეცდომა მოთხოვნის შესრულებისას';
    });
  });
});