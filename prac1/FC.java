import java.net.*;
import java.util.*;

public class FC {
    public static void main(String[] args) throws Exception {
        System.out.print("Enter number: ");
        String n = new Scanner(System.in).nextLine();

        String url = "http://localhost:5000/factorial?n=" + n;
        String response = new Scanner(new URL(url).openStream()).useDelimiter("\\A").next();
        System.out.println(response);
    }
}