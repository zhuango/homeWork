using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
    public class Airport
    {
        private int mID;
        private String mName;
        private String mSign;
        private String mRight;
        private String mArea;
        private String mSafe;

        public int ID { get { return this.mID; } }
        public String Name { get { return this.mName; } }
        public String Sign { get { return mSign; } }
        public String Right { get { return mRight; } }
        public String Area { get { return this.mArea; } }
        public String Safe { get { return this.mSafe; } }

        public List<Flight> Flights
        {
            get
            {
                return null;
            }
        }

        // "ID" : 3, "Name" : "LuKou, NangJing", "Sign" : "LN", "Right" : "NJ", "Area" : 3, "Safe" : "Be safe"
        public Airport(BsonDocument docu)
        {
            this.mID = docu["ID"].ToInt32();
            this.mName = docu["Name"].ToString();
            this.mSign = docu["Sign"].ToString();
            this.mRight = docu["Right"].ToString();
            this.mArea = docu["Area"].ToString();
            this.mSafe = docu["Safe"].ToString();
        }

        public void ShowFlightInfomation()
        {
            foreach (Flight flight in Flights)
            {
                // print information;
            }
        }

        public void TakeingOff()
        {
            // print infomation;
        }
    }
}
