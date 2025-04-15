import java.net.URI;
import java.net.http.*;
import java.util.Scanner;

public class PCC {
    public static void main(String[] args) throws Exception {
        System.out.print("Enter number: ");
        String number = new Scanner(System.in).nextLine();
        String url = "http://localhost:5000/check_prime?number=" + number;
        var response = HttpClient.newHttpClient()
                .send(HttpRequest.newBuilder().uri(URI.create(url)).build(),
                        HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}