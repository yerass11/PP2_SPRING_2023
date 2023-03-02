import json

with open('sample-data.json') as file:
    json_data = json.load(file)
    print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
    imdata = json_data["imdata"]
    for item in imdata:
        nestit = item["l1PhysIf"]
        attribs = nestit["attributes"]
        dn = attribs["dn"]
        speed = attribs["speed"]
        mtu = attribs["mtu"]
        output = ""
        if len(dn) == 42:
            output += dn + "                              " + speed + "   " + mtu
        else:
            output += dn + "                               " + speed + "   " + mtu

        print(output)