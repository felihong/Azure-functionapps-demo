import logging
from PIL import Image
from io import BytesIO
import azure.functions as func


"""
Entry function configured by functions.json file:
blob data input is typed as InputStream.

Configuration details:
{
    "name": name of the blob variable, referenced in code
    "type": type of the trigger of binding, here is blobTrigger
    "direction": must be set as in
    "path": storage container to be monitored, use blob name patterns, e.g 
            "samples/original-{name}"
            "samples/{blobname}.{blobextension}"
            "samples/{name}.png"
    "connection": app setting name that stores connection string to the storage, use default storage connection if left empty
    "dataType": string by default, can be casted to bytes
}
"""
def main(
    # Blob trigger
    myblob: func.InputStream,
    # Input binding blob data bytes
    imgblob: bytes,
    # Output binding queue message string
    outmsg: func.Out[str]
):
    # Retrieve information from trigger input
    logging.info(f"New registration image received \n"
                f"Name: {myblob.name}")

    # Read input binding as bytes and convert to BW mode
    img = Image.open(BytesIO(imgblob)).convert("L")
    buf = BytesIO()
    img.save(buf, format="PNG")
    
    # Imperatively set a parameter as output type
    outmsg.set(f"Processing image {myblob.name} with {len(imgblob)} bytes")

    # Output binding as bytes
    return buf.getvalue()