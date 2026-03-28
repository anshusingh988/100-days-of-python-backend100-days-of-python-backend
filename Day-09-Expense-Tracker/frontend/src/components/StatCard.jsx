import React from 'react';

const StatCard = ({ label, value, type }) => {
  const getLabelColor = () => {
    switch (type) {
      case 'income': return 'var(--success)';
      case 'expense': return 'var(--danger)';
      default: return 'var(--primary)';
    }
  };

  return (
    <div className="stat-card">
      <span className="stat-label">{label}</span>
      <span className="stat-value" style={{ color: getLabelColor() }}>
        {type === 'expense' ? '-' : ''}₹{Math.abs(value).toLocaleString()}
      </span>
    </div>
  );
};

export default StatCard;
