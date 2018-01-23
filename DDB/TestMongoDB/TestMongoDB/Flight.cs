using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
    public class Flight
    {
        private int mID;
        private int mNumber;
        private DateTime mDate;
        private String mSeat;
        private int mEntry;
        private Dictionary<String, Boolean> mSpicture;
        private String mDelay;
        private DateTime mGtime;
        private DateTime mAtime;
        private int mGAirport;
        private int mAAirport;
        private String mGAirportName;
        private String mAAirportName;

        public int ID { get { return this.mID; } }
        public int Number { get { return this.mNumber; } }
        public DateTime Date { get { return this.mDate; } }
        public String Seat { get { return this.Seat; } }
        public int Entry { get { return this.mEntry; } }
        public Dictionary<String, Boolean> Spicture { get { return this.mSpicture; } }
        public String Delay { get { return this.mDelay; } }
        public DateTime Gtime { get { return this.mGtime; } }
        public DateTime Atime { get { return this.mAtime; } }
        public int GAirport { get { return this.mGAirport; } }
        public int AAirport { get { return this.mAAirport; } }
        public String GAirportName { get { return this.mGAirportName; } }
        public String AAirportName { get { return this.mAAirportName; } }


        public Flight(BsonDocument document)
        {
            // "GAirport" : 1, "AAirport" : 2 }

            this.mID = document["ID"].ToInt32();
            this.mNumber = document["Number"].ToInt32();
            this.mDate = DateTime.Parse(document["Date"].ToString());
            this.mSeat = document["Seat"].ToString();
            this.mEntry = document["Entry"].ToInt32();
            this.mDelay = document["Delay"].ToString();
            this.mSpicture = FormSpicture(document["Spicture"].AsBsonDocument);
            this.mGtime = DateTime.Parse(document["Gtime"].ToString());
            this.mAtime = DateTime.Parse(document["Atime"].ToString());
            this.mGAirport = document["GAirport"].ToInt32();
            this.mAAirport = document["AAirport"].ToInt32();
            this.mGAirportName = document["GAirportName"].ToString();
            this.mAAirportName = document["AAirportName"].ToString();
        }
        private Dictionary<String, Boolean> FormSpicture(BsonDocument document)
        {
            Dictionary<String, Boolean> spicture = new Dictionary<string, bool>();
            foreach (String name in document.Names)
            {
                try
                {
                    String tag = document[name].ToString();
                    if (tag == "1")
                    {
                        spicture[name] = true;
                    }
                    else
                    {
                        spicture[name] = false;
                    }
                }
                catch (Exception ex)
                {
                    spicture[name] = false;
                }
            }

            return spicture;
        }
        public override String ToString()
        {
            return String.Format("{0}: {1}, {2} ----> {3}, {4}",
                mNumber,
                mGAirportName,
                mGtime,
                mAAirportName,
                mAtime);
        }

    }
}
