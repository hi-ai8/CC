import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class RupeeConverterClient {
    public static void main(String[] args) throws Exception {
        String rupees = "89";
        // String rupees = "85.70";
        @SuppressWarnings("deprecation")
        // URL url = new URL("http://127.0.0.1:5000/convert?fnt=" + rupees);
        URL url = new URL("http://127.0.0.1:5000/isprime?num=" + rupees);
        // URL url = new URL("http://localhost:5000/convert?inr=" + rupees);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine, response = "";

        while ((inputLine = in.readLine()) != null) {
            response += inputLine;
        }
        in.close();

        System.out.println("Response from server: " + response);
    }
}
