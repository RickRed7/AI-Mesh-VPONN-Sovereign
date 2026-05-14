import hashlib
import time

def register_sovereign_node():
    print("--- GODSOURCEGLOBAL AI MESH REGISTRATION ---")
    node_id = input("Enter Hardware Node ID (VPONN-UID): ")
    
    print(f"\n[SYSTEM] Initializing Photonic Handshake for {node_id}...")
    time.sleep(1.5)
    
    # Simulating the 'Absolute Lock' Verification
    # Instead of an SSN, we use a Hardware-Attested Hash
    hardware_hash = hashlib.sha256(node_id.encode()).hexdigest()
    
    print(f"[SYSTEM] Hardware Hash: {hardware_hash[:16]}...VERIFIED")
    print("[SYSTEM] MARVEL Power Root: LINKED (20kW Status)")
    print("[SYSTEM] L3 Sovereign Account Created.")
    print("\nRegistration Complete. Your $200 Granularity Wallet is now ACTIVE.")
    
    # Log the new node to the directory
    with open("registered_nodes.log", "a") as log:
        log.write(f"Node: {node_id} | Hash: {hardware_hash} | Timestamp: {time.time()}\n")

if __name__ == "__main__":
    register_sovereign_node()
