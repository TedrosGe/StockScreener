import React from 'react';
import ReactDOM from 'react-dom/client'; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RenderLineChart from './components/RenderLineChartComponent';
import TrendingStocks from './components/TrendingStocksComponent';


const root = ReactDOM.createRoot(document.getElementById('root'));


root.render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/home/:symbol" element={<RenderLineChart />} />
        <Route path="/home" element={<TrendingStocks />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
