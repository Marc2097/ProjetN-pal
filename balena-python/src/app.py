import sys

# Add parent directories to the system path
sys.path.append(".")
sys.path.append("..")
sys.path.append("../..")

# Import the HologramCloud class from the Hologram module
from Hologram.HologramCloud import HologramCloud

if __name__ == "__main__":
    # Print introductory messages
    print("")
    print("")
    print("Testing Hologram Cloud class...")
    print("")
    print("* Note: You can obtain device keys from the Devices page")
    print("* at https://dashboard.hologram.io")
    print("")

    # Create an instance of the HologramCloud class with an empty dictionary as the configuration
    # and set the network type to 'cellular'
    hologram = HologramCloud(dict(), network='cellular')

    # Print the type of the cloud (HologramCloud) instance
    print('Cloud type: ' + str(hologram))

    # Send a message to the Hologram Cloud with specified topics and timeout
    recv = hologram.sendMessage('one two three!',
                                topics=['TOPIC1', 'TOPIC2'],
                                timeout=3)

    # Print the response message received from the Hologram Cloud
    print('RESPONSE MESSAGE: ' + hologram.getResultString(recv))
