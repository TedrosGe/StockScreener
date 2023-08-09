import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';
import { Table, Container } from 'react-bootstrap';



const KeyInfoComponent = () => {
  const data = [
    {
      marketCap: '1234',
      recommendationMean: 150.25,
      'p/e': 10000,
      forwardPE: 152.50,
      high: 153.75,
      low: 148.20,
      currentPrice: 12,
      '52WeekChange' : 0.08,
      volume: 22,
      fiftyTwoWeekLow : 83,
      fiftyTwoWeekHigh: 77,

    },

  ];
    return(
      
     
      <Table striped  hover className='no-border-table'>
         {console.log(data)}
     
        <tbody>     
         {  data.map((row, index)=> (
           <><tr key={index}>

             <td> marketCap: {row.marketCap}</td>
             <td>Recom: {row.recommendationMean} </td>
             <td> volume: {row.volume}</td>
             <td> Price: {row.currentPrice}</td>
             <td> High: {row.high}</td>
             <td> Low: {row.low}</td>
           </tr> 
           <tr>
           <td> 52WeekHigh: {row.fiftyTwoWeekHigh}</td>
             <td>52Weeklow: {row.fiftyTwoWeekLow} </td>
             <td> 52WeekCh: {row['52WeekChange']}</td>
             <td> P/E: {row['p/e']}</td>
             <td> forwardPE: {row.forwardPE}</td>
             <td> high: {row.high}</td>
             </tr></>
            
         )
          )
         }  
        </tbody>
      </Table>
    )
  }

  export default KeyInfoComponent;