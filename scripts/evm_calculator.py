# Python Script: Earned Value Management (EVM) & SPI/CPI Metrics Calculator

def calculate_evm(pv, ev, ac):
    """
    Calculates key Earned Value Management metrics for PMP/PMI-ACP project monitoring.
    PV: Planned Value
    EV: Earned Value
    AC: Actual Cost
    """
    cv = ev - ac  # Cost Variance
    sv = ev - pv  # Schedule Variance
    cpi = ev / ac if ac > 0 else 0  # Cost Performance Index
    spi = ev / pv if pv > 0 else 0  # Schedule Performance Index

    print("=== Earned Value Management (EVM) Analysis ===")
    print(f"[*] Planned Value (PV): ${pv:,.2f}")
    print(f"[*] Earned Value  (EV): ${ev:,.2f}")
    print(f"[*] Actual Cost   (AC): ${ac:,.2f}")
    print("---------------------------------------------")
    print(f"[*] Cost Variance (CV): ${cv:,.2f} -> {'Over Budget' if cv < 0 else 'Under Budget/On Track'}")
    print(f"[*] Schedule Variance (SV): ${sv:,.2f} -> {'Behind Schedule' if sv < 0 else 'Ahead/On Schedule'}")
    print(f"[*] CPI: {cpi:.2f} -> {'Over Budget' if cpi < 1 else 'Cost Efficient'}")
    print(f"[*] SPI: {spi:.2f} -> {'Behind Schedule' if spi < 1 else 'Schedule Efficient'}")

if __name__ == "__main__":
    # Example scenario: Project budgeted for $100k, currently 50% completed with $55k spent
    planned_val = 50000.0
    earned_val = 50000.0
    actual_cost = 55000.0
    
    calculate_evm(planned_val, earned_val, actual_cost)
