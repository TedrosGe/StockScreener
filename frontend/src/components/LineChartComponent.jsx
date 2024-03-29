
import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';


const LineChartComponent = ({StockHistory}) =>{

    if (!StockHistory) {
    
    return <p>Loading chart...</p>;
  }
    return( 
    
      <div className='center-container'> 
      

  <ResponsiveContainer width="90%" height={350}  >
        
    <LineChart  data={StockHistory}>
      <XAxis  dataKey="date" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="close" name=" Price" stroke="#8884d8" />
    </LineChart>
  </ResponsiveContainer>
  </div> 
    )

}

export default LineChartComponent;























