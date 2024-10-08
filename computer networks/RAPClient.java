import java.io.*;
import java.net.*;
public class RAPClient {
    public static void main(String[] args) {
        try{
            DatagramSocket client =new DatagramSocket();
            InetAddress addr = InetAddress.getByName("127.0.0.1");
            byte[] sendbyte = new byte[1024];
            byte[] receivebyte= new byte[1024];
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            System.out.println("Enter the physical address(MAC):");
            String macAddress = in.readLine();

            sendbyte = macAddress.getBytes();
            DatagramPacket sender = new DatagramPacket(sendbyte,sendbyte.length,addr,1309);
            client.send(sender);
            DatagramPacket reciver =new DatagramPacket(receivebyte,receivebyte.length);
            client.receive(reciver);
            String ipAddress = new String(reciver.getData());
            System.out.println("THE Logical ADDress (IP) is : "+ ipAddress);
            client.close();
        }catch(IOException e){
            System.out.println("ERROR:"+e.getMessage());
        }
    }
}
