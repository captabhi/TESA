import java.io.*;
import java.net.*;

public class TCPClient {

	/**
	 * @param args
	 */
	public static void main(String[] args) 
	throws Exception{
		String set;
		String  modifiedSentence;
		BufferedReader inFromUser=
			   new BufferedReader(new InputStreamReader(System.in));
		Socket clientSocket=new Socket("127.0.0.1",12345);
		DataOutputStream outToServer=new DataOutputStream(clientSocket.getOutputStream()); 
		BufferedReader  inFromServer= new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
				
		//while(true)
		//{		
		// TODO Auto-generated method stub
		set=inFromUser.readLine();
		outToServer.writeBytes(set + '\n');
		modifiedSentence = inFromServer.readLine();
		System.out.println("From Server:" + modifiedSentence);
		clientSocket.close();
	//}
	}
}
