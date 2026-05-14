import time

class OMDynamicDistributor:
    def __init__(self, target_buffer=2000.0):
        self.current_buffer = 0.0
        self.threshold = target_buffer # Trigger O&M at k increments
        self.om_history = []

    def sync_with_l3_contract(self, incoming_allocation):
        """Simulates pulling the 15% allocation from SovereignEnergySwap.sol"""
        self.current_buffer += incoming_allocation
        print(f"[L3 -> Buffer] Ingress: ${incoming_allocation:.2f} | Current Pool: ${self.current_buffer:.2f}")
        
        if self.current_buffer >= self.threshold:
            self.trigger_om_payout()

    def trigger_om_payout(self):
        print("\n--- [SYSTEM] O&M THRESHOLD REACHED ---")
        payout_amount = self.current_buffer
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Simulated Distribution Logic
        distribution = {
            "MARVEL_Core_Maintenance": payout_amount * 0.40,  # 40% to Nuclear Foundation
            "VPONN_Lattice_Optimization": payout_amount * 0.40, # 40% to Photonic Logic
            "Regional_Infrastructure": payout_amount * 0.20     # 20% to Oceanside Mesh
        }
        
        self.om_history.append({"time": timestamp, "amount": payout_amount})
        self.current_buffer = 0.0 # Reset buffer after flush
        
        for dept, amt in distribution.items():
            print(f"RELEASED: ${amt:.2f} to {dept}")
        print("--- [SYSTEM] INFRASTRUCTURE SECURED ---\n")

if __name__ == "__main__":
    distributor = OMDynamicDistributor(target_buffer=500.0)
    
    # Simulate a series of swaps reaching the threshold
    simulated_swaps = [150.0, 200.0, 180.0] 
    for swap in simulated_swaps:
        time.sleep(0.5)
        distributor.sync_with_l3_contract(swap)
