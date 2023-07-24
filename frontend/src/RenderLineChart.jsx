import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';
import { Table, Container } from 'react-bootstrap';


const LineChartComponent = ({data,symbol}) =>{
 
    return( 

      <div className='center-container'> 
     
  <ResponsiveContainer width="70%" height={350}  >
    <LineChart data={data}>
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="close" name="Close Price" stroke="#8884d8" />
    </LineChart>
  </ResponsiveContainer>
  </div> 
    )

}


const RenderLineChart = ({ symbol }) => {
  const [stockList, setStockList] = useState([]);

  useEffect(() => {
    // Call the lookup endpoint with the provided symbol
    axios
      .get(`http://localhost:8000/lookup/${symbol}`)
      .then(response => {  
      const stocks = response.data.stocks; 
      setStockList(stocks);
      })
      .catch(error => {
        console.error("Stock fetch failed");
      });
  }, [symbol]); // dependency to re-run the effect

  return (
    <div>
 
 <h1>Stock Data Line Chart : {symbol}</h1>
      <LineChartComponent data = {stockList} symbol = {symbol}/> 
    </div>
      
  );
};

export default RenderLineChart;