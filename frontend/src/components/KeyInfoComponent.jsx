import React from 'react';







const LoadingComponent = () => (
  <p>Loading...</p>
);

const KeyInfoComponent = ({ stock_data }) => {

  // Check if stockList is null or empty
  if (!stock_data || stock_data.length === 0) {
    return <LoadingComponent />;
    
  }

  return (
    <div class =" bg-indigo-950"> 
<table class=" mx-auto text-neutral-100 font-mono text-md  text-left  w-10/12 h-full"  >
      <tbody>
     
        
          <React.Fragment>
            <tr>
              <td >company: {stock_data.company}</td>
              <td>marketCap: {stock_data.marketCap}</td>
              <td>recommendation: {stock_data.recommendationMean}</td>
              </tr>
              <tr>
              <td>price: {stock_data.currentPrice}</td>
              <td>high: {stock_data.high}</td>
              <td>low: {stock_data.low}</td>
           
              </tr>
              <tr> 
              <td>52WeekHigh: {stock_data.fiftyTwoWeekHigh}</td>
              <td>52Weeklow: {stock_data.fiftyTwoWeekLow}</td>
              <td>52WeekCh: {stock_data.fiftyTwoWeekHigh}</td>
              </tr>
              <tr> 
              <td>forward PE: {stock_data.forwardPE}</td>
              <td>volume: {stock_data.volume}</td>
              <td>industry: {stock_data.industry}</td>
            </tr>
          </React.Fragment>
        
      </tbody>
    </table>
    </div>
  );
};

export default KeyInfoComponent;
