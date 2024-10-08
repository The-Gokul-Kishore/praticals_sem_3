import java.io.*;
import java.net.*;

public class RAPServer {
    public static void main(String[] args) {
        try {
            DatagramSocket s = new DatagramSocket(1309);
            while (true) {
                byte[] sendbyte = new byte[1024];
                byte[] recivebyte = new byte[1024];
                
                // Receive the MAC address from the client
                DatagramPacket receiver = new DatagramPacket(recivebyte, recivebyte.length);
                s.receive(receiver);
                System.out.println("Received the stuff");

                // Convert received data to string and trim any extra spaces
                String macAddress = new String(receiver.getData()).trim();
                InetAddress clientAddress = receiver.getAddress();
                int clientPort = receiver.getPort();

                // Predefined MAC-to-IP mapping
                String[] ipAddresses = {"165.165.80.80", "165.165.79.1"};
                String[] macAddresses = {"6A:08:AA:C2", "8A:BC:E3:FA"};

                // Iterate over the MAC addresses and match with the received one
                for (int i = 0; i < macAddresses.length; i++) {
                    System.out.println("Checking entry " + i);
                    
                    // Compare received MAC address with the predefined ones
                    if (macAddresses[i].equalsIgnoreCase(macAddress)) {
                        System.out.println("Match found!");

                        // Send the corresponding IP address back to the client
                        sendbyte = ipAddresses[i].getBytes();
                        DatagramPacket sender = new DatagramPacket(sendbyte, sendbyte.length, clientAddress, clientPort);
                        s.send(sender);
                        break;
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("ERROR: " + e);
        }
    }
}
