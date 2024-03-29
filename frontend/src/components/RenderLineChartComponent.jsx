import React, { useEffect, useState } from 'react';
import KeyInfoComponent from './KeyInfoComponent';
import axios from 'axios';
import LineChartComponent from './LineChartComponent'
import { useParams } from 'react-router-dom';
// ... (imports and component definition)

const RenderLineChart = () => {
const {symbol} = useParams();
  const [stockInfo, setStockInfo] = useState([]);
  const [stockHist, setStockHist] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/home/${symbol}`);
      const stocks = response.data.stocks;
      setStockInfo(stocks);

      const response2 = await axios.get(`http://localhost:8000/home/history/${symbol}`)
      const stock_history = response2.data.stock_history;
      setStockHist(stock_history);
   
      setLoading(false);



    } catch (error) {
      console.error("Stock fetch failed", error);
      setLoading(false); 
    }
  };

  useEffect(() => { fetchData(); }, [ symbol]);

  return (
    <div>
     
      <h1> Stock: {symbol}</h1>
      {loading ? ( <p>loading...</p> ) : (
        <div> 
          {(
            <>
            
             <LineChartComponent StockHistory={stockHist} />
 
            {<KeyInfoComponent stock_data={stockInfo} />}
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default RenderLineChart;
