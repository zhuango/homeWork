using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
	public class TakingOffManager
	{
        private DatabaseManager mDBManager;

        public TakingOffManager(DatabaseManager dm)
        {
            this.mDBManager = dm;
        }
        public List<Airport> Airports
		{
			get
			{
				return this.query();
			}
		}

		private List<Airport> query()
		{
			return null;
		}
        public Airport QueryAirport(Int32 airportID)
        {
            Airport airport = new Airport(this.mDBManager.QueryAirport(airportID));
            return airport;
        }

        public List<Flight> QueryFlights(Int32 airportID)
        {
            List<Flight> flights = new List<Flight>();
            foreach(var docu in this.mDBManager.QueryFlightFromAirport(airportID))
            {
                flights.Add(new Flight(docu));
            }
            return flights;
        }
		public void ShowInfo()
		{
			foreach (Airport airport in Airports)
			{
				airport.ShowFlightInfomation();
			}
		}

		public void TakingOff()
		{
			foreach (Airport airport in Airports)
			{
				airport.TakeingOff();
			}
		}
	}
}
