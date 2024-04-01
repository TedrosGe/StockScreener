import React, { useEffect, useState } from 'react';

import { Table, Container } from 'react-bootstrap';

const TableComponent = ({data, symbol}) => {
    return(
     
      <Table className="w-full">
        
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
            <td > {row.date}</td>
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
  
  export default TableComponent;