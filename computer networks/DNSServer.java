import java.io.*;
import java.net.*;
public class DNSServer {
    private static int indexOf(String[] arr,String str){
        str = str.trim();
        for(int i=0;i<arr.length;i++){
            if(arr[i].equals(str))return i;
        }
        return -1;
    }
    public static void main(String args[])throws IOException{
        String[] hosts = {"yahoo.com","gmail.com","criinfo.com","facebook.com"};
        String[] ip = {"68.180.206.184","232.232.232.232","232.232.232.231","232.232.232.230","232.232.232.234"};
        System.out.println("Press Ctrl+c to quit");
        while(true){
            DatagramSocket serversocket = new DatagramSocket(1362);
            byte[] senddata = new byte[1021];
            byte[]recivedata = new byte[1021];
            DatagramPacket recvpack = new DatagramPacket(recivedata,recivedata.length);
            serversocket.receive(recvpack);
            String sen = new String(recvpack.getData());
            InetAddress ipaddress = recvpack.getAddress();
            int port = recvpack.getPort();
            String capsent;
            System.out.println("Request for host"+sen);
            if(indexOf(hosts,sen)!=-1)capsent = ip[indexOf(hosts,sen)];
            else capsent = "host not found";
            senddata = capsent.getBytes();
            DatagramPacket pack = new DatagramPacket(senddata,senddata.length,ipaddress,port);
            serversocket.send(pack);
            serversocket.close();
        }
    }
}
