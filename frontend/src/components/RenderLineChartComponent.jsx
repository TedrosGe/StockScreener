import React, { useEffect, useState } from 'react';
import KeyInfoComponent from './KeyInfoComponent';
import axios from 'axios';

// ... (imports and component definition)

const RenderLineChart = ({ symbol }) => {
  const [stockInfo, setStockInfo] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/home/${symbol}`);
     
      const stocks = response.data.stocks;
      setStockInfo(stocks);
      setLoading(false); 
    } catch (error) {
      console.error("Stock fetch failed", error);
      setLoading(false); // Set loading to false in case of an error
    }
  };

  useEffect(() => { fetchData(); }, [symbol]);

  return (
    <div>
     
      <h1> Stock: {symbol}</h1>
      {loading ? ( <p>loading...</p> ) : (
        <div> 
          {(
            <>
            <KeyInfoComponent stock_data={stockInfo} />
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default RenderLineChart;
