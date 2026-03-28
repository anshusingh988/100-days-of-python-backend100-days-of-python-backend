import React from 'react';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';

ChartJS.register(ArcElement, Tooltip, Legend);

const SummaryChart = ({ data }) => {
  const chartData = {
    labels: data.map(item => item.category),
    datasets: [
      {
        data: data.map(item => item.amount),
        backgroundColor: [
          '#6366f1', '#ec4899', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444'
        ],
        borderWidth: 0,
      },
    ],
  };

  const options = {
    plugins: {
      legend: {
        position: 'bottom',
        labels: { color: '#94a3b8', padding: 20 }
      }
    },
    maintainAspectRatio: false,
  };

  return (
    <div className="chart-section" style={{ height: '100%', width: '100%' }}>
      <Doughnut data={chartData} options={options} />
    </div>
  );
};

export default SummaryChart;
