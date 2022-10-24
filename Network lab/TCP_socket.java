import java.io.*;
import java.net.*;

public class TCP_socket {
    public TCP_socket(String host, int port) {
        try {
            Socket s = new Socket(host, port);
            System.out.println("Connected to " + s.getInetAddress());
            BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
            PrintWriter out = new PrintWriter(s.getOutputStream(), true);
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
            String userInput;
            while (!(userInput = stdIn.readLine()).equals("bye")) {
                try {
                    out.println(userInput);
                    System.out.println(in.readLine());

                } catch (IOException e) {
                    System.out.println("Exception caught when trying to listen on port " + port + " or listening for a connection");
                    System.out.println(e.getMessage());
                }

            }
            try {
                in.close();
                out.close();
                s.close();

            } catch (IOException e) {
                System.out.println("Exception caught when trying to close socket");
                System.out.println(e.getMessage());
            }
        } catch (IOException e) {
            System.out.println("Exception caught when trying to listen on port " + port + " or listening for a connection");
            System.out.println(e.getMessage());

        }
    }

    public static void main(String[] args) {
        TCP_socket socket = new TCP_socket("127.0.0.1", 5000);
    }

}


