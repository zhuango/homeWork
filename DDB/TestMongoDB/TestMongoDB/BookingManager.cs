using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
	public class BookingManager
	{
		private DatabaseManager mDBManager;
        private List<String> mPlaces;
        public List<String> Places { get { return this.mPlaces; } }

        public BookingManager(DatabaseManager dm)
		{
			this.mDBManager = dm;
            this.mPlaces = new List<string> { "ZhouShuiZi, Dalian", "ShuangLiu, ChenDu", "LuKou, NangJing" };
        }
        public BookingManager(DatabaseManager dm, List<string> places)
        {
            this.mDBManager = dm;
            this.mPlaces = places;
        }
		public List<Flight> Query(String gAirportName, String aAirportName)
		{
			List<Flight> flights = new List<Flight>();
			var results = this.mDBManager.QueryFlight(gAirportName, aAirportName);
			foreach (var document in results)
			{
				flights.Add(new Flight(document));
			}
			return flights;
		}

		public List<Flight> Query(int gAirportID, int aAorportID)
		{
			List<Flight> flights = new List<Flight>();
			var results = this.mDBManager.QueryFlight(gAirportID, aAorportID);
			foreach (var document in results)
			{
				flights.Add(new Flight(document));
			}
			return flights;
		}
		public Passenger Book(Int32 ID, String name, String phoneNnumber, String seatNumber, Int32 flightID)
		{
			//generation.
			String tkind = "000";
			String pNumber = "000";
			var document = new BsonDocument
			{
				{"ID", ID },
				{"Name", name },
				{"Tnumber", phoneNnumber },
				{"Snumber", seatNumber },
				{"Tkind", tkind},
				{"Pnumber", pNumber },
				{"FlightNumber", flightID }
			};

			this.mDBManager.InsertPassenger(document);
            this.mDBManager.UpdateFlight(flightID, String.Format("Spicture.{0}", seatNumber), 1);
            return new Passenger(document);
		}
	}
}
