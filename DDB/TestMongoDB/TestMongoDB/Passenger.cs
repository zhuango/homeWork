using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
    public class Passenger
    {
        private int mID;
        private String mName;
        private String mTnumber;
        private String mSnumber;
        private String mTkind;
        private String mPnumber;
        private int mFlightNumber;

        public int ID { get { return this.mID; } }
        public String Name { get { return this.mName; } }
        // telephone number
        public String Tnumber { get { return this.mTnumber; } }
        // seat number
        public String Snumber { get { return this.mSnumber; } }
        // ticket kind
        public String Tkind { get { return this.mTkind; } }
        // package number
        public String Pnumber { get { return this.mPnumber; } set { this.mPnumber = value; } }
        public int FlightNumber { get { return this.mFlightNumber; } }

        public Passenger(BsonDocument document)
        {
            this.mID = document["ID"].ToInt32();
            this.mName = document["Name"].ToString();
            this.mTnumber = document["Tnumber"].ToString();
            this.mSnumber = document["Snumber"].ToString();
            this.mTkind = document["Tkind"].ToString();
            this.mPnumber = document["Pnumber"].ToString();
            this.mFlightNumber = document["FlightNumber"].ToInt32();
        }

        public override string ToString()
        {
            return String.Format("{0}\t{1}\t{2}\t{3}", this.mID, this.mName, this.FlightNumber, this.Pnumber);
        }
    }
}
