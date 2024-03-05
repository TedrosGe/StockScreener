
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

export default LineChartComponent;























