import React from 'react';
import { Home, PieChart, TrendingUp, TrendingDown, Settings, LogOut, PlusCircle } from 'lucide-react';

const Sidebar = ({ activeTab, setActiveTab }) => {
  const navItems = [
    { id: 'dashboard', label: 'Dashboard', icon: Home },
    { id: 'income', label: 'Income', icon: TrendingUp },
    { id: 'expenses', label: 'Expenses', icon: TrendingDown },
    { id: 'settings', label: 'Settings', icon: Settings },
  ];

  return (
    <div className="sidebar">
      <div className="logo">
        <PlusCircle size={32} />
        <span>ExpensePro</span>
      </div>
      
      <ul className="nav-links">
        {navItems.map((item) => (
          <li 
            key={item.id} 
            className={`nav-item ${activeTab === item.id ? 'active' : ''}`}
            onClick={() => setActiveTab(item.id)}
          >
            <item.icon size={20} />
            <span>{item.label}</span>
          </li>
        ))}
      </ul>

      <div className="nav-item">
        <LogOut size={20} />
        <span>Logout</span>
      </div>
    </div>
  );
};

export default Sidebar;
