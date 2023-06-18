import React, { useEffect, useState } from 'react';
import axios from 'axios';



const Component = () => {
  const [trendingStocks, setTrendingStocks] = useState([]);

  useEffect(() => {
    // Call the /lookup endpoint
    axios.get('http://localhost:8000/lookup')
      .then(response => {
        const stocks = response.data.stocks;
        setTrendingStocks(stocks);
     
      })
      .catch(error => {
        console.error("error");
        
      });
  }, []);

  return (
    <div className='main'>

    <div className='menu-container'>
      <div className=' menu-item'> </div>
      <div className=' menu-item'></div>
      <div className=' menu-item'></div>
      <div className=' menu-item'></div>
    </div>
    
    <div>

      <h2>Trending Stocks</h2>
      <ul>
        {trendingStocks.map(stock => (
         <li key={stock.id}>
         Ticker: {stock.ticker}<br />
            Company: {stock.company}<br />
            Industry: {stock.industry}
       </li>
        ))}
      </ul>
    </div>
    </div>
  );
};

export default Component;
