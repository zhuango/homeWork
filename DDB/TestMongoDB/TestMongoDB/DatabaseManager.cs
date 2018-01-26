using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
    public class DatabaseManager
    {
        private MongoClient mMongoClient;
        private IMongoDatabase mFlightBooking;
        private IMongoCollection<BsonDocument> mPassenger;
        private IMongoCollection<BsonDocument> mAirport;
        private IMongoCollection<BsonDocument> mFlight;
        private FilterDefinitionBuilder<BsonDocument> filterBuilder = Builders<BsonDocument>.Filter;
        private UpdateDefinitionBuilder<BsonDocument> updateBuilder = Builders<BsonDocument>.Update;

        public IMongoCollection<BsonDocument> Flight { get { return this.mFlight; } }
        public IMongoCollection<BsonDocument> Airport { get { return this.mAirport; } }
        public IMongoCollection<BsonDocument> Passenger { get { return this.mPassenger; } }

        public DatabaseManager(String serverIP, String port)
        {
            this.mMongoClient = new MongoClient(String.Format("mongodb://{0}:{1}", serverIP, port));
            this.mFlightBooking = this.mMongoClient.GetDatabase("FlightBooking");
            this.mPassenger = this.mFlightBooking.GetCollection<BsonDocument>("Passenger");
            this.mAirport = this.mFlightBooking.GetCollection<BsonDocument>("Airport");
            this.mFlight = this.mFlightBooking.GetCollection<BsonDocument>("Flight");
        }

        public void InsertAirport(BsonDocument airport)
        {
            this.mAirport.InsertOne(airport);
        }
        public void DeleteAirports()
        {
            var filter = this.filterBuilder.Lt("ID", 50);
            var result = this.mAirport.DeleteMany(filter);
            Console.WriteLine(result.DeletedCount);
        }

        public void DeleteAirport(int ID)
        {
            var filter = this.filterBuilder.Eq("ID", ID);
            var result = this.mAirport.DeleteOne(filter);
            Console.WriteLine(result.DeletedCount);
        }

        public BsonDocument QueryPassenger(String name, Int32 flightID)
        {
            var filter = this.filterBuilder.Eq("Name", name) & this.filterBuilder.Eq("FlightNumber", flightID);
            var results = this.mPassenger.Find(filter).First();
            return results;
        }
        public BsonDocument QueryFlight(int ID)
        {
            var filter = this.filterBuilder.Eq("ID", ID);
            var result = this.mFlight.Find(filter).First();

            return result;
        }
        public List<BsonDocument> QueryFlight(String gAirportName, String aAirportName)
        {
            var filter = this.filterBuilder.Eq("Name", gAirportName);
            var gAirport = this.mAirport.Find(filter).First();

            filter = this.filterBuilder.Eq("Name", aAirportName);
            var aAirport = this.mAirport.Find(filter).First();
            Console.WriteLine(aAirport["ID"]);

            return QueryFlight(gAirport["ID"].ToInt32(), aAirport["ID"].ToInt32());
        }

        public List<BsonDocument> QueryFlight(int gAirportID, int aAorportID)
        {
            var filter = this.filterBuilder.Eq("GAirport", gAirportID) & this.filterBuilder.Eq("AAirport", aAorportID);
            var results = this.mFlight.Find(filter).ToList();

            return results;
        }
        public List<BsonDocument> QueryFlightFromAirport(Int32 airportID)
        {
            var filter = this.filterBuilder.Eq("GAirport", airportID);
            var results = this.mFlight.Find(filter).ToList();

            return results;
        }
        public BsonDocument QueryAirport(Int32 airportID)
        {
            var filter = this.filterBuilder.Eq("ID", airportID);
            try
            {
                var result = this.mAirport.Find(filter).First();
                return result;
            }
            catch(Exception ex)
            {
                return null;
            }
        }
        public BsonDocument QueryAirport(String airportName)
        {
            var filter = this.filterBuilder.Eq("Name", airportName);
            try
            {
                var result = this.mAirport.Find(filter).First();
                return result;
            }
            catch (Exception ex)
            {
                return null;
            }
        }
        //public List<BsonDocument> QueryFlight(int flightNumber)
        //{

        //}
        public void InsertFlight(BsonDocument flight)
        {
            this.mFlight.InsertOne(flight);
        }

        public void InsertPassenger(BsonDocument passenger)
        {
            this.mPassenger.InsertOne(passenger);
        }
        public void DeletePassenger()
        {
            var filter = this.filterBuilder.Lt("ID", 100);
            var result = this.mPassenger.DeleteMany(filter);
            Console.WriteLine(result.DeletedCount);
        }
        public void UpdatePassenger(Int32 ID, String property, String newValue)
        {
            var filter = this.filterBuilder.Eq("ID", ID);
            var update = this.updateBuilder.Set(property, newValue);
            var result = this.mPassenger.UpdateOne(filter, update);
        }
        public void UpdateFlight(Int32 ID, String property, Int32 newValue)
        {
            var filter = this.filterBuilder.Eq("ID", ID);
            var update = this.updateBuilder.Set(property, newValue);
            var result = this.mFlight.UpdateOne(filter, update);
        }
        public void UpdateFlight(Int32 ID, String property, String newValue)
        {
            var filter = this.filterBuilder.Eq("ID", ID);
            var update = this.updateBuilder.Set(property, newValue);
            var result = this.mFlight.UpdateOne(filter, update);
        }

        public void DeleteFlight()
        {
            var filter = this.filterBuilder.Lt("ID", 50);
            var result = this.mFlight.DeleteMany(filter);
            Console.WriteLine(result.DeletedCount);
        }
        public void DeleteFlight(int ID)
        {
            var filter = this.filterBuilder.Eq("ID", ID);
            var result = this.mFlight.DeleteOne(filter);
            Console.WriteLine(result.DeletedCount);
        }
    }
}
