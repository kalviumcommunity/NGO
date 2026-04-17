import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import Papa from 'papaparse';
import { LineChart, BarChart2, Activity, Target } from 'lucide-react';

const Card = ({ title, icon: Icon, children, className = '' }) => (
  <motion.div 
    initial={{ opacity: 0, y: 20 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.6 }}
    className={`glass-panel ${className}`}
  >
    <div className="glass-header">
      <Icon size={24} color="var(--accent-amber)" />
      <h2 className="glass-title">{title}</h2>
    </div>
    <div className="glass-content">
      {children}
    </div>
  </motion.div>
);

function App() {
  const [ngoData, setNgoData] = useState([]);

  useEffect(() => {
    fetch('/outputs/ranked_ngo_programs.csv')
      .then(response => response.text())
      .then(csvData => {
        Papa.parse(csvData, {
          header: true,
          dynamicTyping: true,
          skipEmptyLines: true,
          complete: (results) => {
            setNgoData(results.data);
          }
        });
      })
      .catch(err => console.error("Could not load CSV data", err));
  }, []);

  const getBadgeClass = (score) => {
    if (score > 0.7) return 'badge-top';
    if (score > 0.5) return 'badge-mid';
    return 'badge-low';
  };

  return (
    <div className="app-container">
      <header className="header">
        <motion.h1 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8 }}
          className="title"
        >
          NGO <span className="title-gradient">Impact Optimizer</span>
        </motion.h1>
        <motion.p 
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3, duration: 0.8 }}
          className="subtitle"
        >
          Evidence-based evaluation & resource allocation using data science
        </motion.p>
      </header>

      <div className="dashboard-grid">
        <Card title="Executive Dashboard" icon={Activity} className="dashboard-hero">
          <img src="/outputs/final_dashboard.png" alt="Final Dashboard" className="dashboard-img" />
        </Card>

        <Card title="Resource Efficiency Analysis" icon={BarChart2}>
          <img src="/outputs/efficiency_chart.png" alt="Efficiency Chart" className="dashboard-img" />
        </Card>

        <Card title="Outlier Detection (Reach)" icon={LineChart}>
          <img src="/outputs/outlier_boxplot.png" alt="Outlier Boxplot" className="dashboard-img" />
        </Card>

        <Card title="Top Recommended Programs" icon={Target} className="dashboard-hero">
          <div className="table-container">
            <table>
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>NGO Name</th>
                  <th>Program Type</th>
                  <th>Budget</th>
                  <th>Reach</th>
                  <th>Cost/Person</th>
                  <th>Impact Score</th>
                </tr>
              </thead>
              <tbody>
                {ngoData.slice(0, 8).map((row, index) => (
                  <motion.tr 
                    key={index}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: 0.1 * index }}
                  >
                    <td><strong>#{index + 1}</strong></td>
                    <td>{row.ngo_name}</td>
                    <td>{row.program_type}</td>
                    <td>${row.budget_usd?.toLocaleString()}</td>
                    <td>{row.impact_reach?.toLocaleString()}</td>
                    <td>
                      <span className={`badge ${getBadgeClass(row.impact_score)}`}>
                        ${row.cost_per_person?.toFixed(2)}
                      </span>
                    </td>
                    <td>
                      <div style={{ display: 'flex', alignItems: 'center' }}>
                        <span>{(row.impact_score * 100).toFixed(1)}%</span>
                        <div className="score-bar-bg">
                          <div 
                            className="score-bar-fill" 
                            style={{ width: `${Math.min(row.impact_score * 100, 100)}%` }}
                          />
                        </div>
                      </div>
                    </td>
                  </motion.tr>
                ))}
              </tbody>
            </table>
          </div>
        </Card>
      </div>
    </div>
  );
}

export default App;
