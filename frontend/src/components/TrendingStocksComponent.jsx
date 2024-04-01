
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TrendingStockTable from "./TrendingStockTable"

const TrendingStocks = ()=>{
    const[trendingStocks, setTrendingStocks] = useState();
    const [loading, setLoading] = useState(true);
    //make fetchDate a reusable function--for later
    const fetchData = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/home`);
            const stocks = response.data.stocks;
            setTrendingStocks(stocks);
    
            setLoading(false);
    
        } catch (error) {
          console.error("Stock fetch failed", error);
          setLoading(false); 
        }
      };
    
      useEffect(() => { fetchData(); }, []);
    return(
       <div>
       
       <div>
        {
            <TrendingStockTable />
        }
        
        
        
         </div>
        
       
       </div>
    )


}
export default TrendingStocks