# Moving Average Crossover Logger Strategy

## 📌 Strategy Description

This strategy is designed to **compute and log simple moving averages (MA4 and MA7)** for subscribed instruments in real-time using bulk data feeds. It is primarily a **signal observation tool**, not a direct trading execution strategy.  

### 🔄 Steps Followed
1. Subscribe to instruments provided in the event (`subscribeList`).  
2. Initialize a history structure for each instrument to store:  
   - `timestamp`  
   - `lastPrice`  
   - `ma4` (4-period moving average)  
   - `ma7` (7-period moving average)  
3. On each bulk data feed update:  
   - Append the latest timestamp and last price.  
   - Compute MA4 and MA7 based on the most recent prices.  
   - Store and log these values for monitoring.  
4. Provide a utility function `movingAverage()` to retrieve the latest MA values (MA4, MA7, or any custom period).  

### 📊 Trading Interpretations
- **MA4 > MA7** → Indicates **short-term upward momentum** (bullish signal).  
- **MA4 < MA7** → Indicates **short-term downward momentum** (bearish signal).  
- **Crossover Events**:  
  - When MA4 crosses above MA7 → Potential **buy signal**.  
  - When MA4 crosses below MA7 → Potential **sell signal**.  

⚠️ *Note: This code currently only computes and logs signals. Trade execution logic can be added based on these crossover signals.*  

---

## 📚 Libraries Used
- **AlgoAPI**  
  - `AlgoAPIUtil` → Provides utility functions for AlgoAPI.  
  - `AlgoAPI_Backtest` → Enables backtesting environment and event handling. 
