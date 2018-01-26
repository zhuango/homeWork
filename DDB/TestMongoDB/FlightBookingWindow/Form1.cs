using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using FlightBookingSystem;
using MongoDB.Bson;

namespace FlightBookingWindow
{
    public partial class Form1 : Form
    {
        private String mFrom;
        private String mTo;
        private DatabaseManager mDBManager;
        private BookingManager mBookingManager;
        private BoardingManager mBoardingManager;
        private TakingOffManager mTakingOffManager;
        public Form1()
        {
            InitializeComponent();
            this.mDBManager = new DatabaseManager("192.168.1.110", "20000");
            this.mBookingManager = new BookingManager(this.mDBManager);
            this.mBoardingManager = new BoardingManager(this.mDBManager);
            this.mTakingOffManager = new TakingOffManager(this.mDBManager);
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.mFrom = comboBox1.SelectedItem.ToString();
            this.mTo = comboBox2.SelectedItem.ToString();
            List<Flight> flights = this.mBookingManager.Query(this.mFrom, this.mTo);
            DateTime selectedDateStart = DateTime.Parse(dateTimePicker1.Text);
            DateTime selectedDateEnd = selectedDateStart + TimeSpan.FromDays(1);
            // Sort the flights by their taking off time.
            flights.Sort((Flight a, Flight b) =>
            {
                return a.Gtime.CompareTo(b.Gtime);
            });
            String show = "";
            comboBox3.Items.Clear();
            foreach (Flight flight in flights)
            {
                if (flight.Gtime >= selectedDateStart && flight.Gtime < selectedDateEnd)
                {
                    show += flight.ToString() + "\n";
                    // Add qualified flights to flight combobox.
                    comboBox3.Items.Add(flight.ID);
                }
            }
            richTextBox1.Text = show;
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Int32 flightID = Int32.Parse(comboBox3.SelectedItem.ToString());
            String seatNumber = comboBox4.SelectedItem.ToString();
            Int32 ID = Int32.Parse(textBox1.Text.Trim());
            String name = textBox3.Text.Trim();
            String Tnumber = textBox2.Text.Trim();
            this.mBookingManager.Book(ID, name, Tnumber, seatNumber, flightID);
            // Show information of passenger.
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void comboBox4_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox3_SelectedIndexChanged(object sender, EventArgs e)
        {
            int flightID = Int32.Parse(comboBox3.SelectedItem.ToString());
            Flight flight = new Flight(this.mDBManager.QueryFlight(flightID));
            List<String> show = new List<string>();

            comboBox4.Items.Clear();
            // Select available seats.
            foreach (var seat in flight.Spicture.Where((pair) => { return !pair.Value; }).ToList())
            {
                show.Add(seat.Key);
                // Add seat option to seat comboBox.
                comboBox4.Items.Add(seat.Key);
            }

            richTextBox1.Text = String.Join(", ", show);
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            String passengerName = textBox4.Text;
            Int32 flightID = Int32.Parse(textBox5.Text);
            DateTime date = DateTime.Parse(dateTimePicker2.Text);
            Passenger passenger = this.mBoardingManager.Query(passengerName, flightID, date);
            // generate pnumber.
            passenger.Pnumber = System.Guid.NewGuid().ToString();
            this.mBoardingManager.Board(passenger);
            richTextBox2.Text = passenger.ToString() + "\tboards successfully.";
        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {
        }

        private void dateTimePicker2_ValueChanged(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            Int32 airportID = Int32.Parse(textBox6.Text);
            Airport airport = this.mTakingOffManager.QueryAirport(airportID);
            List<Flight> flights = this.mTakingOffManager.QueryFlights(airportID);
            String info = airport.Name + "\n";
            foreach(Flight flight in flights)
            {
                info += flight.ToString() + "\n";
            }
            richTextBox3.Text = info;
        }

        private void textBox6_TextChanged(object sender, EventArgs e)
        {

        }

        private void richTextBox3_TextChanged(object sender, EventArgs e)
        {

        }

        private void richTextBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void comboBox5_SelectedIndexChanged(object sender, EventArgs e)
        {
            String airportName = comboBox5.SelectedItem.ToString();
            Airport airport = this.mTakingOffManager.QueryAirport(airportName);
            textBox6.Text = airport.ID.ToString();
        }
    }
}
