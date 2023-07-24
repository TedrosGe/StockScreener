import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {Table} from 'react-bootstrap'


const LookUp = () => {
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
     <Table striped bordered hover>
          <thead>
            <tr>
              <th>ID</th>
              <th>Symbol </th>
              <th>Company</th>
              <th>Industry</th>
            </tr>
          </thead>
          <tbody>
            {trendingStocks.map((stock)=> (
                <tr key = {stock.id}>
                
                <td>{stock.id}</td>
                <td>{stock.ticker}</td>
                <td>{stock.company}</td>
                <td>null for now</td>
                
              </tr>
            )
            )}
            
          </tbody>
        </Table>
  );
};

export default LookUp;
