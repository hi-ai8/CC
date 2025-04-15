import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TemperatureConverterClient {
    public static void main(String[] args) {
        try {
            Scanner sc = new Scanner(System.in);
            System.out.print("Scale (celsius/fahrenheit): ");
            String scale = sc.nextLine();
            System.out.print("Temperature: ");
            String value = sc.nextLine();
            
            String url = "http://127.0.0.1:5000/convert?scale=" + scale + "&value=" + value;
            String response = new Scanner(new URL(url).openStream()).useDelimiter("\\A").next();
            System.out.println(response);
            
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}