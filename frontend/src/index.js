import React from 'react';
import ReactDOM from 'react-dom'; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RenderLineChart from './components/RenderLineChartComponent';



ReactDOM.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/home/:symbol" element={<RenderLineChart />} />
      </Routes>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);