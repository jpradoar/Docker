# MQTT server,writer,reader

### Run broker server
docker run -itd --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto:1.5.8


### Logic
<pre>

                        ---------
                        | Graph | 
                        ---------             
              --------     |
       _______| MQTT |_____|
      |       --------
   --------    | | |
   | core |    | | |
   --------    | | |
               | | |____________________________
      _________| |                              |
     |           |_________                     |
     |                     |                    |
 --------------        --------------       ------------
 | client_001 |        | client_002 |       | client_n |
 --------------        --------------       ------------

</pre>
