package serverPlusSqlDatabase;
import javax.net.ssl.*;
import javax.net.*;
import java.io.*;
import java.net.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.*;

class EchoThread extends Thread {
    protected Socket socket;
    protected Connection myConn;
    public EchoThread(Socket clientSocket,Connection conn) {
        this.socket = clientSocket;
        this.myConn=conn;
    }

    public void run() {
        InputStream inp = null;
        BufferedReader brinp = null;
        PrintWriter out = null;
       
        try {
        	 socket.setSoTimeout(60*1000);
            inp = socket.getInputStream();
            brinp = new BufferedReader(new InputStreamReader(inp));
            //out = new DataOutputStream(socket.getOutputStream());
            out=new PrintWriter(socket.getOutputStream(),true);

        } catch (Exception e) {
        	e.printStackTrace();
            return;
        }
        String line;
        while (true) {
            try {
                line = brinp.readLine();
                //System.out.println("received: "+line);
                Statement myStmt=myConn.createStatement();        
                if ((line == null) || line.equalsIgnoreCase("QUIT")) {
                		System.out.println(socket.getInetAddress());
                		socket.close();
                		return;
                } 
                else {
                	String sql="insert into tempTesaData values("+line+")";
                	myStmt.executeUpdate(sql);
                	System.out.println("Query Ok..");
                }
            }
            catch(java.net.SocketTimeoutException e)
            {
            	try
            	{
            	socket.close();
            	}
            	catch(Exception i)
            	{
            		i.printStackTrace();
            		
            	}
            }
            catch (Exception e) {
            	//if(e.equals(java.net.SocketTimeoutException))
                e.printStackTrace();
                return;
            }
        }
    }
}



public class serverPlusSqlDatabase {
static public int PORT=12345;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        ServerSocket serverSocket = null;
        Socket socket = null;
        ////////////////Initialising server
        try {
            serverSocket = new ServerSocket(PORT);
            //System.out.println("Timeout is:");
            //System.out.println(serverSocket.getSoTimeout());
            //serverSocket.setSoTimeout(60*1000);
        } catch (IOException e) {
            e.printStackTrace();

        }
        
        //////////////Connecting with database.......
        try {	
        	//DriverManager.registerDriver(new com.mysql.jdbc.Driver ());
        	//Class.forName("com.mysql.jdbc.Driver");
    		Connection conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/jtest","root","prashant");
    		while (true) {
                    socket = serverSocket.accept();
                    new EchoThread(socket,conn).start();
                    // new thread for a client
    		}


        }
        catch(Exception e)
        {
        	e.printStackTrace();
        }
        
                

	}

}
