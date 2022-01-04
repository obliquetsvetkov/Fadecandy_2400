import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import processing.net.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class readopcForStrandsver3 extends PApplet {


int opcState=0;
int channelNumber=0;
int command = -1;
int dataLowByte=0;
int dataHighByte=0;
int dataLength=0;
int dataRead=0;
int port = 7890;
IntList pixelValues;

int padding=20;
int spacing=19;
int pixelsPerStrip=60;
int numberOfStrips=6;
float pixelHeight=10;
float pixelWidth = 10;



Server myServer;        

public void setup()
{
  
  print(((pixelsPerStrip-1)*spacing)+(2*padding));
print(numberOfStrips*padding*2);
  background(0);
  stroke(0);
  pixelValues=new IntList();
  myServer = new Server(this, port);
}

public void draw()
{  

  // Get the next available client
  Client thisClient = myServer.available();
  // If the client is not null, then read and process data

  if (thisClient !=null) {
    while (thisClient.available ()>0) {
      int currentByte=thisClient.read();
      //first byte is channel 0 is broadcast, any other number specifies an individual channel
      //second byte is command, 0 is set pixel colours
      //length of data high byte
      //length of data low byte
      //data

      switch(opcState) {
      case 0:
        channelNumber = currentByte;
        pixelValues.clear();
        print("channel ");
        print(channelNumber);
        print("  ");
        opcState++;
        break;
      case 1:
        command = currentByte;
        print("command ");
        print(command);
        print("  ");
        opcState++;
        break;
      case 2:
        dataHighByte=currentByte;
        print("high ");
        print(dataHighByte);
        print(" ");
        opcState++;
        break;
      case 3:
        dataLowByte=currentByte;
        print("low ");
        print(dataLowByte);
        print(" ");

        //combinelow and high here
        dataHighByte=dataHighByte<<8;
        dataLength=dataHighByte|dataLowByte;
        print("combined ");
        println(dataLength);
        opcState++;
        break;
      case 4:
        pixelValues.append(currentByte);
        dataRead++;
        if (dataRead==dataLength) {
          //message is finished
          displayData();
          opcState=0;
          dataRead=0;
          dataLength=0;
          command = -1;
          channelNumber = -1;
        }
      }
    }
  }
}

public void displayData() {
  background(0);
  stroke(127);
  for (int i=1; i<numberOfStrips; i++) {
    line(0, i*padding*2, width, i*padding*2);
  }
  stroke(0);
  int red=0;
  int green=0;
  int blue=0;

  float step =  PApplet.parseFloat(width-(3*padding))/((pixelValues.size()/3)-1);
  int size = 10;
  for (int i=0; i<pixelValues.size (); i++) {
    int pixelNumber=i/3;    
    switch(i%3) {
    case 0:
      red=pixelValues.get(i);
      break;
    case 1:
      green=pixelValues.get(i);
      break;
    case 2:
      blue=pixelValues.get(i);
      fill(red, green, blue);
      ellipseMode(CENTER);
      ellipse(padding + ((pixelNumber%pixelsPerStrip)*spacing), padding + ((pixelNumber/pixelsPerStrip)*padding*2), pixelWidth, pixelHeight) ;
    }
  }
}
  public void settings() {  size(800, 600); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "readopcForStrandsver3" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
