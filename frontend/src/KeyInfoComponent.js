import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';
import { Table, Container } from 'react-bootstrap';



const KeyInfoComponent1 = ({data}) => {
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

  export default KeyInfoComponent1;