#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <string.h>

// Node Number
String node = "0";

// Sensor Variables
float gas_data = 100;
float temp_data = -35;

// Wifi Config
const char* ssid = "SSID";
const char* password = "SSIDpasswd";

// Server Config
const char* serverName = "http://{ip}:{port}/Test_Key/push_data";

// Timer Delay config
unsigned long lastTime = 0;
unsigned long timerDelay = 3000;

// strings for JSON
String json_data;

// function definitions
String create_json(String node_no, String sensor_name, String sensor_value);
int send_data(String sensor_name, String sensor_value);


void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while(WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());
 
  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
  Serial.println("Node Number : " + node);
}


void loop() {
  //Send an HTTP POST request every 10 minutes
  if ((millis() - lastTime) > timerDelay) {
    //Check WiFi connection status
    if(WiFi.status()== WL_CONNECTED){
      // increment for testing purpose
      send_data(node, "mq135", String(gas_data++, 2));
      send_data(node, "DHT22", String(temp_data++, 2));
      
    }
    else {
      Serial.println("WiFi Disconnected");
    }
    lastTime = millis();
  }
}

String create_json(String node_no, String sensor_name, String sensor_value){
  return String("{\"node\":\"" + node_no + "\",\"sensor\":\"" + sensor_name + "\",\"sen_data\":\"" + sensor_value + "\"}");
}


int send_data(String node_no, String sensor_name, String sensor_value){
  int status = 0;

  WiFiClient client;
  HTTPClient http;
      
  http.begin(client, serverName);

  // Specify content-type header
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  http.addHeader("Content-Type", "application/json");
  json_data = create_json(node_no, sensor_name, sensor_value);
  
  int httpResponseCode = http.POST(json_data);
  Serial.print("HTTP Response code: ");
  Serial.println(httpResponseCode);
    
  // Free resources
  http.end();

  return status;
}