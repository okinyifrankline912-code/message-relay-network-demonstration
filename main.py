import random
import time
import matplotlib.pyplot as plt

nodes = ["Node A", "Node B", "Node C", "Node D", "Node E"]

def split_message(message, size=3):
    return [message[i:i+size] for i in range(0, len(message), size)]

def send_packets(packets):
    received = []
    routes = []

    print("\n--- Sending packets through network ---\n")

    for packet in packets:
        path = []
        hops = random.randint(2, 5)

        # packet loss simulation (10%)
        if random.random() < 0.1:
            print(f"❌ Packet '{packet}' LOST")
            continue

        for _ in range(hops):
            node = random.choice(nodes)
            path.append(node)

        print(f"Packet '{packet}' route: {' -> '.join(path)}")

        received.append(packet)
        routes.append(len(path))

    return received, routes

def rebuild_message(packets):
    return "".join(packets)

def visualize(routes):
    if not routes:
        print("No data to visualize.")
        return

    plt.hist(routes, bins=range(1, 7), edgecolor="black")
    plt.title("Packet Path Length Distribution")
    plt.xlabel("Number of hops")
    plt.ylabel("Packets")
    plt.show()

message = input("Enter message: ")

packets = split_message(message)

print("\nPackets:", packets)

received, routes = send_packets(packets)

print("\nRebuilding message...")

final_message = rebuild_message(received)

print("\nFinal Message:", final_message)

print("\nShowing visualization...")
visualize(routes)
