const express = require('express');
const cors = require('cors');
const db = require('./db');

const app = express();
app.use(cors());
app.use(express.json());

// Get all transactions
app.get('/api/transactions', async (req, res) => {
  const rows = await db.all('SELECT * FROM transactions ORDER BY date DESC');
  res.json(rows);
});

// Add new transaction
app.post('/api/transactions', async (req, res) => {
  const { date, description, amount, type } = req.body;
  await db.run(
    'INSERT INTO transactions (date, description, amount, type) VALUES (?, ?, ?, ?)',
    [date, description, amount, type]
  );
  res.json({ success: true });
});

// Delete a transaction
app.delete('/api/transactions/:id', async (req, res) => {
  await db.run('DELETE FROM transactions WHERE id = ?', [req.params.id]);
  res.json({ success: true });
});

// Summary
app.get('/api/summary', async (req, res) => {
  const [income] = await db.all('SELECT SUM(amount) as total FROM transactions WHERE type = "income"');
  const [expense] = await db.all('SELECT SUM(amount) as total FROM transactions WHERE type = "expense"');
  res.json({
    income: income.total || 0,
    expense: expense.total || 0,
    balance: (income.total || 0) - (expense.total || 0),
  });
});

const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
