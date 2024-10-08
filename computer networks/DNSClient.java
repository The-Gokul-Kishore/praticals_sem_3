import java.io.*;
import java.net.*;

public class DNSClient {
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        DatagramSocket clientsocket = new DatagramSocket();
        InetAddress ipadderess;
        if(args.length==0){
            ipadderess = InetAddress.getLocalHost();

        }else{
            
        }
    }    
}
