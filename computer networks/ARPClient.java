import java.io.*;
import java.net.*;
public class ARPClient {
    public static void main(String args[])throws IOException{
        try{
            Socket ss = new Socket(InetAddress.getLocalHost(),1100);
            PrintStream ps = new PrintStream(ss.getOutputStream());
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String ip;
            System.out.println("Enter the IP ADDRESS");
            ip = br.readLine();
            ps.println(ip);
            BufferedReader br2 = new BufferedReader(new InputStreamReader(ss.getInputStream()));
            System.out.println("ARP from server:");
            String str;
            while(!((str=br2.readLine()).equalsIgnoreCase("end"))){
                System.out.println(str);
            }
            ss.close();
        }catch(IOException e){
            System.out.println("Error:"+e);
        }
    }
}
