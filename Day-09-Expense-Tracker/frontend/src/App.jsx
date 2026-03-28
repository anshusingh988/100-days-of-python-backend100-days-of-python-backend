import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Sidebar from './components/Sidebar';
import StatCard from './components/StatCard';
import SummaryChart from './components/SummaryChart';
import { Plus, Trash2, IndianRupee } from 'lucide-react';

const API_BASE_URL = 'http://localhost:5000/api';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [transactions, setTransactions] = useState([]);
  const [summary, setSummary] = useState({ totalIncome: 0, totalExpense: 0, balance: 0, categories: [] });
  const [formData, setFormData] = useState({ title: '', amount: '', type: 'expense', category: '', description: '' });

  const fetchTransactions = async () => {
    try {
      const res = await axios.get(`${API_BASE_URL}/transactions`);
      setTransactions(res.data);
    } catch (err) {
      console.error("Error fetching transactions", err);
    }
  };

  const fetchSummary = async () => {
    try {
      const res = await axios.get(`${API_BASE_URL}/summary`);
      setSummary(res.data);
    } catch (err) {
      console.error("Error fetching summary", err);
    }
  };

  useEffect(() => {
    fetchTransactions();
    fetchSummary();
  }, []);

  const handleAdd = async (e) => {
    e.preventDefault();
    try {
      await axios.post(`${API_BASE_URL}/transactions`, formData);
      setFormData({ title: '', amount: '', type: 'expense', category: '', description: '' });
      fetchTransactions();
      fetchSummary();
    } catch (err) {
      console.error("Error adding transaction", err);
    }
  };

  const handleDelete = async (id) => {
    try {
      await axios.delete(`${API_BASE_URL}/transactions/${id}`);
      fetchTransactions();
      fetchSummary();
    } catch (err) {
      console.error("Error deleting transaction", err);
    }
  };

  return (
    <>
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
      
      <main className="main-content">
        <header className="dashboard-header">
          <h1>Professional Dashboard</h1>
          <p className="stat-label">Welcome back! Here's your financial overview.</p>
        </header>

        <section className="stats-grid">
          <StatCard label="Total Balance" value={summary.balance} />
          <StatCard label="Total Income" value={summary.totalIncome} type="income" />
          <StatCard label="Total Expense" value={summary.totalExpense} type="expense" />
        </section>

        <form className="add-transaction-form card-container" onSubmit={handleAdd}>
          <div>
            <label className="stat-label">Title</label>
            <input 
              required
              value={formData.title} 
              onChange={e => setFormData({...formData, title: e.target.value})} 
              placeholder="e.g. Salary"
            />
          </div>
          <div>
            <label className="stat-label">Amount</label>
            <input 
              required
              type="number" 
              value={formData.amount} 
              onChange={e => setFormData({...formData, amount: e.target.value})} 
              placeholder="0.00"
            />
          </div>
          <div>
            <label className="stat-label">Type</label>
            <select value={formData.type} onChange={e => setFormData({...formData, type: e.target.value})}>
              <option value="income">Income</option>
              <option value="expense">Expense</option>
            </select>
          </div>
          <div>
            <label className="stat-label">Category</label>
            <input 
              required
              list="categories" 
              value={formData.category} 
              onChange={e => setFormData({...formData, category: e.target.value})} 
              placeholder="Category"
            />
            <datalist id="categories">
              <option value="Salary" /><option value="Rent" /><option value="Food" />
              <option value="Travel" /><option value="Shopping" /><option value="Utilities" />
            </datalist>
          </div>
          <button type="submit" className="primary"><Plus size={20} /></button>
        </form>

        <div className="dashboard-grid">
          <section className="card-container">
            <h3 style={{ marginBottom: '20px' }}>Recent Transactions</h3>
            <ul className="transaction-list">
              {transactions.map(t => (
                <li key={t.id} className="transaction-item">
                  <div className="transaction-info">
                    <span className="transaction-title">{t.title}</span>
                    <span className="transaction-meta">{t.category} • {t.date}</span>
                  </div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
                    <span className={`transaction-amount ${t.type === 'income' ? 'amount-income' : 'amount-expense'}`}>
                      {t.type === 'income' ? '+' : '-'}₹{t.amount.toLocaleString()}
                    </span>
                    <Trash2 
                      size={18} 
                      className="stat-label" 
                      style={{ cursor: 'pointer' }} 
                      onClick={() => handleDelete(t.id)}
                    />
                  </div>
                </li>
              ))}
            </ul>
          </section>

          <section className="card-container">
            <h3 style={{ marginBottom: '20px' }}>Expense Distribution</h3>
            {summary.categories.length > 0 ? (
              <SummaryChart data={summary.categories} />
            ) : (
              <p className="stat-label" style={{ textAlign: 'center', marginTop: '50px' }}>No expense data yet</p>
            )}
          </section>
        </div>
      </main>
    </>
  );
}

export default App;
