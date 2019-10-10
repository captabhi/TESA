
import java.io.*;
import java.net.*;

public class TCPServer {

	public static void main(String argv[]) throws Exception {
		String clientSentence;
		String capitalizedSentence;
		try {
		ServerSocket welcomeSocket = new ServerSocket(12345);
		while(true) {
			Socket connectionSocket = welcomeSocket.accept();
			System.out.println("Got connection......");
			BufferedReader inFormClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
			//DataOutputStream outToClient=new DataOutputStream(connectionSocket.getOutputStream()); 
			PrintWriter outToClient=new PrintWriter(connectionSocket.getOutputStream(),true);

			clientSentence = inFormClient.readLine();
			System.out.println("Server received: "+clientSentence);
			capitalizedSentence = clientSentence.toUpperCase() ;
			outToClient.println(capitalizedSentence);
			System.out.println("Server sent: "+capitalizedSentence);
			
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	

	}
}
