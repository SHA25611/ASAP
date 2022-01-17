import wls_config as cnf
import os

admin_srv = cnf.listen_Address

mng_server = []

mng_dict = cnf.mng_server_matrix
for key in mng_dict:
	mng_server.append(mng_dict[key][0])


#print(admin_srv)  # This is admin machine ip for domain
#print(mng_server)

mng_server.sort()

#print("\n")
#print(mng_server)

unq_mng_srv = []

temp = mng_server[0]
unq_mng_srv.append(temp)

for item in mng_server:
	if(item == temp):
		continue
	else:
		unq_mng_srv.append(item)
		temp = item

#print("\n")
#print(unq_mng_srv)  # This is the list of managed server machine ips

''' Now we will create a auxilary text file that will
    store this information to assist ansible variable
'''

var_file = open(r"../../playbook_variables/dom_var.txt","w+")

# Preparing data to write

line1 = "---\n"
var_file.write(line1+"\n")
var_file.write("admin_server: "+admin_srv+"\n")
var_file.write("managed_servers:"+"\n")

data_lst = []

for item in unq_mng_srv:
	str = "     - "+item
	var_file.write(str+"\n")

var_file.write("domain_name: "+cnf.domain_name+"\n")
var_file.write("...\n")


var_file.close()

# Changing file extension to *.yml

txt_var_file = "../../playbook_variables/dom_var.txt"

file_name = os.path.splitext(txt_var_file) # file_name is a tupple with root and extension of the var_file

# renaming

os.rename(txt_var_file, file_name[0] + '.yml')

print("domain hosts var file successfully created")






		
