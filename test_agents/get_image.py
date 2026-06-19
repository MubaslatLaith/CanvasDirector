

from contextmanager.apiclient.invokeai.client import InvokeAIClient

INVOKE_URL = "http://127.0.0.1:9091"
USERNAME = "email@email.email"
PASSWORD = "weakpassword" 

api_client = InvokeAIClient(INVOKE_URL)
user = api_client.login(USERNAME, PASSWORD)


input_board_name = "In Board"  
input_image_name = api_client.boards.get_image_ids_by_board_name (input_board_name) 

output_board_name = "Out Board" 
output_image_name = api_client.boards.get_image_ids_by_board_name (output_board_name) 


print ('input image')
print(input_image_name) 
i = 0
input_image_url = api_client.images.get_image_url(input_image_name[i]) 
print(input_image_url)


print('output image') 
print(output_image_name) 
i= 0 
output_image_url = api_client.images.get_image_url(output_image_name[i]) 
print (output_image_url)




