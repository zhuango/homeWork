using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
	public class BoardingManager
	{
        private DatabaseManager mDBManager;
        public BoardingManager(DatabaseManager dm)
        {
            this.mDBManager = dm;
        }
		public Passenger Query(String name, Int32 flightNumber, DateTime date)
		{
            Passenger passenger = new Passenger(this.mDBManager.QueryPassenger(name, flightNumber));
            return passenger;
		}

		public Flight Query(String flightNumber)
		{
			return null;
		}

		public void Board(Passenger passenger)
		{
            this.mDBManager.UpdatePassenger(passenger.ID, "Pnumber", passenger.Pnumber);
            this.mDBManager.UpdateFlight(passenger.FlightNumber, String.Format("Spicture.{0}", passenger.Snumber), 1);
        }
	}
}
