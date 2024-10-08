import java.io.*;
import java.net.*;
public class ARPServer {
    public static void main(String[] args) {
        try{
            ServerSocket ss = new ServerSocket(1100);
            Socket s = ss.accept();
            PrintStream ps = new PrintStream(s.getOutputStream());
            BufferedReader br1 = new BufferedReader(new InputStreamReader(s.getInputStream()));
            String ip = br1.readLine();
            Runtime r = Runtime.getRuntime();
            Process p = r.exec("cmd /c arp -a " + ip);

            BufferedReader br2  = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String str;
            while((str=br2.readLine())!=null){
                ps.println(str);
            }
            ps.println("end");
            ss.close();
        }catch(IOException e){
            System.out.println("Error:"+e);
        }
    }
}
