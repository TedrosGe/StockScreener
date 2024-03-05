import React from 'react';


import { Table } from 'react-bootstrap';




const LoadingComponent = () => (
  <p>Loading...</p>
);

const KeyInfoComponent = ({ stock_data }) => {
    {console.log("test4", stock_data)} 
  // Check if stockList is null or empty
  if (!stock_data || stock_data.length === 0) {
    return <LoadingComponent />;
    
  }

  return (
    
<Table striped hover bordered size='sm' border style={{ borderCollapse: 'collapse' }}>
      <tbody>
  
        
          <React.Fragment>
            <tr>
              <td>Volume: {stock_data.volume}</td>
              <td>MarketCap: {stock_data.marketCap}</td>
              <td>Recom: {stock_data.recommendationMean}</td>
              </tr>
              <tr>
              <td>Price: {stock_data.currentPrice}</td>
              <td>High: {stock_data.high}</td>
              <td>Low: {stock_data.low}</td>
           
              </tr>
              <tr> 
              <td>52WeekHigh: {stock_data.fiftyTwoWeekHigh}</td>
              <td>52Weeklow: {stock_data.fiftyTwoWeekLow}</td>
              <td>52WeekCh: {stock_data.fiftyTwoWeekHigh}</td>
              </tr>
              <tr> 
              <td>P/E: {stock_data.forwardPE}</td>
              <td>forwardPE: {stock_data.forwardPE}</td>
              <td>high: {stock_data.high}</td>
            </tr>
          </React.Fragment>
        
      </tbody>
    </Table>
  );
};

export default KeyInfoComponent;
