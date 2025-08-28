
from AlgoAPI import AlgoAPIUtil, AlgoAPI_Backtest

class AlgoEvent:
    def __init__(self):
        self.data_history = {}

    def start(self, mEvt):
        self.evt = AlgoAPI_Backtest.AlgoEvtHandler(self, mEvt)
        self.myinstrument = mEvt['subscribeList']

        # Initialize structure for each instrument
        for instrument in self.myinstrument:
            self.data_history[instrument] = {
                'timestamp': [],
                'lastPrice': [],
                'ma4': [],
                'ma7': []
            }

        self.evt.start()

    def on_bulkdatafeed(self, isSync, bd, ab):
        for instrument in self.myinstrument:
            if instrument not in bd:
                continue

            # Get latest data
            timestamp = bd[instrument]['timestamp']
            lastPrice = bd[instrument]['lastPrice']

            # Store timestamp and price
            hist = self.data_history[instrument]
            hist['timestamp'].append(timestamp)
            hist['lastPrice'].append(lastPrice)

            # Compute and store MA4 and MA7
            ma4 = self._calculate_moving_average(hist['lastPrice'], 4)
            ma7 = self._calculate_moving_average(hist['lastPrice'], 7)
            hist['ma4'].append(ma4)
            hist['ma7'].append(ma7)

            # Log result
            self.evt.consoleLog(
                f"{instrument} | LastPrice={lastPrice}, MA4={ma4}, MA7={ma7}"
            )

    def _calculate_moving_average(self, data, period):
        if len(data) < period:
            return None
        return sum(data[-period:]) / period

    def movingAverage(self, instrument, period):
        """
        Returns the latest MA4 or MA7 for lastPrice of an instrument.
        """
        if instrument not in self.data_history:
            return None
        if period == 4:
            return self.data_history[instrument]['ma4'][-1] if self.data_history[instrument]['ma4'] else None
        elif period == 7:
            return self.data_history[instrument]['ma7'][-1] if self.data_history[instrument]['ma7'] else None
        else:
            # Compute on-demand for custom period
            return self._calculate_moving_average(self.data_history[instrument]['lastPrice'], period)

    # Other event methods (unchanged)
    def on_marketdatafeed(self, md, ab): 
        pass
    def on_newsdatafeed(self, nd): 
        pass
    def on_weatherdatafeed(self, wd): 
        pass
    def on_econsdatafeed(self, ed): 
        pass
    def on_corpAnnouncement(self, ca): 
        pass
    def on_orderfeed(self, of): 
        pass
    def on_dailyPLfeed(self, pl):
        pass
    def on_openPositionfeed(self, op, oo, uo):
        pass

