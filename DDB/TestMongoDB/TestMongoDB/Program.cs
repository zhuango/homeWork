using MongoDB.Bson;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FlightBookingSystem
{
	class Program
	{
		static void Main(string[] args)
		{
            DatabaseManager dm = new DatabaseManager("192.168.1.110", "20000");
            Passenger passenger = new Passenger(dm.QueryPassenger("zhuanglui", 7));
            //dm.DeleteAirports();
            //InsertAirport(dm);
            //Test();
            BookingManager bm = new BookingManager(dm);
            List<Flight> flights0 = bm.Query(1, 2);
            //List<Flight> flights1 = bm.Query("ZhouShuiZi, Dalian", "ShuangLiu, ChenDu");
        }
        static void Test()
        {
            DatabaseManager dm = new DatabaseManager("192.168.1.110", "20000");
            //dm.DeleteFlight();
            //InsertFlight(dm);

            dm.DeletePassenger();
            InsertPassenger(dm);

            //dm.UpdateFlight(100, "Spicture.A001", 0);
            //DateTime now = DateTime.Now;
            //DateTime nownow = DateTime.Now;
            //if (now < nownow)
            //{
            //    Console.WriteLine("early");
            //}
            //string date = DateTime.Now.ToString();
            //DateTime generatedFromStr = DateTime.Parse(date);
            //Console.WriteLine(generatedFromStr.ToString());
        }
        static void InsertPassenger(DatabaseManager dm)
		{
			var document = new BsonDocument
			{
				{"ID", 1 },
				{"Name", "Ksa" },
				{"Tnumber", "13423235432" },
				{"Snumber", "E012" },
				{"Tkind", "12"},
				{"Pnumber", "12" },
				{"FlightNumber", 4 }
			};
            dm.InsertPassenger(document);
		}
        static void InsertFlight(DatabaseManager dm)
        {
            List<String> airports = new List<string> { "", "ZhouShuiZi, Dalian", "ShuangLiu, ChenDu", "LuKou, NangJing" };
            Random random = new Random();
            for (int i = 0; i < 50; i++)
            {
                BsonDocument spic = new BsonDocument
                {
                    { "A001", 0 },
                    { "A002", 0 },
                    { "A003", 0 },
                    { "A004", 0 },
                    { "A005", 0 },
                    { "A006", 0 },
                    { "A007", 0 },
                    { "B001", 0 },
                    { "B002", 0 },
                    { "B003", 0 },
                    { "B004", 0 },
                    { "B005", 0 },
                    { "B006", 0 },
                    { "B007", 0 },
                    { "C001", 0 },
                    { "C002", 0 },
                    { "C003", 0 },
                    { "C004", 0 },
                    { "C005", 0 },
                    { "C006", 0 },
                    { "C007", 0 },
                    { "D001", 0 },
                    { "D002", 0 },
                    { "D003", 0 },
                    { "D004", 0 },
                    { "D005", 0 },
                    { "D006", 0 },
                    { "D007", 0 },
                };
                DateTime now = DateTime.Now + TimeSpan.FromMinutes(random.Next(120, 1500));
                int fromAirport = random.Next(1, 4);
                int toAirport = random.Next(1, 4);
                while (toAirport == fromAirport)
                {
                    toAirport = random.Next(1, 4);
                }
                var document = new BsonDocument
                {
                    { "ID", i },
                    { "Number", i },
                    { "Date", now.ToString()},
                    { "Seat", "DL" },
                    {"Entry", 1 },
                    {"Delay", "EnNa" },
                    {"Spicture", spic},
                    {"Gtime", now.ToString() },
                    {"Atime", (now +  TimeSpan.FromMinutes(random.Next(120, 1500))).ToString()},
                    {"GAirport", fromAirport },
                    {"AAirport", toAirport },
                    {"GAirportName", airports[fromAirport]},
                    {"AAirportName", airports[toAirport] }
                };
                dm.InsertFlight(document);
            }
			
		}
		static void InsertAirport(DatabaseManager dm)
		{
            var document0 = new BsonDocument
            {
                { "ID", 1 },
                { "Name", "ZhouShuiZi, Dalian" },
                { "Sign", "ZD" },
                { "Right", "DL" },
                {"Area", 1 },
                {"Safe", "Be save" }
            };
            var document1 = new BsonDocument
            {
                { "ID", 2 },
                { "Name", "ShuangLiu, ChenDu" },
                { "Sign", "SC" },
                { "Right", "CD" },
                {"Area", 2 },
                {"Safe", "Be safe" }
            };
            var document2 = new BsonDocument
            {
                { "ID", 3 },
                { "Name", "LuKou, NangJing" },
                { "Sign", "LN" },
                { "Right", "NJ" },
                {"Area", 3 },
                {"Safe", "Be safe" }
            };
            //var document = new BsonDocument
            //{
            //	{ "ID", 4 },
            //	{ "Name", "Inter, Nanjing" },
            //	{ "Sign", "IN" },
            //	{ "Right", "NJ" },
            //	{"Area", 4 },
            //	{"Safe", "Be safe" }
            //};
            dm.InsertAirport(document0);
            dm.InsertAirport(document1);
            dm.InsertAirport(document2);
        }

		static void FindDocument()
		{
			MongoClient mongoClient = new MongoClient("mongodb://192.168.1.108:20000");
			var database = mongoClient.GetDatabase("FlightBooking");
			var collection = database.GetCollection<BsonDocument>("Airport");
			var document = collection.Find(new BsonDocument()).FirstOrDefault();
			Console.WriteLine(document.ToString());
		}
		static async Task TestMongoDBAsync()
		{
			MongoClient mongoClient = new MongoClient("mongodb://192.168.1.108:20000");
			var database = mongoClient.GetDatabase("testdb");
			var collection = database.GetCollection<BsonDocument>("FlightBooking");
			await collection.InsertOneAsync(new BsonDocument("Name", "Jack"));
			var list = await collection.Find(new BsonDocument("Name", "Jack")).ToListAsync();
			foreach (var document in list)
			{
				Console.WriteLine(document["Name"]);
			}
		}
	}
}
