from dataclasses import dataclass
from fileinput import filename
import socket
from venv import create 
from HTMLParse import *
# cache to keep track of post and get file names
 
@dataclass
class cacheCommand():
  def __init__(self, command,file,host,response):
        self.command = command
        self.file = file
        self.host =host
        self.response =response

# cache
cache =[]

def inCache(command,file,host):

      
      for c in cache:
        
        
       if c.command == command and c.file == file and c.host == host:
        return True
      
      return False
    
def getCachedCommand(command,file,host):
    for c in cache:
        
     if c.command == command and c.file==file and c.host== host :
        return c

def insertIntoCache(command,file,host,response):
    cache.append(cacheCommand(command,file,host,response))



def isEmpty():
    
    if cache==[]:
        return True
    else:
         return False
   

if __name__ == "__main__":
  while True:
    commandFile = input("Enter File Name : ")
    commands = []
    with open(commandFile) as f:
      lines = f.readlines()
      
      for l in lines:
        if '\n' in l:
          l = l[:-1]
        commands.append(l)
    f.close()
    
      
    for command in commands:
      
      print("doing command")
      print(command)

      CLIENT = socket.gethostbyname(socket.gethostname())
      clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
      command = command.split(' ')
    
      if len(command) < 3:
        print("Error in Command")
        continue
    
      if len(command) >= 3:
        if command[0].lower() != 'get' and command[0].lower() != 'post':
          print('Unhandled Command')
          continue
      
      
      if command[0].lower() == 'get':
        FILE_NAME = command[1]
        HOST = command[2]
        HOSTPort = 80 if len(command)<4 else command[3]
       
              
        if(not inCache("get",FILE_NAME,HOST)):
            
        
    

            
            request = f"GET {FILE_NAME} HTTP/1.1\r\nHost: {HOST}:{HOSTPort}\r\n\r\n"
            print(f"Connect to {HOST} port = {HOSTPort}")
            clientSocket.connect((HOST,int(HOSTPort)))
            #  response = clientSocket.recv(1024)
            #  print(response.decode('utf-8'))
            clientSocket.send(bytes(request,'utf-8'))  
            response = clientSocket.recv(1024)
            response = response.decode('utf-8')             
            parsedResponse = splitResponse(response)
            insertIntoCache("get",FILE_NAME,HOST,response)

            if parsedResponse[0][1] == "200":
              
              FILE_NAME = FILE_NAME.replace('/','_')
              f= open(FILE_NAME,"w+")
              f.write(parsedResponse[-1])
              f.close()
              print("File Recived and Saved")
            else:
              print(response)
              print("ERROR")
            
            clientSocket.close()
        else:
                 
               print("cached response is "+getCachedCommand("get",FILE_NAME,HOST).response)
               
                
          
          
          ## fetch folder

      elif command[0].lower() == 'post':
        FILE_NAME = command[1]
        HOST = command[2]
        HOSTPort = 80 if len(command)<4 else command[3]

        
     
        if(not inCache('post',FILE_NAME,HOST)):
          
          
          
        
          with open(FILE_NAME) as postFile:
            postFileLines = postFile.readlines()
            
          request = f"POST {FILE_NAME} HTTP/1.1\r\nHost: {HOST}:{HOSTPort}\r\n\r\n"
          for line in postFileLines:
           request = request +line
            
           clientSocket.connect((HOST,int(HOSTPort)))
          
           clientSocket.send(bytes(request,'utf-8'))  
           response = clientSocket.recv(1024)
           response = response.decode('utf-8')
           insertIntoCache("post",FILE_NAME,HOST,response)
           print(response)        
           clientSocket.close()
        else:
          print("cached response is "+getCachedCommand("post",FILE_NAME,HOST).response)
            
        
