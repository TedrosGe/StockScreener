import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';
import { Table, Container } from 'react-bootstrap';
import KeyInfoComponent1 from "./KeyInfoComponent"

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
const TableComponent = ({data, symbol}) => {
  return(
   
    <Table striped border hover>
       {console.log(data)}
      <thead>
        <tr>
          <th>Date </th>
          <th> Close/Last</th>
          <th>Volume</th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>

        </tr>
      </thead>
      <tbody>
      
       {  data.map((row, index)=> (
         <tr key = {index}>
          <td> {row.date}</td>
          <td>{row.close} </td>
          <td> {row.volume}</td>
          <td> {row.open}</td>
          <td> {row.high}</td>
          <td> {row.low}</td>

          </tr>
      
        )
        
        
        )
       }
        
     
      </tbody>


    </Table>

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
  console.log(stockList)
  return (
    <div>
 
      <h1>Stock Data Line Chart : {symbol}</h1>
      {stockList.length > 0 ? (
        <>
     <LineChartComponent data = {stockList} symbol = {symbol}/> 
      {/* <TableComponent data = {stockList} symbol = {symbol}/> */}
      {<KeyInfoComponent1 data ={stockList}/>}
        </>
      ) 
    : (
      <p>Loading...</p>
    )}
     
    </div>
      
  );
};

export default RenderLineChart;