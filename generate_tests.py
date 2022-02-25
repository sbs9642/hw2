with open('0_input','w') as f:
    f.write('GET /index.html HTTP/1.0\n')
    
with open('0_client_output','w') as f:
    f.write('GET /index.html HTTP/1.0\n')
    f.write('Method = GET\n')
    f.write('Request-URL = /index.html\n')
    f.write('HTTP-Version = HTTP/1.0\n')
    f.write('<!DOCTYPE html>\n')
    f.write('<html>\n')
    f.write('<body>\n')
    f.write('<h1>COMP431</h1>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    
with open('0_server_output','w') as f:
    f.write("")
    
with open('1_input','w') as f:
    f.write('get index.html HTTP/1.0\n')
    
with open('1_client_output','w') as f:
    f.write('get index.html HTTP/1.0\n')
    f.write('ERROR -- Invalid Method token.\n')
    
with open('1_server_output','w') as f:
    f.write("")
    
with open('2_input','w') as f:
    f.write('GET /index©.html HTTP/1.0\n')
    
with open('2_client_output','w') as f:
    f.write('GET /index©.html HTTP/1.0\n')
    f.write('ERROR -- Invalid Absolute-Path token.\n')
    
with open('2_server_output','w') as f:
    f.write("")
