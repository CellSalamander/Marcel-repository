const express = require('express');
const app = express();
const path = require('path');
const sqlite3 = require('sqlite3').verbose();

const PORT = 3000;

app.use(express.static(path.join(__dirname, 'public')));


app.use(express.json());


app.post('/api/book', (req, res) => {
  const { name, surname, phone, email, address, message } = req.body;

  if (!email || !phone) {
    return res.status(400).json({ error: 'Missing required fields.' });
  }

  const db = new sqlite3.Database('./main.db', sqlite3.OPEN_READWRITE, (err) => {
    if (err) {
      console.error("DB connection error:", err.message);
      return res.status(500).json({ error: 'Database connection failed.' });
    }

    function getCurrentDateTime(){
      const now = new Date();
      const year = now.getFullYear();
      const month = String(now.getMonth() + 1).padStart(2, '0');
      const day = String(now.getDate()).padStart(2, '0');
      const hours = String(now.getHours()).padStart(2, '0');
      const minutes = String(now.getMinutes()).padStart(2, '0');
      const seconds = String(now.getSeconds()).padStart(2, '0');
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    };

    const currentDate = getCurrentDateTime();

    db.run(`INSERT INTO users (name, surname, phone, email, address)
            VALUES (?, ?, ?, ?, ?)`,
      [name, surname, phone, email, address],
      function(err) {
        if (err) {
          console.error("Insert error:", err.message);
          return res.status(500).json({ error: 'Insert failed' });
        }

        const newUserID = this.lastID;

        db.run('INSERT INTO orders (userID, created_at, scheduled_at, status, notes) VALUES (?,?,?,?,?)',
          [newUserID,currentDate,null,"Pending",message],
          function(err) {
            if (err) {
              console.error("Insert error:", err.message);
              return res.status(500).json({ error: 'Insert 2 failed' });
            } 

            res.json({ message: 'Booking successful', id: this.lastID });
            
            db.close((err) => {
              if (err) {
                console.error("Could not close database", err.message);
              }
            });
            
          }
        );
      }
    );
  });
});



app.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});
